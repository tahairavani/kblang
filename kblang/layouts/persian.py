from .keyboard_layouts import KeyboardLayout


class FaLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self.fa_layout = [
            'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', "\\",
            'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ',
            'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و', 'ژ', 'ء',
            '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', '-', '='
        ]
        self.fa_shift_layout = [
            'ْ', 'ٌ', 'ٍ', 'ً', 'ُ', 'ِ', 'َ', 'ّ', ']', '[', '}', '{',
            'ؤ', 'ئ', 'إ', 'أ', 'آ', 'ة', '»', '«', '؛', ':', '"',
            'ـ', 'ٓ', 'ٰ', 'ٔ', 'ٕ', 'ٔ', 'ٓ', 'ٰ', 'ٖ', 'ٗ',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'
        ]
        return [*self.fa_layout, *self.fa_shift_layout]

    @property
    def language_code(self) -> str:
        return "fa"
