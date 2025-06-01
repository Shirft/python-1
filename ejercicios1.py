nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
correo=input("Correo Electronico: ")

if (nombre and apellido and correo >"") and (edad>18):
    print(nombre,"\n",apellido,"\n",edad,"\n",correo)
else:
    print("\nERROR!")
