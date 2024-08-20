from transformers import AutoModelForCausalLM, AutoTokenizer
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
    def __init__(self, model_name="HuggingFaceTB/SmolLM-360M-Instruct", base_prompt="I'd like you to answer my questions briefly!\n"):
        self.device = "cpu"
        self.base_prompt = base_prompt
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)

    def send_prompt(self, prompt):
        logging.info(f"Sending prompt to chat model: {prompt}")
        try:
            data = [
                        {
                            "role": "user",
                            "content": self.base_prompt + prompt
                        }
                    ]
            
            input_text = self.tokenizer.apply_chat_template(data, tokenize=False)            
            logging.info(f"Sending prompt to chat model: {input_text}")
            inputs = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
            outputs = self.model.generate(inputs, max_new_tokens=50, temperature=0.2, top_p=0.9, do_sample=True)
            content = self.tokenizer.decode(outputs[0]).split("\n")[-1].strip("<|im_end|>")
            print(f"Received response from chat model: {content}")
            logging.info(f"Received response from chat model: {content}")
            return content

        except requests.RequestException as e:
            raise APIError(f"Failed to connect to API: {e}")

