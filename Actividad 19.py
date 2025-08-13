class Galleta:
    def __init__(self, nombre, precio, peso ):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
    def mostrar_informacion(self):
         print(f"Nombre de la Galleta: {self.nombre}, Costo de la galleta: {self.precio}, Peso de la galleta: {self.peso}")