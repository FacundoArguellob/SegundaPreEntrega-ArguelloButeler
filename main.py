from database.manageDB import *
from classes.classUsuario import Usuario
from grafico.menus import *
from random import randint

def test():
    usuarios_test = [
    {
        "nombre": "Juan Perez",
        "edad": 30,
        "email": "juan@example.com",
        "password": "contrasena123",
        "direccion": "Calle 123, Ciudad"
    },
    {
        "nombre": "Maria Lopez",
        "edad": 25,
        "email": "maria@example.com",
        "password": "password456",
        "direccion": "Avenida 456, Pueblo"
    },
    {
        "nombre": "Carlos Gomez",
        "edad": 35,
        "email": "carlos@example.com",
        "password": "clave789",
        "direccion": "Plaza 789, Villa"
    },
    {
        "nombre": "Ana Torres",
        "edad": 28,
        "email": "ana@example.com",
        "password": "secreto987",
        "direccion": "Carrera 987, Ciudad"
    },
    {
        "nombre": "Luis Ramirez",
        "edad": 40,
        "email": "luis@example.com",
        "password": "micontra",
        "direccion": "Calle 555, Ciudad"
    },
    {
        "nombre": "Elena Martinez",
        "edad": 22,
        "email": "elena@example.com",
        "password": "miclave",
        "direccion": "Avenida 222, Pueblo"
    },
    {
        "nombre": "Pedro Sanchez",
        "edad": 31,
        "email": "pedro@example.com",
        "password": "123456",
        "direccion": "Plaza 111, Villa"
    },
    {
        "nombre": "Laura Rodriguez",
        "edad": 29,
        "email": "laura@example.com",
        "password": "abcdef",
        "direccion": "Carrera 999, Ciudad"
    },
    {
        "nombre": "Miguel Flores",
        "edad": 27,
        "email": "miguel@example.com",
        "password": "qwerty",
        "direccion": "Avenida 777, Pueblo"
    },
    {
        "nombre": "Sofia Vargas",
        "edad": 33,
        "email": "sofia@example.com",
        "password": "abc123",
        "direccion": "Plaza 222, Villa"
    }
]


    user = usuarios_test[randint(0, len())]
    nombre = user["nombre"]
    edad = user["edad"]
    email = user["email"]
    password = user["password"]
    direccion = user["direccion"]
    return nombre, edad, email, password, direccion
def registro():
    nombre = (input("Nombre: "))
    edad = (input("Edad: "))
    email = (input("Email: "))
    password = (input("Password: "))
    direccion = (input("Direccion: "))
    #nombre, edad, email, password, direccion = test()
    nuevo_usuario = Usuario(get_id(), nombre, edad, email, password, direccion)
    nuevo_usuario.registro()


def login():
    email = input("Email: ")
    password = input("Password: ")
    db_usuarios = peticion_usuario()
    flag = True
    for usuario in db_usuarios:
        if email == usuario["email"] and password == usuario["password"]:
            print(f"login exitoso, Bienvenido {usuario['nombre']}")
            flag = False
            break
    if flag:
        print("las credenciales son incorrectas o el usuario no existe")
    else:
        login_usuario = Usuario(usuario["id"], usuario["nombre"], usuario["edad"], email, password, usuario["direccion"])
        login_usuario.login() 
    

def menu():
    while True:
        menu_inicio()
        try:
            eleccion = int(input())
            match eleccion:
                case 1:
                    login()
                case 2:
                    registro()
                case 3:
                    break
                case _:
                    print("numero fuera de rango")
        except ValueError:
            print("escribe un numero por favor")


def main():
    inicio_db()
    menu()
main()