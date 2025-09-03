from kblang import kbfix
from wordfreq import word_frequency

class KeyboardLanguageFixer:
    def __init__(self, candidates=None, min_freq=1e-6):
        """
        :param candidates: list of language codes to check (default: ['fa', 'ar', 'ru'])
        :param min_freq: threshold for word validity using wordfreq
        """
        self.candidates = candidates or ["fa", "ar", "ru"]
        self.min_freq = min_freq

    def score_text(self, text, lang):
        """
        Score a corrected text by counting valid dictionary words
        """
        words = text.split()
        score = 0
        for w in words:
            if word_frequency(w, lang) > self.min_freq:
                score += 1
        return score

    def fix_text(self, text):
        """
        It will try all languages and pick the best correction.
        
        To use in client code follow below way:-

        fixer = KeyboardLanguageFixer()
        print(fixer.fix_text("sghl ]x,vd lk o,fl"))

        Output:
         {
           "original": "sghl ]x,vd lk o,fl",
           "corrected": "سلام خوبم چطوری",
           "language": "fa",
           "is_gibberish": False
         }
        """
        best_lang = None
        best_score = 0
        best_text = None

        for lang in self.candidates:
            corrected = kbfix(text, lang)
            score = self.score_text(corrected, lang)

            if score > best_score:
                best_score = score
                best_lang = lang
                best_text = corrected

        return {
            "original": text,
            "corrected": None if best_score < 1 else best_text,
            "language": None if best_score < 1 else best_lang,
            "is_gibberish": best_score < 1
        }
