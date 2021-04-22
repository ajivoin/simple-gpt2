import requests


class TextGenerator:
    def __init__(self, deepai_api_key: str):
        """
        Get API key from https://deepai.org/
        """
        self.api_key = deepai_api_key

    def generate(self, base_text: str) -> str:
        try:
            return requests.post(
                "https://api.deepai.org/api/text-generator",
                data={
                    "text": base_text,
                },
                headers={"api-key": self.api_key},
            ).json()["output"]
        except Exception as e:
            print(f"Error: {e}")
            return None
