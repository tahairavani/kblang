from .keyboard_layouts import KeyboardLayout


class FrLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._fr_layout = [
            'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '^', '$', '\\',
            'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'ù',
            'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':', '!', '²',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '°', '+',
        ]
        self._fr_shift_layout = [
            'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '¨', '£', '|',
            'Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', '%',
            'W', 'X', 'C', 'V', 'B', 'N', '?', '.', '/', '§', '',
            '&', 'é', '"', "'", '(', '-', 'è', '_', 'ç', 'à', ')', '=',
        ]
        return [*self._fr_layout, *self._fr_shift_layout]

    @property
    def language_code(self) -> str:
        return "fr"