from layouts.keyboard_layouts import KeyboardLayout
from layouts.persian import FaLayout
from layouts.english import EnLayout
from converter import ConvertLang

class Langueageditector:
    def __init__(self, text):
        self.text  = text
    def get_languages(self):
        scores = {}
        total_charts = 0

        for ch in self.text.lower():
            for lang, alphabet in KeyboardLayout.get_keyboard_layouts().items():
                if ch in alphabet:
                    scores[lang] = scores.get(lang, 0) + 1
                    total_charts += 1

    #mohasebe darsad
        percentages = {}
        for lang, count in scores.items():
            percentages[lang] = round((count / total_charts) * 100, 2) if total_charts > 0 else 0 

        #peyda kardan zaban asli
        best_lang = max(percentages, key=percentages.get) if percentages else None
        return best_lang, percentages  
           

detect = Langueageditector("hello سلام")
print(detect.get_languages())