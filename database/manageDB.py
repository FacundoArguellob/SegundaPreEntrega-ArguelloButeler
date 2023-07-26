import json
import os
from database.productos import *
path = os.path.abspath(os.path.dirname(__file__))
first_id = {"current_id" : 0}
file_name = "\DB.json"
current_id = 0
db = {}


def get_id():
    return current_id


def estructura_db():
    with open(path + file_name, "w") as file:
        pass
    if "current_id" not in db:
        db["current_id"] = current_id
    if "usuarios" not in db:
        db["usuarios"] = []
    if "productos" not in db:
        db["productos"] = []

    if len(db["productos"]) == 0: db["productos"] = productosDicc()
    with open(path + file_name, "w") as file:
        json.dump(db, file, indent=4)

def inicio_db():
    global db
    global current_id
    try:
        with open(path + file_name) as file:
            db = json.load(file)
            current_id = db.get("current_id", 0)
        estructura_db()   
    except FileNotFoundError:
        estructura_db()
    

def guardar_usuario(nuevo_usuario):
    global current_id
    try:
        db['current_id'] = current_id
        db['usuarios'].append(nuevo_usuario)
        with open(path + file_name, "w") as file:
            json.dump(db, file, indent=4)
        current_id += 1
        print("Usuario creado con exito")
    except Exception as e:
        print(f"paso esto: {e}")


def peticion_usuario():
    return db["usuarios"]


def peticion_productos():
    return db["productos"]


def eliminar_db():
    if os.path.exists(path + file_name):
        os.remove(path + file_name)
        print(f"El archivo {path + file_name} ha sido eliminado.")
    else:
        print(f"El archivo {path + file_name} no existe.")