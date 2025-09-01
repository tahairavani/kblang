from .keyboard_layouts import KeyboardLayout


class JaLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        # Basic Hiragana layout (JIS-style, simplified)
        self._ja_layout = [
            'ぬ', 'ふ', 'あ', 'う', 'え', 'お', 'や', 'ゆ', 'よ', 'わ', 'ほ', 'へ', '\\',
            'た', 'て', 'い', 'す', 'か', 'ん', 'な', 'に', 'ら', 'せ', '゛',
            'ち', 'と', 'し', 'は', 'き', 'く', 'ま', 'の', 'り', 'れ', 'け',
            'む', 'つ', 'さ', 'そ', 'ひ', 'こ', 'み', 'も', 'ね', 'る', 'め', '-', '=',
        ]

        # Shifted layout (Katakana equivalents)
        self._ja_shift_layout = [
            'ヌ', 'フ', 'ア', 'ウ', 'エ', 'オ', 'ヤ', 'ユ', 'ヨ', 'ワ', 'ホ', 'ヘ', '|',
            'タ', 'テ', 'イ', 'ス', 'カ', 'ン', 'ナ', 'ニ', 'ラ', 'セ', '゜',
            'チ', 'ト', 'シ', 'ハ', 'キ', 'ク', 'マ', 'ノ', 'リ', 'レ', 'ケ',
            'ム', 'ツ', 'サ', 'ソ', 'ヒ', 'コ', 'ミ', 'モ', 'ネ', 'ル', 'メ', '_', '+',
        ]

        return [*self._ja_layout, *self._ja_shift_layout]

    @property
    def language_code(self) -> str:
        return "ja"
