import io
import requests
import numpy as np

from protgeom.bio import Protein
from gzip import GzipFile

def fetchPDB(name):
    name_curated = name.strip().lower()
    handler = {
        200: lambda resp : parsePDBFile(io.TextIOWrapper(GzipFile('', 'r', 0, io.BytesIO(resp.content))), name_curated),
        404: lambda _ :  (_ for _ in ()).throw( RuntimeError(f'Protein ${name_curated} not found'))
    }
    resp = requests.get(f'https://ftp.wwpdb.org/pub/pdb/data/biounit/PDB/all/{name_curated}.pdb1.gz')
    if (resp.status_code in handler):
        return handler[resp.status_code](resp)
    else:
        raise RuntimeError(f'Unexpecter response from PDB: ${resp.status_code} fetching {name_curated}')


def parsePDBFile(pdb_f, name='unknown'):
    def parse_cord(line):
        #https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html
        x = float(line[31:38])
        y = float(line[39:46])
        z = float(line[47:54])
        return [x,y,z]

    cords = np.array([],dtype=float)
    for line in pdb_f:
        if line.startswith('ATOM'):
            cords = np.append(cords, parse_cord(line))

    cords_folded = cords.reshape(-1,3)
    atom_num = cords_folded.shape[0]
    return Protein(atom_num, cords_folded, name)