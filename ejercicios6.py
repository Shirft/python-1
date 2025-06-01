modelo={
    "cerveza":20,
    "tomates":10
}
while True:
    productos=modelo.copy()
    producto=input("Ingrese nombre del producto:")
    precio=input("Ingrese precio del producto:")
    if producto=="fin":
        break
    else:
        productos.setdefault(producto, precio)
        print(productos)
