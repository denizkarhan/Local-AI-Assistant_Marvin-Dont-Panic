from melo.api import TTS

model = TTS(language='EN', device='cpu')
speaker_ids = model.hps.data.spk2id

podcast = 'The field of text-to-speech has seen rapid development recently.'

output_path = 'en-default.wav'
a = model.tts_to_file(podcast, speaker_ids['EN-Default'], output_path)

print(type(a))