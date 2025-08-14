class Galleta:
    def __init__(self, nombre, precio, peso ):
            self.nombre = nombre
            self.precio = precio
            self.peso = peso
    def mostrar_informacion(self):
         return f"Nombre de la Galleta: {self.nombre}, Costo de la galleta: {self.precio}, Peso de la galleta: {self.peso}"
class Galletachispas(Galleta):
    def __init__(self, nombre,precio,peso,cantidad_chispas):
        super().__init__(nombre,precio,peso)
        self.cantidad_chispas = cantidad_chispas
    def mostrar_info(self):
        return super().mostrar_informacion() + f",Cantidad de chispas {self.cantidad_chispas}"

class Relleno:
    def __init__(self, sabor_del_relleno):
        self.sabor_del_relleno = sabor_del_relleno

    def describir_relleno(self):
        return f"El sabor del relleno: {self.sabor_del_relleno}"

class GalletaconRelleno(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", {self.describir_relleno()}"

class Registrar_galleta:
    def __init__(self):
        self.registro_galletas =[]
    def add_galleta_basica(self):
       try:
           nombre = input("Ingrese el nombre de la galleta: ").strip()
           precio = float(input("Ingrese el precio de la galleta:  "))
           peso = float(input("Ingrese el peso de la Galleta: "))
           self.registro_galletas.append(Galleta(nombre, precio, peso))
           print("Galleta basica Registrada ")
       except ValueError:
           print("Error al ingresar los datos")
    def add_galleta_chispas(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ").strip()
            precio = float(input("Ingrese el precio de la galleta:  "))
            peso = float(input("Ingrese el peso de la Galleta: "))
            cantidad_chispas = int(input("Ingrese la cantidad de chispas: "))
            self.registro_galletas.append(Galleta(nombre, precio, peso, cantidad_chispas))
            print("Galletacon chispas  Registrada ")
        except ValueError:
            print("Error al ingresar datos")
    def add_galleta_rellena(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ").strip()
            precio = float(input("Ingrese el precio de la galleta:  "))
            peso = float(input("Ingrese el peso de la Galleta: "))
            sabor = input("Ingrese el baro de la galleta: ")
            self.registro_galletas.append(GalletaconRelleno(nombre, precio, peso, sabor))
            print("Galleta con relleno Registrada ")
        except ValueError:
            print("Error al ingresar datos")
    def listar_galletas(self):
        nombre = input("Nombre a buscar: ").strip()
        encontrados = [g for g in self.registro_galletas if g.nombre.lower() == nombre.lower()]
        if encontrados:
            for g in encontrados:
                print(g.mostrar_informacion())
        else:
            print(" No encontrada.")

    def buscar_galleta(self):
        nombre = input("Nombre de la galleta a buscar: ").strip()
        encontrados = [g for g in self.registro_galletas if g.nombre.lower() == nombre.lower()]
        if encontrados:
            for g in encontrados:
                print(g.mostrar_informacion())
        else:
            print(" No encontrada.")

    def eliminar_galleta(self):
        nombre = input("Nombre de la galleta a eliminar: ").strip()
        antes = len(self.registro_galletas)
        self.registro_galletas = [g for g in self.registro_galletas if g.nombre.lower() != nombre.lower()]
        if len(self.registro_galletas) < antes:
            print(" Eliminada.")
        else:
            print(" No se encontró.")