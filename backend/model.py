import os
from mistralai import Mistral
from dotenv import load_dotenv

class PromptEnhancer:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.model = "mistral-large-latest"
        self.client = Mistral(api_key=self.api_key)

    def enhance_prompt(self, prompt: str) -> str:
        system_prompt = "Improve the following prompt by making it more specific, clear, and effective:"
        
        response = self.client.chat.complete(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"Original prompt: {prompt}\n\nEnhanced prompt:"
                }
            ]
        )
        
        return response.choices[0].message.content.strip()
