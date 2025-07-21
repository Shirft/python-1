import sqlite3
from colorama import init, Fore, Style

# Inicializar colorama para usar colores en la terminal
init(autoreset=True)

# Conexión y creación de base de datos SQLite
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

# Crear la tabla 'productos' si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio INTEGER NOT NULL,
    categoria TEXT
)
""")

# Validar que un campo no esté vacío
def validar_campo(texto, campo):
    while not texto.strip():
        print(Fore.RED + f"El campo '{campo}' no puede estar vacío.")
        texto = input(f"{campo}: ")
    return texto

# Validar que la cantidad sea un entero mayor o igual a 0
def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            return cantidad
        except ValueError as e:
            print(Fore.RED + f"Ingrese una cantidad valida. Error: {e}")

# Validar que el precio sea un número positivo
def validar_precio():
    while True:
        try:
            precio = int(input("Precio: "))
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a cero.")
            return precio
        except ValueError as e:
            print(Fore.RED + f"Ingrese un precio valido. Error: {e}")

# Registrar un nuevo producto en la base de datos
def registrar_producto():
    try:
        nombre = validar_campo(input("Nombre del producto: "), "Nombre del producto")
        descripcion = input("Descripción: ")
        cantidad = validar_cantidad()
        precio = validar_precio()
        categoria = validar_campo(input("Caregoria: "), "Categoria")
        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria,))
        conexion.commit()
        print(Fore.GREEN + "Producto registrado exitosamente.")
    except Exception as e:
        print(Fore.RED + f"Error al registrar producto: {e}")

# Mostrar todos los productos registrados
def ver_productos():
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if not productos:
            print(Fore.YELLOW + "No se encuentran productos agregados.")
        for producto in productos:
            print(producto)
    except Exception as e:
        print(Fore.RED + f"Error al mostrar productos: {e}")

# Actualizar los datos de un producto existente por su ID
def actualizar_producto():
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if not productos:
            print(Fore.YELLOW + "No se encuentran productos agregados.")
        else:
            id = validar_campo(input("ID del producto a actualizar: "), "ID")
            nombre = validar_campo(input("Nuevo nombre: "), "Nombre")
            descripcion = input("Nueva descripción: ")
            cantidad = validar_cantidad()
            while True:
                try:
                    precio = validar_precio()
                    break
                except ValueError:
                    print(Fore.RED + "Ingrese un precio valido.")
            categoria = validar_campo(input("Nueva categoría: "), "Categoría")
            cursor.execute("""
            UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id = ? 
            """, (nombre, descripcion, cantidad, precio, categoria, id,))
            conexion.commit()
            print(Fore.YELLOW + "Producto actualizado.")
    except Exception as e:
        print(Fore.RED + f"Error al actualizar producto: {e}")

# Eliminar un producto por su ID
def eliminar_producto():
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if not productos:
            print(Fore.YELLOW + "No se encuentran productos agregados.")
        else:
            id = validar_campo(input("ID del producto a eliminar: "), "ID")
            cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            conexion.commit()
            print(Fore.RED + "Producto eliminado.")
    except Exception as e:
        print(Fore.RED + f"Error al eliminar producto: {e}")

# Buscar productos por ID, nombre o categoría
def buscar_producto():
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if not productos:
            print(Fore.YELLOW + "No se encuentran productos agregados.")
        else:
            opcion = input("Buscar por 1.ID - 2.Nombre - 3.Categoría : ")
            if opcion == '1':
                id = validar_campo(input("ID: "), "ID")
                cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
            elif opcion == '2':
                nombre = validar_campo(input("Nombre: "), "Nombre")
                cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
            elif opcion == '3':
                categoria = validar_campo(input("Categoría: "), "Categoría")
                cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", ('%' + categoria + '%',))
            else:
                print(Fore.RED + "Opción inválida.")
                return
            productos = cursor.fetchall()
            for producto in productos:
                print(producto)
    except Exception as e:
        print(Fore.RED + f"Error en búsqueda: {e}")

# Mostrar productos cuyo stock esté por debajo o igual al límite
def reporte_bajo_stock():
    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if not productos:
            print(Fore.YELLOW + "No se encuentran productos agregados.")
        else:
            while True:
                try:    
                    limite = int(input("Mostrar productos con cantidad menor o igual a: "))
                    if limite<0:
                        raise ValueError("Ingrese un numero positivo.")
                    break
                except ValueError as e:
                    print(Fore.RED + f"Ingrese un limite valido. Error: {e}")
            cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
            productos = cursor.fetchall()
            print(Fore.CYAN + "Productos con bajo stock:")
            if not productos:
                print(Fore.YELLOW + "No se encuentran productos con el stock especificado.")
            else:
                for producto in productos:
                    print(producto)
    except Exception as e:
        print(Fore.RED + f"Error en el reporte. Error:{e}")

# Menú principal de la aplicación para interactuar con el usuario
def menu():
    while True:
        print(Style.BRIGHT + Fore.BLUE + "\n--- MENÚ DE INVENTARIO ---")
        print("1. Registrar producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte bajo stock")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1': registrar_producto()
        elif opcion == '2': ver_productos()
        elif opcion == '3': actualizar_producto()
        elif opcion == '4': eliminar_producto()
        elif opcion == '5': buscar_producto()
        elif opcion == '6': reporte_bajo_stock()
        elif opcion == '7':
            print(Fore.MAGENTA + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida, intente de nuevo.")

# Ejecutar el menú principal
menu()

# Cerrar la conexión a la base de datos
conexion.close()
