
lista_productos=[]

def agregar_prod():
    nombre_producto=input("Ingrese nombre del producto: ")
    precio_producto=int(input("Ingrese precio del producto: "))

    producto=[nombre_producto, precio_producto]

    lista_productos.append(producto)

def consulta_prod(list_prod):
    print("Productos en lista: ")
    for products in list_prod:
        print(f"Nombre: {products[0]}\t Precio: {products[1]}")


def delete_prod(list_prod):
    product_deleted=input("Ingrese nombre del producto a eliminar: ")
    for product in list_prod:
        if product[0]==product_deleted:
            list_prod.remove(product)
            print(f"Producto {product_deleted} eliminado")

while True:
    print("MENU")
    print("1. AGREGAR PRODUCTOS\n2. CONSULTAR LISTA DE PRODUCTOS\n3. ELIMINAR UN PRODUCTO\n4. PARA SALIR DEL PROGRAMA")

    opcion=int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            agregar_prod()
        case 2:
            consulta_prod(lista_productos)
        case 3:
            delete_prod(lista_productos)
        case 4:
            print("Saliendo del programa")
            break

