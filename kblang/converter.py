from layouts import persian,english

class ConvertLang:
    languages = {"en" : english.EnLayout().mapping,
                 "fa" : persian.FaLayout().mapping
                 }
    def __init__(self, text, from_lang = None , to_lang = None):
        self.text = text
        self.from_lang = from_lang
        self.to_lang = to_lang

    
    def get_converted_text(self):
        result = self.text
        for from_lang,to_lang in zip(ConvertLang.languages[self.from_lang],ConvertLang.languages[self.to_lang]):
            result = result.replace(from_lang,to_lang)
        return result
        
    def __str__(self):
        return self.get_converted_text()
