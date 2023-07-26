#parte grafica de la app

def menu_inicio():
    print("""
    (1) - Login
    (2) - Registro
    (3) - Eliminar DB
    (4) - Salir
    """)

def menu_usuario():
    print("""
    (1) - Comprar
    (2) - Mostrar usuario actual
    (3) - Salir          
    """)

def mostrar_productos(db_productos):
    for producto in db_productos:
        print(f"""
        id = {producto["id"]}
        nombre = {producto["nombre"]}
        precio = {producto["precio"]}
        descripcion = {producto["descripcion"]}
        distribuidor = {producto["distribuidor"]}
    """)

def mostrar_usuario():
    pass