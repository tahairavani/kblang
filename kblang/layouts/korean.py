from .keyboard_layouts import KeyboardLayout


class KoLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._ko_layout = [
            'ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', '[', ']', '\\',
            'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', ';', "'",
            'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', ',', '.', '/',
            '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
        ]
        self._ko_shift_layout = [
            'ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅒ', 'ㅖ', '{', '}', '|',
            'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', ':', '"',
            'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', '<', '>', '?',
            '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
        ]
        return [*self._ko_layout, *self._ko_shift_layout]

    @property
    def language_code(self) -> str:
        return "ko"
