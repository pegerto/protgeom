from abc import abstractclassmethod
import numpy as np
from scipy import spatial

class ProteinRepresentation:
    """ 
    A interface for a protein 3D representation
    Attributes:
        matrix -> ndarray 
            A transformation of the 3D structure to a 2D structure.

    """
    @abstractclassmethod
    def matrix(self) -> np.ndarray:
        pass


class ContactMap(ProteinRepresentation):
    """
    A class representing a representation of a protein.

    Contact map represent the distance between all the possible residue pairs
    and stablish a cutoff distance in Å.
    """

    def __init__(self, protein, cutoff) -> None:
        """
        Constructs a contact map from the 

        Parameters
        ----------
            protein : bio.Protein
                A Protein represention
            cutoff : double
               distance consiser as a threashold for 2 residue pair are worth to be represented.

        """
        dist = spatial.distance.pdist(protein.calpha_cords)
        contact = spatial.distance.squareform(dist)
        contact[contact > cutoff] = np.nan
        self.data = contact 
    
    @property
    def matrix(self) -> np.ndarray:
        return self.data