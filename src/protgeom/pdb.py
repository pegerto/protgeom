from protgeom.bio import Protein


def parsePDBFile(pdb_f):
    atom_number = 0
    for line in pdb_f:
        if line.startswith('ATOM'):
            atom_number+=1

    return Protein(atom_number)