import logging
from MeloTTS.melo.api import TTS
from pydub import AudioSegment
from pydub.playback import play

model = TTS(language='EN', device='cpu')
speaker_ids = model.hps.data.spk2id

class SpeechSynthesizer:
    def __init__(self):
        self.speed = 1.0
        self.speaker_ids = model.hps.data.spk2id
        self.model = TTS(language='EN', device='cpu')
        self.response = "None"
        self.output_path = "output_path.wav"

    def text_to_speech(self, text):
        logging.info(f"Converting text to speech: {text}")
        try:
            self.model.tts_to_file(text, speaker_ids['EN-Default'], self.output_path, speed=self.speed)

            logging.info("Playing audio...")

            song = AudioSegment.from_wav(self.output_path)
            print('playing sound using  pydub')
            play(song)

            logging.info("Audio playback completed.")
        except Exception as e:
            logging.error(f"Error in text_to_speech: {e}")
