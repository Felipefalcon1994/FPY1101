contVocales = 0
contCons = 0

strng = input("Ingrese una cadena de texto")
strng = strng.lower()
for i in strng:
    if i.isalpha():
        if i in "aeiou":
            contVocales += 1
        else:
            contCons += 1
    else:
        print("SOLO SE PERMITEN LETRAS")       
        break 
print(f"Vocales {contVocales}, Consonantes: {contCons}")