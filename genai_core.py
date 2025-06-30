from openai import OpenAI

client = OpenAI(
    api_key="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",  # your real OpenRouter key
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
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",    
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800,
    )
    return response.choices[0].message.content
