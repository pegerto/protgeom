from dataclasses import dataclass
import string
from numpy import ndarray


@dataclass(frozen=True)
class Protein:
    """ Define a protein with the inner structure
    """
    num_atoms: int
    cords: ndarray
    calphas: list
    name: string = 'unknown'

    def __str__(self):
        return self.name
    
    @property
    def calpha_cords(self) -> ndarray:
        return self.cords[[calpha[0] for calpha in self.calphas],:]