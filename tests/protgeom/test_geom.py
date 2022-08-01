import math
from protgeom.geom import contact_map

import numpy as np

def calpha_cords():
    return np.array([
        [1,1,1],
        [2,2,2]
    ])

def test_contact_map_symetric():
    cmap = contact_map(calpha_cords(), 5)
    assert cmap[0][1] == cmap[1][0]


def test_contact_map_euclidean_distance():
    cmap = contact_map(calpha_cords(), 5)
    dist = np.subtract(calpha_cords()[0], calpha_cords()[1])
    assert cmap[0][1] == math.sqrt(np.dot(dist, dist.T))


def test_contact_map_cutoff():
    cmap = contact_map(calpha_cords(), 1.7)
    assert np.isnan(cmap[0][1])
    cmap = contact_map(calpha_cords(), 1.8)
    assert not np.isnan(cmap[0][1])