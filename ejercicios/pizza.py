#La pizzería pepe jhons ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza son los siguientes:

#Ingredientes vegetarianos: Pimiento, Cebolla, Choclo y tofu.
#Ingredientes no vegetarianos: Pepperoni, Jamón, Chorizo y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
#en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
#Solo se puede elegir 2 ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
#Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

#variables:


print("Bienvenido a Pepe Juan's")
print("")
opt = (input("Desea una Pizza Vegetariana?, yes/no:"))
if opt == "yes":
    print("Los Ingredientes Disponibles son:")
    print("1. Pimiento")
    print("2. Cebolla")
    print("3. Choclo")
    print("4. Tofu")
    print("Recuerda que solo puedes elegir dos ingredientes")
    print("La Mozzarella y la salsa ya vienen incluidas")
    ing1 = (input("Cual será su primer ingrediente?"))
    ing2 = (input("Cual será su segundo ingrediente?"))
    print("Has elegido una pizza vegetariana con ", ing1, "y" ,ing2, "DISFRUTALA!" )

if opt == "no":
    print("Los Ingredientes Disponibles son:")
    print("5. Pepperoni")
    print("6. Jamón")
    print("7. Chorizo")
    print("8. Salmón")
    print("Recuerda que solo puedes elegir dos ingredientes")
    print("La Mozzarella y la salsa ya vienen incluidas")
    ing1 = (input("Cual será su primer ingrediente?"))
    ing2 = (input("Cual será su segundo ingrediente?"))
    print("Has elegido una pizza no vegetariana con ", ing1, "y" ,ing2, "DISFRUTALA!" )

