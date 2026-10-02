

# CORRECTO: Separamos la estructura del reporte de la lógica de guardado
class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

class GuardadorReporte:
    def guardar(self, reporte: Reporte, ruta: str):
        with open(ruta, "w") as f:
            f.write(reporte.contenido)
