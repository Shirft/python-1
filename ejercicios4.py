lista=["miguel", " pablo", " ", " ", "jorge"]
for cliente in range(len(lista)):
    if lista[cliente].strip()=="":
        print(f"Cliente {cliente+1}: Dato no valido")
        continue
    print(f"Cliente {cliente+1}: {lista[cliente].strip().capitalize()}")
    
