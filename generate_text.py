import os
from dotenv import load_dotenv
from groq import Groq

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