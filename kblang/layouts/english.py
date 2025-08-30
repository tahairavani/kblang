from .keyboard_layouts import KeyboardLayout


class EnLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._en_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
        ]
        self._en_shift_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',
            '`', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '0', '-', '=',
        ]
        return [*self._en_layout, *self._en_shift_layout]

    @property
    def language_code(self) -> str:
        return "en"
