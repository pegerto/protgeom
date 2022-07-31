
import io
import pytest
from protgeom.bio import Protein
from protgeom.pdb import parsePDBFile

@pytest.fixture
def example_pdb_file():
    return io.StringIO("""
    
    """)

def test_pdb_read():
    assert parsePDBFile(example_pdb_file) == Protein("abc")