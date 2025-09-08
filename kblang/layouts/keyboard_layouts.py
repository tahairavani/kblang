from abc import ABC, abstractmethod


class KeyboardLayout(ABC):
    @property
    @abstractmethod
    def mapping(self) -> list:
        """return a dictionary mapping characters to their equivalents"""
        pass

    @property
    @abstractmethod
    def language_code(self) -> str:
        """return a language code example -> english = en OR persian = fa """
        pass

    @classmethod
    def _all_keyboard_layouts(cls):
        layouts = dict()
        for subclass in cls.__subclasses__():
            layouts[subclass().language_code] = subclass().mapping
        return layouts

    @classmethod
    def get_keyboard_layouts(cls, layout=None):
        if layout is not None:
            return cls._all_keyboard_layouts()[layout]
        else:
            return cls._all_keyboard_layouts()
