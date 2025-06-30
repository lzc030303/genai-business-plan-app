import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("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"),  # your real OpenRouter key
    base_url="https://openrouter.ai/api/v1"
)

def generate_business_plan(idea: str) -> str:
    prompt = f"""You are a business consultant. Based on this startup idea: "{idea}", write a business plan including:
    - Problem it solves
    - Target market
    - Unique value proposition
    - Monetization strategy
    - Go-to-market plan
    """

    response = client.chat.completions.create(
    model="meta-llama/llama-4-maverick:free",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=800
)

    return response.choices[0].message.content
