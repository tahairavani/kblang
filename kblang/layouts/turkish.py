from .keyboard_layouts import KeyboardLayout


class TrLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._tr_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p', 'ğ', 'ü',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç', '.', ',', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
        ]
        self._tr_shift_layout = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Ğ', 'Ü',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ş', 'İ',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Ö', 'Ç', ':', ';', '~',
            '!', '"', '^', '+', '%', '&', '/', '(', ')', '=', '_', '*',
        ]
        return [*self._tr_layout, *self._tr_shift_layout]

    @property
    def language_code(self) -> str:
        return "tr"