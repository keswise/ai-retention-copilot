from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_push(segment):

    prompt = f"""
    You are a CRM marketer.

    Customer Segment:
    {segment}

    Generate one high-converting push notification.

    Requirements:
    - Maximum 100 characters
    - Clear CTA
    - Personalized tone
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


def generate_whatsapp(segment):

    prompt = f"""
    You are a CRM marketer.

    Customer Segment:
    {segment}

    Generate a WhatsApp campaign message.

    Requirements:
    - Conversational tone
    - Include CTA
    - Include personalization placeholder {{name}}
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


def generate_email(segment):

    prompt = f"""
    You are a CRM marketer.

    Customer Segment:
    {segment}

    Generate:

    Subject Line

    Email Body

    Requirements:
    - Personalized
    - Retention focused
    - Clear CTA
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

    print("\n----- PUSH -----\n")

    print(
        generate_push(
            "At Risk"
        )
    )

    print("\n----- WHATSAPP -----\n")

    print(
        generate_whatsapp(
            "At Risk"
        )
    )

    print("\n----- EMAIL -----\n")

    print(
        generate_email(
            "At Risk"
        )
    )