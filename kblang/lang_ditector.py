from wordfreq import word_frequency
from .layouts.keyboard_layouts import KeyboardLayout
from .layouts import load_keyboard_layouts
from .converter import ConvertLang

class LanguageDetector:
    """LanguageDetector"""
    def __init__ (self,min_freq=1e-6):
        self.min_freq = min_freq
        load_keyboard_layouts.load_layouts()
        self.available_languages = KeyboardLayout.get_keyboard_layouts()

    def check_text_score(self,text,language):
        """
        Score a corrected text by counting valid dictionary words
        """
        words = text.split()
        return sum(1 for w in words if word_frequency(w, language)> self.min_freq)

    def get_recommended_language(self,text):
        """
        Try all available layouts and pick the best correction.
        """
        best_lang = None
        best_score = 0

        for lang in self.available_languages:
            converted = ConvertLang(text, to_lang=lang).get_converted_text(text=text)
            score = self.check_text_score(converted, lang)

            if score > best_score:
                best_score = score
                best_lang = lang

        return {
            "original": text,
            "language": None if best_score < 1 else best_lang,
            "is_gibberish": best_score < 1
        }

    def get_current_language(self,text):
        scores = {}
        total_charts = 0
        for ch in text.lower():
            for lang, alphabet in self.available_languages.items():
                if ch in alphabet:
                    scores[lang] = scores.get(lang, 0) + 1
                    total_charts += 1

        percentages = {}
        for lang, count in scores.items():
            percentages[lang] = round(
                (count / total_charts) * 100, 2) if total_charts > 0 else 0

        best_lang = max(percentages, key=lambda x: percentages[x])
        return best_lang, percentages

    def check_language(self,text):
        current_language = self.get_current_language(text)
        recommended_language = self.get_recommended_language(text)
        return {
            "original": text,
            "current_language": current_language,
            "recommended_language": recommended_language,
            "is_gibberish": recommended_language["is_gibberish"]
        }
