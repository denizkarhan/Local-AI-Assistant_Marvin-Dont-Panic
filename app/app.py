import os
import logging
from flask import Flask, render_template, jsonify, request
from src import chat_model, chat_model_HuggingFaceTB, speech_synthesizer_melotts, voice_assistant

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

voice_assistant_stt = voice_assistant.VoiceAssistant()
llm_model = chat_model_HuggingFaceTB.ChatModel()
synthesizer = speech_synthesizer_melotts.SpeechSynthesizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/reset-prompt', methods=['POST'])
def reset_prompt():
    llm_model.base_prompt = "I'd like you to answer my questions briefly!\n"
    print("prompt reset complete!")
    return jsonify({"status": "success", "data": "success"})

@app.route('/api/submit-prompt', methods=['POST'])
def submit_prompt():
    data = request.json.get('prompt')
    llm_model.base_prompt += data + "\n"
    return jsonify({"status": "success", "data": data})

@app.route('/api/submit-data', methods=['POST'])
def submit_data():
    data = request.json
    voice_assistant_stt.model_reload(data)
    return jsonify({"status": "success", "data": data})

@app.route('/api/select-model', methods=['POST'])
def select_model():
    global llm_model
    modelNames = {
        "Llama 3.1": "llama3.1",
        "Phi 3 Mini": "phi3",
        "Gemma 2": "gemma2",
        "Mistral": "gemma2:2b",
        "Neural Chat": "neural-chat",
        "Code Llama": "codellama"
    }
    select_model = request.json.get('button_text')
    print(f"Clicked button text: {modelNames[select_model]}")
    if select_model != "HuggingFaceTB":
        ollamaModel = modelNames[select_model]
        os.system("ollama run " + ollamaModel)
        llm_model = chat_model.ChatModel(model_name=ollamaModel)

    return jsonify({"status": "success", "button_text": select_model})

@app.route('/api/select-lang', methods=['POST'])
def select_lang():
    data = request.json
    speaker = data.get('button_text')
    synthesizer.speaker_native = speaker
    print(f"Clicked button text: {speaker}")
    return jsonify({"status": "success", "button_text": speaker})

@app.route('/record', methods=['POST'])
def record():
    question = voice_assistant_stt.get_question()
    return jsonify({'text': question if question else 'I did not understand what you said.'})

@app.route('/answer', methods=['POST'])
def answer():
    data = request.json
    question = data.get('question', '')

    if question and question != 'I did not understand what you said.':
        try:
            response = llm_model.send_prompt(question)
            synthesizer.response = response
        except llm_model.APIError as e:
            logging.error(f"Error during chat model interaction: {e}")
            return jsonify({'text': 'There was an error processing your request.'}), 500

        return jsonify({'text': response})
    
    return jsonify({'text': 'Invalid question provided.'}), 400

@app.route('/speaker', methods=['POST'])
def speaker():
    try:
        synthesizer.text_to_speech(synthesizer.response)
    except llm_model.APIError as e:
        logging.error(f"Error during chat model interaction: {e}")
        return jsonify({'text': 'There was an error processing your request.'}), 500
    return jsonify({'text': 'Invalid question provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
