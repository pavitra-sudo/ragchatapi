from openai import OpenAI

from app.config import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_answer(
    question: str,
    context_chunks: list[str]
):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in context, say:
"I could not find relevant information."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    return response.choices[0].message.content