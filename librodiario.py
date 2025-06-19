from datetime import datetime
from typing import List, Dict
import logging
import traceback

#Configuración de logging
logging.basicConfig(
    filename='log_contable.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MontoInvalidoError(Exception):
    """Excepción lanzada cuando el monto es cero o negativo."""
    pass

class LibroDiario:
    """Gestión contable básica de ingresos y egresos."""

    def __init__(self):
        self.transacciones: List[Dict] = []

    def agregar_transaccion(self, fecha: str, descripcion: str, monto: float, tipo: str) -> None:
        """Agrega una transacción con manejo de errores."""

        try:
            #Controla si el tipo es ingreso o egreso.
            if tipo.lower() not in ("ingreso", "egreso"):
                raise ValueError("Tipo de transaccion invalido, debe poner 'ingreso' o 'egreso'.")

            #Controla si el formato correcto de fecha año-mes-día (2025-06-19).
            try:
                fecha_dt = datetime.strptime(fecha, "%Y-%m-%d") 
            except ValueError:
                raise ValueError("Formato de fecha invalido, debe usar el formato: yyyy-mm-dd.")

            #Controla si el monto el mayor o menos a 0.
            if monto <= 0:
                raise MontoInvalidoError("El monto debe ser mayor a cero.")

            #Registra la transacción.
            transaccion = {
                "fecha": fecha_dt,
                "descripcion": descripcion,
                "monto": monto,
                "tipo": tipo.lower()
            }
            self.transacciones.append(transaccion)

            #Registrar transacción exitosa
            logging.info(f"Transaccion registrada: {fecha} | {descripcion} | {monto} | {tipo}")

        except (ValueError, MontoInvalidoError) as e:
            error_line = traceback.format_exc().strip().splitlines()[-1]
            logging.error(f"{e} - Linea: {error_line}")
            print(f"[ERROR] {e}")

    def calcular_resumen(self) -> Dict[str, float]:
        """Devuelve el resumen total de ingresos y egresos."""
        resumen = {"ingresos": 0.0, "egresos": 0.0}
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                resumen["ingresos"] += transaccion["monto"]
            else:
                resumen["egresos"] += transaccion["monto"]
        return resumen
