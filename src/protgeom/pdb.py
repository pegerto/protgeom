import numpy as np

from protgeom.bio import Protein

def parsePDBFile(pdb_f):
    def parse_cord(line):
        #https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html
        x = float(line[31:38])
        y = float(line[39:46])
        z = float(line[47:54])
        return [x,y,z]

    atom_number = 0
    cords = np.array([],dtype=float)
    for line in pdb_f:
        if line.startswith('ATOM'):
            atom_number+=1
            cords = np.append(cords, parse_cord(line))

    return Protein(atom_number, cords.reshape(-1,3))