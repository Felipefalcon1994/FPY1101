
totalIngresos = 0
cantidadPasajes = 0

try:
    cantidadPasajes = int(input("cuantos pasajes desea vender?: "))
except:
    print("Solo se admiten números.")

for i in range (cantidadPasajes):
    try: 
       print(f"Cuanto cobra por el pasaje {i+1}: ") 
       valorPasaje = int(input("Ingrese valor: "))
    except:
        print("Solo se permite un valor numérico.")
        
    totalIngresos += valorPasaje 

print(f"El total de ingresos por la venta de {i+1} pasajes es de: {totalIngresos}.")   
