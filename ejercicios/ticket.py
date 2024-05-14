#variables.
adulto = 5000
adultoMayor = 2500
nino = 2000
numTickets = 0
totalTickets = 0

#inicializar programa.
name = input("ingrese su nombre")
edad = int(input("ingrese su edad"))

if edad >= 18 and edad < 60 :
    numTickets = int(input("Cuantos ticket desea comprar?"))
    totalTickets = int((numTickets * adulto))
    print("Estimado ", name,  "el total a pagar es: ",totalTickets)
elif edad < 18 :
    numTickets = int(input("Cuantos ticket desea comprar?"))
    totalTickets = int((numTickets * nino))
    print("Estimado ", name,  "el total a pagar es: ",totalTickets)
elif edad >= 60 :
     numTickets = int(input("Cuantos ticket desea comprar?"))
     totalTickets = int((numTickets * adultoMayor))
     print("Estimado ", name,  "el total a pagar es: ",totalTickets)
 


