import math
from protgeom.bio import Protein
from protgeom.geom import ContactMap

import numpy as np

def protein():
    return Protein(2, np.array([
        [1,1,1],
        [2,2,2]
    ]), [(0,1),(1,2)])


def test_contact_map_symetric():
    cmap = ContactMap(protein(), 2)
    assert cmap.matrix[0][1] == cmap.matrix[1][0]


def test_contact_map_euclidean_distance():
    cmap = ContactMap(protein(), 5)
    dist = np.subtract(protein().calpha_cords[1], protein().calpha_cords[0])
    print(dist)
    assert cmap.matrix[0][1] == math.sqrt(np.dot(dist, dist.T))


def test_contact_map_cutoff():
    cmap = ContactMap(protein(), 0.5)
    assert np.isnan(cmap.matrix[0][1])
    cmap = ContactMap(protein(), 1.8)
    assert not np.isnan(cmap.matrix[0][1])