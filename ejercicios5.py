clientes=[]

while True:
    cliente=input("Ingrese nombre de los clientes:")
    if cliente=="":
        print("Dato vacio ingresado!")
    elif cliente=="fin":
        break
    else:
        clientes.append(cliente)

clientes.sort()
for nombres in clientes:
    print(nombres)
