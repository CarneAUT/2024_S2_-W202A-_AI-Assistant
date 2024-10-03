import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

def generate_text(course_content):
        history = [
            {"role": "system",
             "content": "Create a Mock Quiz using the following course content"},
            {"role": "user",
             "content": f"Course Content:\n{course_content}"}
        ]

        chat_completion = client.chat.completions.create(
            messages=history,
            model="llama3-8b-8192",
        )

        return chat_completion.choices[0].message.content

        # generated_text = ""
        # for chunk in chat_completion:
        #     if chunk.choices and chunk.choices[0] and chunk.choices[0].delta and chunk.choices[0].delta.content:
        #         generated_text += chunk.choices[0].delta.content
        #
        # return generated_text

course_content = """
he concept of supply chain management has evolved significantly over the past few decades. In the past, companies were primarily focused on managing their internal operations and supply chains were often fragmented and disjointed. However, with the rise of globalization and the increasing complexity of global supply chains, companies have come to realize the importance of managing their supply chains effectively. This has led to the development of supply chain management as a distinct discipline, with its own set of principles, practices, and tools.

Effective supply chain management involves a range of activities, including demand forecasting, inventory management, logistics, and supply chain risk management. It also requires a deep understanding of the company's internal operations and its relationships with its suppliers, customers, and other stakeholders. Supply chain managers must be able to analyze data and make informed decisions quickly, as well as communicate effectively with other stakeholders. In addition, they must be able to adapt to changing circumstances and respond to disruptions in the supply chain.

One of the key challenges facing supply chain managers is the need to balance competing demands and priorities. For example, companies may need to balance the need to reduce costs with the need to improve customer service. They may also need to balance the need to respond quickly to changes in demand with the need to maintain a stable and reliable supply chain. To address these challenges, supply chain managers must be able to use a range of tools and techniques, including data analytics, simulation modeling, and scenario planning. They must also be able to work collaboratively with other stakeholders to identify and prioritize opportunities for improvement.
"""

print(generate_text(course_content))