from .keyboard_layouts import KeyboardLayout


class HiLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._hi_layout = [
            'ौ', 'ै', 'ा', 'ी', 'ू', 'ब', 'ह', 'ग', 'द', 'ज', 'ड', '़', '\\',
            'ो', 'े', '्', 'ि', 'ु', 'प', 'र', 'क', 'त', 'च', 'ट',
            'ं', 'म', 'न', 'व', 'ल', 'स', ',', '.', '/', 'ञ', 'ॆ',
            '१', '२', '३', '४', '५', '६', '७', '८', '९', '०', '-', '=',
        ]
        self._hi_shift_layout = [
            'औ', 'ऐ', 'आ', 'ई', 'ऊ', 'भ', 'ङ', 'घ', 'ध', 'झ', 'ढ', 'ञ', '|',
            'ओ', 'ए', 'अ', 'इ', 'उ', 'फ', 'ऱ', 'ख', 'थ', 'छ', 'ठ',
            'ँ', 'ण', 'श', 'ष', 'ळ', 'श्र', ';', ':', '?', 'ॐ', 'ऎ',
            '!', '@', '#', '₹', '%', '^', '&', '*', '(', ')', '_', '+',
        ]
        return [*self._hi_layout, *self._hi_shift_layout]

    @property
    def language_code(self) -> str:
        return "hi"