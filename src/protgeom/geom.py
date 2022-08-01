import numpy as np
from scipy import spatial

def contact_map(calphas, cutoff):
    dist = spatial.distance.pdist(calphas)
    contact = spatial.distance.squareform(dist)
    contact[contact > cutoff] = np.nan
    return contact 