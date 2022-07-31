#  ProtGeom: Protein Geometric 

Python package for geometrical learning on protein structures.

## Install

To install this library please use 

```
pip install -i https://test.pypi.org/simple/ protgeom -U
```

## Examples


Fetch protein structure
```python
mol_7q0b = fetchPDB('7Q0B')
```

Look at the number of atoms.
```python
mol_7q0b.num_atoms
```

21148

Read the atom cordinates in a 3D cartesian plane with unit defined in Å 

```python
mol_7q0b.cords
```
    array([[193.53 , 206.683, 173.089],
           [193.285, 208.002, 173.678],
           [194.431, 208.461, 174.578],
           ...,
           [210.995, 129.905, 137.104],
           [210.455, 128.536, 137.509],
           [209.865, 130.913, 136.954]])


We can work with cordinates:
 


```python
%matplotlib inline

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
```


```python
fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
ax = plt.axes(projection='3d')
ax.scatter3D(mol_7q0b.cords[:,0], mol_7q0b.cords[:,1], mol_7q0b.cords[:,2])
```

    
![png](doc/img/scatter3D.png)
    


## Release Processs 

Release process is not currently automated, I will enable a github action workflow as soon the project get some additional commiters.

```
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```
