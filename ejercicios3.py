
meses=1
suma=0
ingreso=0
nombre=input("Ingrese su nombre: ").capitalize()
apellido=input("Ingrese su apellido: ").capitalize()
email=input("Ingrese su correo electronico")
while meses<=6:
    ingreso=int(input(f"Ingresos del mes {meses} : "))
    if ingreso<0:
        print("ingrese un numero positivo")
        continue

    suma+=ingreso
    meses+=1

print(f"{nombre} {apellido}\n{email}\ntotal de ingresos en los 6 meses: ${suma}")