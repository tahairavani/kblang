from .keyboard_layouts import KeyboardLayout


class ElLayout(KeyboardLayout):
    @property
    def mapping(self) -> list:
        self._el_layout = [
            ';', 'ς', 'ε', 'ρ', 'τ', 'υ', 'θ', 'ι', 'ο', 'π', '[', ']', '\\',
            'α', 'σ', 'δ', 'φ', 'γ', 'η', 'ξ', 'κ', 'λ', '΄', "'",
            'ζ', 'χ', 'ψ', 'ω', 'β', 'ν', 'μ', ',', '.', '-', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
        ]
        self._el_shift_layout = [
            ':', 'Σ', 'Ε', 'Ρ', 'Τ', 'Υ', 'Θ', 'Ι', 'Ο', 'Π', '{', '}', '|',
            'Α', 'Σ', 'Δ', 'Φ', 'Γ', 'Η', 'Ξ', 'Κ', 'Λ', '¨', '"',
            'Ζ', 'Χ', 'Ψ', 'Ω', 'Β', 'Ν', 'Μ', '<', '>', '_', '~',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
        ]
        return [*self._el_layout, *self._el_shift_layout]

    @property
    def language_code(self) -> str:
        return "el"