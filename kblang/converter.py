from .layouts.keyboard_layouts import KeyboardLayout
from .lang_ditact import Langueageditector
from .layouts.load_keyboard_layouts import load_layouts
from .layouts.load_keyboard_layouts import load_layouts

class ConvertLang:
    load_layouts()
    languages = KeyboardLayout.get_keyboard_layouts()

    def __init__(self, text, from_lang=None, to_lang=None):
        self.text = text
        self.from_lang = from_lang
        self.to_lang = to_lang

    def get_converted_text(self):
        result = self.text
        if self.from_lang is not None:
            self.from_lang = Langueageditector(self.text).check_languae()[0]
        for from_lang, to_lang in zip(ConvertLang.languages[self.from_lang],
                                      ConvertLang.languages[self.to_lang]):
            result = result.replace(from_lang, to_lang)
        return result

    def __str__(self):
        return self.get_converted_text()
