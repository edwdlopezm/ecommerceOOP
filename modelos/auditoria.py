# modelos/auditoria.py

from datetime import datetime
from modelos.cambio import Cambio


class Auditable:

    def __init__(self):

        self._historial: list[Cambio] = []


    def registrar_cambio(self,campo: str,valor_anterior,valor_nuevo):

        cambio = Cambio(
            campo=campo,
            valor_anterior=valor_anterior,
            valor_nuevo=valor_nuevo,
            fecha=datetime.now()
        )

        self._historial.append(cambio)


    @property
    def historial(self):

        return self._historial.copy()


    def mostrar_historial(self):

        for cambio in self._historial:

            print(
                f"{cambio.fecha:%d/%m/%Y %H:%M:%S} | "
                f"{cambio.campo}: "
                f"{cambio.valor_anterior} → "
                f"{cambio.valor_nuevo}"
            )