from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def get_recommendation(segment):

    prompt = f"""
    You are an expert CRM and Retention Marketing strategist.

    Customer Segment:
    {segment}

    Provide:

    1. Retention Strategy
    2. Communication Channels
    3. Timing
    4. Offer Recommendation
    5. Expected Outcome

    Keep the response practical and concise.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    print(
        get_recommendation(
            "At Risk"
        )
    )