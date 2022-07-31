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

    def parse_calpha(line):
        atom_num = int(line[7:11]) - 1
        atom_name = line[13:16].strip()
        res_number = int(line[23:26]) - 1
        if atom_name == 'CA':
            return  (atom_num,res_number)
        return None


    cords = np.array([],dtype=float)
    calphas = []
    for line in pdb_f:
        if line.startswith('ATOM'):
            cords = np.append(cords, parse_cord(line))
            calpha = parse_calpha(line)
            if calpha:
                calphas.append(calpha)

    cords_folded = cords.reshape(-1,3)
    atom_num = cords_folded.shape[0]
    sorted_caphas = sorted(calphas,key=lambda x: x[1])
    return Protein(atom_num, cords_folded, sorted_caphas, name)