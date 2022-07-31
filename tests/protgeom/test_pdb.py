
import io
import pytest
from protgeom.bio import Protein
from protgeom.pdb import parsePDBFile

def example_pdb_file():
    return io.StringIO("""
ATOM      1  N   ILE A  16      -8.155   9.648  20.365  1.00 10.68           N
ATOM      2  CA  ILE A  16      -8.150   8.766  19.179  1.00 10.68           C
ATOM      3  C   ILE A  16      -9.405   9.018  18.348  1.00 10.68           C
ATOM      4  O   ILE A  16     -10.533   8.888  18.870  1.00 10.68           O
ATOM      5  CB  ILE A  16      -8.091   7.261  19.602  1.00 10.68           C
ATOM      6  CG1 ILE A  16      -6.898   6.882  20.508  1.00  7.42           C
ATOM      7  CG2 ILE A  16      -8.178   6.281  18.408  1.00  7.42           C
ATOM      8  CD1 ILE A  16      -5.555   6.893  19.773  1.00  7.42           C
ATOM      9  N   VAL A  17      -9.224   9.305  17.090  1.00  9.63           N
ATOM     10  CA  VAL A  17     -10.351   9.448  16.157  1.00  9.63           C
ATOM     11  C   VAL A  17     -10.500   8.184  15.315  1.00  9.63           C
ATOM     12  O   VAL A  17      -9.496   7.688  14.748  1.00  9.63           O
ATOM     13  CB  VAL A  17     -10.123  10.665  15.222  1.00  9.63           C
ATOM     14  CG1 VAL A  17     -11.319  10.915  14.278  1.00 11.95           C
ATOM     15  CG2 VAL A  17      -9.737  11.970  15.970  1.00 11.95           C
ATOM     16  N   GLY A  18     -11.714   7.720  15.167  1.00 15.04           N
ATOM     17  CA  GLY A  18     -12.021   6.630  14.259  1.00 15.04           C    
    """)

def test_pdb_read():
    assert parsePDBFile(example_pdb_file()) == Protein(17)