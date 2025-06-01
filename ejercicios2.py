nombre=input("Ingrese Nombre: ").capitalize()
apellido=input("Ingrese su apellido: ").capitalize()
email=input("Ingrese email: ")
edad= int(input("Ingrese edad: "))

if (email.count("@")==1) and (email.find(" ")==-1):
    print(nombre,apellido,"\n",email,"\n",edad )
else:
    print("El email ingresado no es correcto")

if(edad<15):
    print("Niño/a")
elif (edad>15) and (edad<18):
    print("Adolescente")
else:
    print("Adulto")