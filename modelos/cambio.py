from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Cambio:
    campo: str
    valor_anterior: Any
    valor_nuevo: Any
    fecha: datetime