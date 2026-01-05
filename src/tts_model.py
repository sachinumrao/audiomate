import wave
from abc import ABC, abstractmethod

from piper import PiperVoice


class BaseTTSModel(ABC):
    @abstractmethod
    def load_model(self, model_path: str):
        pass

    @abstractmethod
    def generate_audio(self, text: str, output_filepath: str):
        pass


class PiperTTSModel(BaseTTSModel):
    def load_model(self, model_path: str) -> None:
        self.model = PiperVoice.load(model_path)

    def generate_audio(self, text: str, output_filepath: str) -> None:
        with wave.open(output_filepath, "wb") as wav_file:
            self.model.synthesize_wav(text, wav_file)


if __name__ == "__main__":
    sample_text = """Manchester United has fired manager Ruben Amorim after a rollercoaster spell at the Premier League giant, the club confirmed on Monday.
    A club statement said the Red Devils’ hierarchy “reluctantly made the decision that it is the right time to make a change.”
    “This will give the team the best opportunity of the highest possible Premier League finish,” the statement added. “The club would like to thank Ruben for his contribution to the club and wishes him well for the future.”
    Amorim was tasked with rebuilding the team when he took over in November 2024 but has struggled to find consistency over his 14 months in charge.
    The club currently sits sixth in the Premier League after another uninspiring draw against Leeds United on Sunday.
    There was clearly tension building behind the scenes at Old Trafford with Amorim hinting on Sunday that he was unhappy with interference from the club’s leadership.
    “I just want to say that I’m going to be the manager of this team, not just the coach. I was really clear on that,” he said in what proved to be his last news conference at United."""

    model_name = "./models/en_US-lessac-medium.onnx"
    output_filepath = "./results/news.wav"

    piper_model = PiperTTSModel()
    piper_model.load_model(model_name)
    piper_model.generate_audio(sample_text, output_filepath)
