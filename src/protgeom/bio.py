from dataclasses import dataclass
from numpy import ndarray
@dataclass(frozen=True)
class Protein:
    """ Define a protein with the inner structure
    """
    num_atoms: int
    cords: ndarray