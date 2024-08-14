# Local-AI-Assistant_Marvin-Dont-Panic
Your fully customizable native AI assistant, powered by Whisper, llama3.1, Phi-3-Mini and transformers.VitsModel. It is a language model with voice command processing capabilities, tailored to your own needs and use cases.

---

### Install the necessary dependencies to start the installation. Let's do this step by step through the terminal 🛠️
```bash
  git clone git@github.com:denizkarhan/Local-AI-Assistant_Marvin-Dont-Panic.git
  cd Local-AI-Assistant_Marvin-Dont-Panic/
```

### Using pyenv we have to set up the download of the necessary packages in the python@3.11.7 version environment. 
```bash
  pyenv install 3.11.7
  pyenv virtualenv 3.11.7 dont_panic
  pyenv activate dont_panic
  pip install -r requirements.txt
```


### Download ollama (Linux & macOS) | To run and chat with phi3: 
```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ollama run phi3
```

### Here are some example models that can be downloaded 🎊

| Model                | Parameters | Size   | Download                             |
|----------------------|------------|--------|--------------------------------------|
| Llama 3.1            | 8B         | 4.7GB  | `ollama run llama3.1`                |
| Llama 3.1            | 70B        | 40GB   | `ollama run llama3.1:70b`            |
| Llama 3.1            | 405B       | 231GB  | `ollama run llama3.1:405b`           |
| Phi 3 Mini           | 3.8B       | 2.3GB  | `ollama run phi3`                    |
| Phi 3 Medium         | 14B        | 7.9GB  | `ollama run phi3:medium`             |
| Gemma 2              | 2B         | 1.6GB  | `ollama run gemma2:2b`               |
| Gemma 2              | 9B         | 5.5GB  | `ollama run gemma2`                  |
| Gemma 2              | 27B        | 16GB   | `ollama run gemma2:27b`              |
| Mistral              | 7B         | 4.1GB  | `ollama run mistral`                 |
| Moondream 2          | 1.4B       | 829MB  | `ollama run moondream`               |
| Neural Chat          | 7B         | 4.1GB  | `ollama run neural-chat`             |
| Starling             | 7B         | 4.1GB  | `ollama run starling-lm`             |
| Code Llama           | 7B         | 3.8GB  | `ollama run codellama`               |
| Llama 2 Uncensored   | 7B         | 3.8GB  | `ollama run llama2-uncensored`       |
| LLaVA                | 7B         | 4.5GB  | `ollama run llava`                   |
| Solar                | 10.7B      | 6.1GB  | `ollama run solar`                   |

‼️ You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

### REST API
- Ollama has a REST API for running and managing models, generate a response

```python
    def llm_request(self, prompt):
        logging.info(f"Sending prompt to chat model: {prompt}")
        try:
            data = {
                # model = Llama 3.1 | Phi 3 Mini
                "model": self.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": "I'd like you to answer my questions briefly!\n" + prompt 
                    }
                ],
                "stream": False
            }

            headers = {
                "Content-Type": "application/json"
            }

            # self.url = http://localhost:11434/api/chat
            response = requests.post(self.url, headers=headers, json=data)
```

### Available Whisper models and languages
Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

| Size     | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|----------|------------|--------------------|--------------------|---------------|----------------|
| tiny     | 39 M       | `tiny.en`          | `tiny`             | ~1 GB         | ~32x           |
| base     | 74 M       | `base.en`          | `base`             | ~1 GB         | ~16x           |
| small    | 244 M      | `small.en`         | `small`            | ~2 GB         | ~6x            |
| medium   | 769 M      | `medium.en`        | `medium`           | ~5 GB         | ~2x            |
| large    | 1550 M     | N/A                | `large`            | ~10 GB        | 1x             |
