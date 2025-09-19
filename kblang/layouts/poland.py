from .keyboard_layouts import KeyboardLayout


class PlLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._pl_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ż', 'ź', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ł', 'ń',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=', "'",
        ]
        self._pl_shift_layout = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Ż', 'Ź', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ł', 'Ń',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ';', ':', '_', '~',
            '!', '@', '#', '¤', '%', '^', '&', '*', '(', ')', '+', '"',
        ]
        return [*self._pl_layout, *self._pl_shift_layout]

    @property
    def language_code(self) -> str:
        return "pl"