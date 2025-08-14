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
    def mostrar_informacion(self):
        informacion_galleta = super().mostrar_informacion()
        return  f"{informacion_galleta}Cantidad de chispas {self.cantidad_chispas}"

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
class RegistroDuplicado(Exception):
    pass


class Registrar_galleta:
    def __init__(self):
        self.registro_galletas =[]

    def namesrepetidos(self, nombre):
        for i in self.registro_galletas:
            if i.nombre.lower() == nombre.lower():
               return True
        return False


    def add_galleta_basica(self):
       try:
           nombre = input("Ingrese el nombre de la galleta: ").strip()
           if self.namesrepetidos(nombre):
               raise RegistroDuplicado("Este nombre ya fue usado, vuelva a intentar")
           if not nombre:
               print("El nombre no puede quedar vacio")
               return
           precio = float(input("Ingrese el precio de la galleta:  "))
           peso = float(input("Ingrese el peso de la Galleta: "))
           if peso <0 or precio <0:
               raise ValueError("EL valor es invalido, intente de nuevo")
           self.registro_galletas.append(Galleta(nombre, precio, peso))
           print("Galleta basica Registrada ")
       except ValueError:
           print("El valor es invalido, intente de nuevo")
       except RegistroDuplicado as e:
           print(e)
       except Exception as e:
           print("Se produjo un error")
    def add_galleta_chispas(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ").strip()
            if self.namesrepetidos(nombre):
                raise RegistroDuplicado("Este nombre ya fue usado, vuelva a intentar")
            if not nombre:
                print("El nombre no puede quedar vacio")
                return
            precio = float(input("Ingrese el precio de la galleta:  "))
            peso = float(input("Ingrese el peso de la Galleta: "))
            cantidad_chispas = int(input("Ingrese la cantidad de chispas: "))
            if peso < 0 or precio < 0 or cantidad_chispas<0:
                raise ValueError("EL valor es invalido, intente de nuevo")
            self.registro_galletas.append(Galletachispas(nombre, precio, peso, cantidad_chispas))
            print("Galletacon chispas  Registrada ")
        except ValueError:
            print("EL valor es invalido, intente de nuevo")
        except RegistroDuplicado as e:
            print(e)
        except Exception as e:
            print("Se produjo un error")
    def add_galleta_rellena(self):
        try:
            nombre = input("Ingrese el nombre de la galleta: ").strip()
            if not nombre:
                print("El nombre no puede quedar vacio")
                return
            precio = float(input("Ingrese el precio de la galleta:  "))
            peso = float(input("Ingrese el peso de la Galleta: "))
            sabor = input("Ingrese el sabor de la galleta: ")
            if peso < 0 or precio < 0:
                raise ValueError("EL valor es invalido, intente de nuevo")
            self.registro_galletas.append(GalletaconRelleno(nombre, precio, peso, sabor))
            print("Galleta con relleno Registrada ")
        except ValueError:
            print("El valor es invalido, intente de nuevo")
        except RegistroDuplicado as e:
            print(e)
        except Exception as e:
            print("Se produjo un error")
    def listar_galletas(self):
        if not self.registro_galletas:
            print("No hay galletas registradas.")
        else:
            for g, k  in enumerate (self.registro_galletas):
                print(k.mostrar_informacion())

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

gestor = Registrar_galleta()
while True:
    print("\n--- MENÚ ---")
    print("1. Registrar galleta básica")
    print("2. Registrar galleta con chispas")
    print("3. Registrar galleta rellena")
    print("4. Listar galletas")
    print("5. Buscar por nombre")
    print("6. Eliminar por nombre")
    print("7. Salir")

    option = input("Ingrese una opcion: ")
    match option:
        case "1":
            gestor.add_galleta_basica()
        case "2":
            gestor.add_galleta_chispas()
        case "3":
            gestor.add_galleta_rellena()
        case "4":
            gestor.listar_galletas()
        case "5":
            gestor.buscar_galleta()
        case "6":
            gestor.eliminar_galleta()
        case "7":
            print("Se esta sdasliendo del programas... gracias por usarlo")
            break
        case _:
            print("Erro ingrese un caracter valido")