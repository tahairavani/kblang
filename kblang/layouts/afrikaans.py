from .keyboard_layouts import KeyboardLayout


class AfLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._af_layout = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
            'é', 'è', 'ê', 'ë', 'ï', 'î', 'ô', 'ö', 'û', 'ü', 'ç'
        ]
        self._af_shift_layout = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', '~',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
            'É', 'È', 'Ê', 'Ë', 'Ï', 'Î', 'Ô', 'Ö', 'Û', 'Ü', 'Ç'
        ]
        return [*self._af_layout, *self._af_shift_layout]

    @property
    def language_code(self) -> str:
        return "af"