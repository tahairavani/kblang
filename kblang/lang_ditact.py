from layouts.keyboard_layouts import KeyboardLayout
from layouts.persian import FaLayout
from layouts.english import EnLayout

class Langueageditector:
    langueages = KeyboardLayout.get_keyboard_layouts()
    def __init__(self, text):
        self.text = text 
    def get_langueage(self):
        return(self.text)
print(Langueageditector("hello").get_langueage())
