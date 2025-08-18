from abc import ABC, abstractmethod

class KeyboardLayout(ABC):
    @property
    @abstractmethod
    def mapping(self) -> list:
        """return a dictionary mapping characters to their equivalents"""
        pass
