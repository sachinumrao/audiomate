from abc import ABC, abstractmethod

import librosa
import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor


class BaseSTTModel(ABC):
    @abstractmethod
    def load_model(self, model_path: str):
        pass

    @abstractmethod
    def convert_text_to_audio(self, audio_filepath: str, output_filepath: str):
        pass


class WhisperSTTModel(BaseSTTModel):
    def load_model(self, model_path: str):
        self.device = "cpu"
        self.processor = WhisperProcessor.from_pretrained(model_path)
        self.model = WhisperForConditionalGeneration.from_pretrained(model_path)
        self.model.config.forced_decoder_ids = self.processor.get_decoder_prompt_ids(
            language="english", task="transcribe"
        )
        self.model.to(self.device)

    def convert_text_to_audio(self, audio_filepath: str, output_filepath: str):
        audio, sr = librosa.load(audio_filepath, sr=16000, mono=True)
        inputs = self.processor(audio, sampling_rate=16000, return_tensors="pt")
        input_features = inputs.input_features.to(self.device)
        with torch.no_grad():
            predicted_ids = self.model.generate(input_features)

        text = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

        # save text to file
        with open(output_file_path, "w") as f:
            f.write(text)


if __name__ == "__main__":
    # test whisper model
    model_name = "openai/whisper-tiny"
    audio_file_path = "./results/news.wav"
    output_file_path = "./results/news_transcribed.txt"

    whisper_model = WhisperSTTModel()
    whisper_model.load_model(model_name)
    whisper_model.convert_text_to_audio(audio_file_path, output_file_path)

# Fix: whisper model loading
