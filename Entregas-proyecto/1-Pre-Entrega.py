lista_productos=[]

def agregar_prod(lista):
    while True:
        nombre_producto=input("Ingrese nombre del producto: ")
        categoria_producto=input("Ingrese categoria del producto: ")
        precio_producto=int(input("Ingrese precio del producto: "))
        if (nombre_producto.strip()=="") or (categoria_producto.strip()==""):
            print("Uno de los campos se encuentra vacio, volver a ingresar los datos del producto")
        else:
            productos=[nombre_producto, categoria_producto, precio_producto]
            lista.append(productos)
            break

def mostrar_prod(lista_mostrar):
    bandera=0
    print("Lista de productos:")
    for producto in range(len(lista_mostrar)):
        print(f"{producto+1}. Producto: {lista_mostrar[producto][0]}\tCategoria: {lista_mostrar[producto][1]}\tPrecio: {lista_mostrar[producto][2]}")
        bandera=1
    if bandera==0:
        print("Lista vacia!")

def buscar_prod(lista_buscar):
    bandera=0
    busqueda_producto=input("Ingrese nombre de producto que desea buscar: ")
    for busqueda in lista_buscar:
        if busqueda[0]==busqueda_producto:
            print(f"Producto: {busqueda[0]}\t Categoria: {busqueda[1]}\tPrecio: {busqueda[2]}")
            bandera=1
    if bandera==0:
        print("Producto no encontrado!")       

def delete_prod(lista_delet):
    bandera=0
    delet_producto=int(input("Ingrese posicion del producto que desea eliminar: "))
    for delete in range(len(lista_delet)):
        if delete==delet_producto:
            print(f"Se elimino el producto {lista_delet[delete][0]}")
            lista_delet.remove(lista_delet[delete])
            bandera=1
    if bandera==0:
        print("Posicion no encontrada!")


while True:
    print("MENU\n1.AGREGAR PRODUCTOS\n2.MOSTRAR PRODUCTOS\n3.BUSCAR PRODUCTO\n4.ELIMINAR PRODUCTO\n5.SALIR DEL PROGRAMA")

    option=int(input("\nIngrese una opcion: "))
    if option>5 or option<0:
        print("Ingrese una opcion valida!\n")
    else:
        match option:
            case 1:
                agregar_prod(lista_productos)
            case 2:
                mostrar_prod(lista_productos)
            case 3:
                buscar_prod(lista_productos)
            case 4:
                delete_prod(lista_productos)
            case 5:
                print("Saliendo del programa")
                break
