# number_conversion/conversion_base.py

from abc import ABC, abstractmethod

class ConversionBase(ABC):
    """
    Abstract class for number conversion operations.
    """

    @abstractmethod
    def convert(self, value):
        pass
