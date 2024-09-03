# File: custom_phonemizer.py

from PersianG2p import Persian_g2p_converter
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

_DEF_FA_PUNCS = "؟ ! ) ("
class CustomPhonemizer(BasePhonemizer):
     language = "fa"
    def __init__(self, punctuations=_DEF_FA_PUNCS, keep_puncs=False, **kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)
        self.converter = Persian_g2p_converter(True)
    
    def phonemize(self, text):
        # Call the appropriate method from Persian_g2p_converter to perform phonemization
        # Use 'transliterate' if that's the method you want; adjust if necessary
        return self.converter.transliterate(text, tidy=False)  # Adjust method if necessary

    def version(self) -> str:
        return "0.0.2"

    def is_available(self) -> bool:
        return True

# Example usage
if __name__ == "__main__":
    phonemizer = CustomPhonemizer(use_large=True)
    phoneme_text = phonemizer.phonemize('سلام چطوری')
    print(phoneme_text)
