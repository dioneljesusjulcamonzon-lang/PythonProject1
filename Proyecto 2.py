

# CORRECTO: Usamos clases. Para un nuevo cliente, creamos una clase nueva sin tocar las anteriores
class Descuento:
    def aplicar(self, precio):
        return precio

class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8

class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9
