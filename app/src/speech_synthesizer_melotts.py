import logging
from MeloTTS.melo.api import TTS
from pydub import AudioSegment
from pydub.playback import play

class SpeechSynthesizer:
    def __init__(self):
        self.speed = 1.0
        self.language = 'EN'
        self.device = 'cpu'
        self.model = TTS(language=self.language, device=self.device)
        self.speaker_native = "EN-Default"
        self.speaker_ids = self.model.hps.data.spk2id
        self.response = "None"
        self.output_path = "output_path.wav"

    def text_to_speech(self, text):
        logging.info(f"Converting text to speech: {text}")
        try:
            self.model.tts_to_file(text, self.speaker_ids[self.speaker_native], self.output_path, speed=self.speed)

            logging.info("Playing audio...")

            song = AudioSegment.from_wav(self.output_path)
            print('playing sound using  pydub')
            play(song)

            logging.info("Audio playback completed.")
        except Exception as e:
            logging.error(f"Error in text_to_speech: {e}")
