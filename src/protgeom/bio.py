from dataclasses import dataclass

@dataclass(frozen=True)
class Protein:
    """ Define a protein with the inner structure
    """
    name: str