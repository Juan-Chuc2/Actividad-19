class Galleta:
    def __init__(self, nombre, precio, peso ):
            self.nombre = nombre
            self.precio = precio
            self.peso = peso
    def mostrar_informacion(self):
         return f"Nombre de la Galleta: {self.nombre}, Costo de la galleta: {self.precio}, Peso de la galleta: {self.peso}"


class Registrar_galleta:
    def __init__(self):
        self.registro_galletas =[]
    def add_galleta_basica(self):
       try:
           nombre = input("Ingrese el nombre de la galleta: ").strip()
           precio = float(input("Ingrese el precio de la galleta:  "))
           peso = float(input("Ingrese el peso de la Galleta: "))
           self.registro_galletas.append(Galleta(nombre, precio, peso))
       except ValueError:
           print("Error al ingresar los datos")
