import wave
from piper import PiperVoice

voice = PiperVoice.load("./models/en_US-lessac-medium.onnx")
with wave.open("./results/test.wav", "wb") as wav_file:
    voice.synthesize_wav("Welcome to the world of speech synthesis!", wav_file)
