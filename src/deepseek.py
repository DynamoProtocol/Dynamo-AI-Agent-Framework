import requests

class DeepSeekAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1"  # Replace with actual API URL

    def analyze(self, portfolio_data):
        try:
            response = requests.post(
                f"{self.base_url}/analyze",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=portfolio_data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error calling DeepSeek API: {e}")
            return None
