from dataclasses import dataclass
import string
from numpy import ndarray

from protgeom.geom import contact_map


@dataclass(frozen=True)
class Protein:
    """ Define a protein as a biological molecule
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

    def contact(self, cutoff):
        contact_map(self.calphas, cutoff)