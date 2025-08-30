from .keyboard_layouts import KeyboardLayout


class EsLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._es_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '´', '¡',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ', '`', 'ç',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'", '¿'
        ]
        self._es_shift_layout = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '¨', '!',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ', '^', 'Ç',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ';', ':', '_',
            '!', '"', '·', '$', '%', '&', '/', '(', ')', '=', '?', '¿'
        ]
        return [*self._es_layout, *self._es_shift_layout]

    @property
    def language_code(self) -> str:
        return "es"