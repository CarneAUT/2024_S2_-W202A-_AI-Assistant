import os
from dotenv import load_dotenv
from groq import Groq
from prompts import chat_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()


def generate_text(content, system_prompt):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(

        messages=[

            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": f"{content}",
            }
        ],

        # The language model which will generate the completion.
        model="llama-3.1-70b-versatile",

        temperature=0.5,
        max_tokens=8000,
        top_p=1,
        stop=None,
        stream=False,
    )

    response = chat_completion.choices[0].message.content

    return response


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def rag_pipeline(content):
    os.getenv("GROQ_API_KEY")
    llm = ChatGroq(model="llama-3.2-90b-text-preview")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.create_documents([content])
    vectorstore = InMemoryVectorStore.from_documents(documents=splits, embedding=HuggingFaceEmbeddings())

    retriever = vectorstore.as_retriever()
    prompt_template = PromptTemplate.from_template(chat_prompt)

    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt_template
            | llm
            | StrOutputParser()
    )

    return rag_chain


def generate_chat_response(rag_chain, question):
    return rag_chain.invoke(question)
