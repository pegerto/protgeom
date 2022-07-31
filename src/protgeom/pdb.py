import numpy as np

from protgeom.bio import Protein

def parsePDBFile(pdb_f):
    def parse_cord(line):
        pass

    atom_number = 0
    cords = np.ndarray(shape=(3,), dtype=float)
    for line in pdb_f:
        if line.startswith('ATOM'):
            atom_number+=1

    return Protein(atom_number, cords)