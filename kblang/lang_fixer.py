from wordfreq import word_frequency
from .converter import ConvertLang
from .layouts.keyboard_layouts import KeyboardLayout
from .layouts.load_keyboard_layouts import load_layouts

class KeyboardLanguageFixer:
    def __init__(self, min_freq=1e-6):
        """
        :param min_freq: threshold for word validity using wordfreq
        """
        load_layouts()
        # get all available layouts dynamically
        self.available_languages = list(KeyboardLayout.get_keyboard_layouts().keys())
        self.min_freq = min_freq

    def score_text(self, text, lang):
        """
        Score a corrected text by counting valid dictionary words
        """
        words = text.split()
        return sum(1 for w in words if word_frequency(w, lang) > self.min_freq)

    def fix_text(self, text):
        """
        Try all available layouts and pick the best correction.
        """
        best_lang = None
        best_score = 0
        best_text = None

        for lang in self.available_languages:
            converted = ConvertLang(text, to_lang=lang).get_converted_text()
            score = self.score_text(converted, lang)

            if score > best_score:
                best_score = score
                best_lang = lang
                best_text = converted

        return {
            "original": text,
            "corrected": None if best_score < 1 else best_text,
            "language": None if best_score < 1 else best_lang,
            "is_gibberish": best_score < 1
        }
