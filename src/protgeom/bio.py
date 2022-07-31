from dataclasses import dataclass
import string
from unicodedata import name
from numpy import ndarray


@dataclass(frozen=True)
class Protein:
    """ Define a protein with the inner structure
    """
    num_atoms: int
    cords: ndarray
    name: string = 'unknown'

    def __str__(self):
        return name