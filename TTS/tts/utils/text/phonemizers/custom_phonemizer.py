# File: custom_phonemizer.py

from PersianG2p import Persian_g2p_converter

class CustomPhonemizer:
    def __init__(self, use_large=False):
        # Initialize an instance of Persian_g2p_converter
        self.converter = Persian_g2p_converter(use_large=use_large)
    
    def phonemize(self, text):
        # Call the appropriate method from Persian_g2p_converter to perform phonemization
        # Use 'transliterate' if that's the method you want; adjust if necessary
        return self.converter.transliterate(text, tidy=False)  # Adjust method if necessary

# Example usage
if __name__ == "__main__":
    phonemizer = CustomPhonemizer(use_large=True)
    phoneme_text = phonemizer.phonemize('سلام چطوری')
    print(phoneme_text)
