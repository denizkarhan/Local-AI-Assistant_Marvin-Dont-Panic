import os
import sys
import whisper
import numpy as np
import sounddevice as sd
import scipy.io.wavfile

class VoiceAssistant:
    def __init__(self, fs=44100, chunk_size=1024, silence_threshold=0.0001, silence_duration=3, model_name="small"):
        self.fs = fs
        self.chunk_size = chunk_size
        self.silence_threshold = silence_threshold
        self.silence_duration = silence_duration
        self.model_name = model_name
        self.model = whisper.load_model(self.model_name)

    def record_audio(self, output_filename='audio.mp3'):
        recording = []
        silent_chunks = 0
        max_silent_chunks = int(self.silence_duration * self.fs / self.chunk_size)

        print("Recording started. The recording will stop if 3 seconds of silence is detected.")

        def callback(indata, frames, time, status):
            nonlocal silent_chunks
            if status:
                print(status, file=sys.stderr)
            volume_norm = np.linalg.norm(indata) / frames
            recording.append(indata.copy())
            silent_chunks += 1 if volume_norm < self.silence_threshold else 0

        with sd.InputStream(samplerate=self.fs, channels=1, callback=callback, blocksize=self.chunk_size):
            while True:
                if silent_chunks >= max_silent_chunks:
                    break
                sd.sleep(int(1000 * self.chunk_size / self.fs))

        recorded_data = np.concatenate(recording, axis=0)
        scipy.io.wavfile.write(output_filename, self.fs, recorded_data)
        print(f"Recording saved to '{output_filename}'.")

    def transcribe_audio(self, input_filename='audio.mp3'):
        result = self.model.transcribe(input_filename)
        os.remove(input_filename)
        return result["text"]

    def get_question(self):
        self.record_audio()
        transcription = self.transcribe_audio()
        return transcription
