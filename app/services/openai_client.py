import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

def generate_story_from_prompt(prompt: str) -> str | None:
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # veya "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "Sen yaratıcı, özgün bir çocuk masalı yazarı ve pedagogsun."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=1000
        )
        content = response.choices[0].message.content
        return content.strip() if isinstance(content, str) else None
    except Exception as e:
        return f"[HATA]: {str(e)}"


