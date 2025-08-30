from .keyboard_layouts import KeyboardLayout


class ItLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._it_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'è', '+', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ò', 'à', 'ù',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'", 'ì'
        ]
        self._it_shift_layout = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'é', '*', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ç', '°', '§',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ';', ':', '_',
            '!', '"', '£', '$', '%', '&', '/', '(', ')', '=', '?', '^'
        ]
        return [*self._it_layout, *self._it_shift_layout]

    @property
    def language_code(self) -> str:
        return "it"