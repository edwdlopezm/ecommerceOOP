from abc import ABC
import uuid


class Entidad(ABC):

    def __init__(self):
        self._id = uuid.uuid4()

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if not isinstance(other, Entidad):
            return NotImplemented
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"({str(self._id)[:8]})"
        )
    
    def __repr__(self):
        return self.__str__()