from layouts.keyboard_layouts import KeyboardLayout
from layouts.persian import FaLayout
from layouts.english import EnLayout
from converter import ConvertLang

class Langueageditector:
    def __init__(self, text):
        self.text = text 
    def get_langueage(self):
        lang = KeyboardLayout.get_keyboard_layouts()
        for t in self.text:
           for key, value in lang:
              if key in lang:
                return KeyboardLayout.language_code
detector =  Langueageditector("سلام")
print(detector.get_langueage())
print(KeyboardLayout.language_code)