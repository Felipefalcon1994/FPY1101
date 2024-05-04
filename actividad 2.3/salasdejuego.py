#variables
precioAdulto = 5000
precioJoven = 3500
precioMenor = 0
usuarios = 0
total = 0
totalFamilia = 0

edad = int(input("Ingrese su edad"))
if edad >= 4 and edad < 18:
    print("El precio de la entrada es de: ",precioJoven)
    usuarios = int(input("Cuantas personas tienen entre 4 y 18 años?"))
    total = usuarios * precioJoven
    print("El precio a pagar es de: ",total)
if edad > 18:
    print("El precio de la entrada es de: ",precioAdulto)
    usuarios = int(input("Cuantas personas tienen mas de 18 años?"))  
    total = usuarios * precioAdulto
    print("El precio a pagar es de: ",total)
if edad < 4: 
    print("No paga entrada")
totalFamilia = total    