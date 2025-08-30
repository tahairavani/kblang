from .keyboard_layouts import KeyboardLayout


class ArLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._ar_layout = [
            'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'د', '\\',
            'ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك', 'ط',
            'ئ', 'ء', 'ؤ', 'ر', 'لا', 'ى', 'ة', 'و', 'ز', 'ظ',
            'ذ', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '٠', '-', '=',
        ]
        self._ar_shift_layout = [
            'َ', 'ً', 'ُ', 'ٌ', 'لإ', 'إ', '‘', '’', '÷', '×', '؛', '<', '>',
            'ِ', 'ٍ', 'لأ', 'أ', 'ـ', '،', '/', ':', '"', '~',
            'ْ', '}', '{', 'ّ', 'لآ', 'آ', "'", ',', '.', '؟',
            '~', '!', '@', '#', '$', '%', '^', '&', '*', ')', '(', '_', '+',
        ]
        return [*self._ar_layout, *self._ar_shift_layout]

    @property
    def language_code(self) -> str:
        return "ar"