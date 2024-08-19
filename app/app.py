import logging
from flask import Flask, render_template, jsonify, request
from src import chat_model, speech_synthesizer_melotts, voice_assistant

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

voice_assistant_stt = voice_assistant.VoiceAssistant()
model = chat_model.ChatModel()
synthesizer = speech_synthesizer_melotts.SpeechSynthesizer()

@app.route('/')
def index():
    return render_template('index.html')

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
            response = model.send_prompt(question)
            synthesizer.response = response
        except chat_model.APIError as e:
            logging.error(f"Error during chat model interaction: {e}")
            return jsonify({'text': 'There was an error processing your request.'}), 500

        return jsonify({'text': response})
    
    return jsonify({'text': 'Invalid question provided.'}), 400

@app.route('/speaker', methods=['POST'])
def speaker():
    try:
        synthesizer.text_to_speech(synthesizer.response)
    except chat_model.APIError as e:
        logging.error(f"Error during chat model interaction: {e}")
        return jsonify({'text': 'There was an error processing your request.'}), 500
    return jsonify({'text': 'Invalid question provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
