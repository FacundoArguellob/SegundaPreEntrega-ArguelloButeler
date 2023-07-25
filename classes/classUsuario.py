import database.manageDB as database
from grafico.menus import *

class Usuario:
    def __init__(self, id, nombre, edad, email, password, direccion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.password = password
        self.direccion = direccion
    

    def __str__(self):
        return (f"ID: {self.id}, NOMBRE: {self.nombre}, EMAIL: {self.email}")

      
    def login(self):
        self.acciones()  


    def registro(self):
        database.guardar_usuario(self.__dict__)


    def comprar(self):
        db_productos = database.peticion_productos()
        mostrar_productos(db_productos)
        while True:
            try:
                eleccion = int(input("elige el id del producto que quieres comprar (0 para salir): "))
                if eleccion == 0: break
                if eleccion > len(db_productos):
                    print("numero fuera de rango")
                else:
                    for producto in db_productos:
                        if producto["id"] == eleccion:
                            print(f"Gracias {self.nombre} Compraste: {producto['nombre']}")

            except ValueError:
                print("escribe un numero por favor")


    def acciones(self):
        while True:
            menu_usuario()
            try:
                eleccion = int(input())
                match eleccion:
                    case 1:
                        self.comprar()
                    case 2:
                        informacion = self.__str__()
                        print(informacion)
                    case 3:
                        break
                    case _:
                        print("numero fuera de rango")
            except ValueError:
                print("escribe un numero por favor")