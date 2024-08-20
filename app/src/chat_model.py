import logging
import requests

class APIError(Exception):
    """Custom exception for API errors."""
    
    def __init__(self, message, status_code=None, response_text=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_text = response_text

    def __str__(self):
        base_message = f"APIError: {self.args[0]}"
        if self.status_code is not None:
            base_message += f" (Status Code: {self.status_code})"
        if self.response_text:
            base_message += f"\nResponse Text: {self.response_text}"
        return base_message

class ChatModel:
    def __init__(self, url="http://localhost:11434/api/chat", model_name="phi3", base_prompt="I'd like you to answer my questions briefly!\n"):
        self.url = url
        self.model_name = model_name
        self.base_prompt = base_prompt

    def send_prompt(self, prompt):
        logging.info(f"Sending prompt to chat model: {prompt}")
        try:
            data = {
                "model": self.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": self.base_prompt + prompt 
                    }
                ],
                "stream": False
            }

            headers = {
                "Content-Type": "application/json"
            }

            response = requests.post(self.url, headers=headers, json=data)
            response.raise_for_status()
            content = response.json()['message']['content']
            logging.info(f"Received response from chat model: {content}")
            return content
        except requests.RequestException as e:
            raise APIError(f"Failed to connect to API: {e}", status_code=response.status_code, response_text=response.text)
