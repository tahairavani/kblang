from .keyboard_layouts import KeyboardLayout


class UrLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._ur_layout = [
            'ط', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ہ', 'خ', 'ح', 'ج', 'د', '\\',
            'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ',
            'ظ', 'ز', 'و', 'چ', 'پ', 'ر', 'ء', '،', '.', '/', 'ۂ',
            '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', '-', '=',
        ]
        self._ur_shift_layout = [
            'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ہ', 'خ', 'ح', 'ج', 'ڈ', '|',
            'ش', 'س', 'ی', 'ب', 'ل', 'آ', 'ٹ', 'ن', 'م', 'ک', 'گ',
            'ذ', 'ژ', 'ؤ', 'چ', 'پ', 'ڑ', 'ء', '؛', ':', '؟', 'ۓ',
            '!', '@', '#', '₨', '%', '^', '&', '*', '(', ')', '_', '+',
        ]
        return [*self._ur_layout, *self._ur_shift_layout]

    @property
    def language_code(self) -> str:
        return "ur"
    