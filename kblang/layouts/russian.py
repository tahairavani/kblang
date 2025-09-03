from .keyboard_layouts import KeyboardLayout


class RuLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._ru_layout = [
            'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', '\\',
            'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
            'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', 'ё',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
        ]
        self._ru_shift_layout = [
            'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', '/',
            'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э',
            'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', ',', 'Ё',
            '!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+',
        ]
        return [*self._ru_layout, *self._ru_shift_layout]

    @property
    def language_code(self) -> str:
        return "ru"