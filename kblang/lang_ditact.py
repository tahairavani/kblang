from .layouts.keyboard_layouts import KeyboardLayout


class Langueageditector:
    def __init__(self, text):
        self.text = text
        self.languages = KeyboardLayout.get_keyboard_layouts().items()

    def check_languae(self):
        scores = {}
        total_charts = 0
        for ch in self.text.lower():
            for lang, alphabet in self.languages:
                if ch in alphabet:
                    scores[lang] = scores.get(lang, 0) + 1
                    total_charts += 1

        # mohasebe darsad
        percentages = {}
        for lang, count in scores.items():
            percentages[lang] = round(
                (count / total_charts) * 100, 2) if total_charts > 0 else 0

        # peyda kardan zaban asli
        best_lang = max(
            percentages, key=percentages.get) if percentages else None
        return best_lang, percentages

    def get_language(self):
        self.check_languae()[0]

    def get_languages_score(self):
        self.check_languae()[1]

    def __str__(self):
        self.check_languae()