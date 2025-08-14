class Galleta:
    def __init__(self, nombre, precio, peso ):
            self.nombre = nombre
            self.precio = precio
            self.peso = peso
    def mostrar_informacion(self):
         print(f"Nombre de la Galleta: {self.nombre}, Costo de la galleta: {self.precio}, Peso de la galleta: {self.peso}")


class Registrar_galleta:
    def __init__(self):
        self.registro_galletas =[]
    def add_galleta_basica(self):
        while True:
            try:
                nombre = input("Ingrese el nombre de la galleta")
                if not nombre:
                    print("El nombre no puede quedar vacío")
                else:
                    break
            except ValueError:
                print("No puede quedar vacio el nombre")

        while True:
            try:
                precio = float(input("Ingrese el precio: "))
                if precio <= 0:
                    print(" El precio debe ser mayor que 0.")
                else:
                    break
            except ValueError:
                print(" Debe ingresar un número válido para el precio.")

        while True:
            try:
                peso = float(input("Ingrese el peso en gramos: "))
                if peso <= 0:
                    print(" El peso debe ser mayor que 0.")
                else:
                    break
            except ValueError:
                print(" Debe ingresar un número válido para el peso.")
