from .keyboard_layouts import KeyboardLayout


class SvLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._sv_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '¨', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', "'",
        ]
        self._sv_shift_layout = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Å', '^', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ';', ':', '_', '~',
            '!', '"', '#', '¤', '%', '&', '/', '(', ')', '=', '?', '*',
        ]
        return [*self._sv_layout, *self._sv_shift_layout]

    @property
    def language_code(self) -> str:
        return "sv"