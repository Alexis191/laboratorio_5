from datetime import datetime
from typing import List, Dict

class LibroDiario:
    """Gestión contable básica de ingresos y egresos."""

    def __init__(self):
        self.transacciones: List[Dict] = []

    def agregar_transaccion(self, fecha: str, descripcion: str, monto: float, tipo: str) -> None:
        """Agrega una transacción al libro diario."""
        if tipo not in ("ingreso", "egreso"):
            raise ValueError("Tipo de transacción inválido. Use 'ingreso' o 'egreso'.")

        try:
            fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'DD/MM/YYYY'.")

        transaccion = {
            "fecha": fecha_dt,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        }
        self.transacciones.append(transaccion)

    def calcular_resumen(self) -> Dict[str, float]:
        """Devuelve el resumen total de ingresos y egresos."""
        resumen = {"ingresos": 0.0, "egresos": 0.0}
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                resumen["ingresos"] += transaccion["monto"]
            else:
                resumen["egresos"] += transaccion["monto"]
        return resumen