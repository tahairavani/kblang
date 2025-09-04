from .keyboard_layouts import KeyboardLayout


class KuAraLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._ku_ara_layout = [
            'ق', 'و', 'ە', 'ر', 'ت', 'ی', 'ئ', 'ح', 'ۆ', 'پ', ']', '[', '\\',
            'ا', 'س', 'د', 'ف', 'گ', 'ه', 'ژ', 'ک', 'ل', '؛', "'",
            'ز', 'خ', 'ج', 'ڤ', 'ب', 'ن', 'م', '،', '.', '/',
             '‍','١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '٠', '-', '='
        ]
        self._ku_ara_shift_layout = [
            'X', 'X', 'ه', 'ڕ', 'ط', 'ێ', 'ء', 'ع', 'ؤ', 'ث', '}', '{', '|',
            'آ', 'ش', 'ذ', 'إ', 'غ', '‌', 'أ', 'ك', 'ڵ', ':', '"',
            'ض', 'ص', 'چ', 'ظ', 'ى', 'ة', 'ـ', '>', '<', '؟',
            '÷', '!', '@', '#', '$', '%', '^', '&', '*', ')', '(', 'ـ', '+',
        ]
        return [*self._ku_ara_layout, *self._ku_ara_shift_layout]

    @property
    def language_code(self) -> str:
        return "ku_ara"
