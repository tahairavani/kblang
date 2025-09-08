from .layouts.keyboard_layouts import KeyboardLayout
from .lang_ditector import LanguageDetector
from .layouts.load_keyboard_layouts import load_layouts

class ConvertLang:
    load_layouts()

    def __init__(self, text,from_lang=None, to_lang=None):
        if from_lang is not None:
            self.from_lang = from_lang
        elif from_lang is None:
            self.from_lang = LanguageDetector().get_current_language(text)[0]
        self.to_lang = to_lang
        self.available_languages = KeyboardLayout.get_keyboard_layouts()
        self.text = text
    def get_converted_text(self, text):
        result = text
        for from_lang, to_lang in zip(self.available_languages[self.from_lang],
                                      self.available_languages[self.to_lang]):
            result = result.replace(from_lang, to_lang)
        return result
