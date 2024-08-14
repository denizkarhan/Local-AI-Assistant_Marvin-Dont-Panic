import logging
import torch
import numpy as np
from pydub.playback import play
from pydub import AudioSegment
from transformers import VitsModel, AutoTokenizer

class SpeechSynthesizer:
    def __init__(self, model=None, tokenizer=None, model_name="facebook/mms-tts-eng"):
        self.model = model if model else VitsModel.from_pretrained(model_name)
        self.tokenizer = tokenizer if tokenizer else AutoTokenizer.from_pretrained(model_name)
        self.response = "None"

    def text_to_speech(self, text):
        logging.info(f"Converting text to speech: {text}")
        try:
            inputs = self.tokenizer(text, return_tensors="pt")
            with torch.no_grad():
                output = self.model(**inputs).waveform

            output_numpy = output.cpu().numpy()
            if output_numpy.ndim > 1:
                output_numpy = output_numpy[0]

            output_numpy = np.int16(output_numpy / np.max(np.abs(output_numpy)) * 32767)
            audio_segment = AudioSegment(
                output_numpy.tobytes(),
                frame_rate=18000,
                sample_width=2,
                channels=1
            )

            logging.info("Playing audio...")
            play(audio_segment)
            logging.info("Audio playback completed.")
        except Exception as e:
            logging.error(f"Error in text_to_speech: {e}")