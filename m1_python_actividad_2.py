animal = ["gato", "pato", ]

while True :
    print("")
    print("")
    print("************************************************")
    print("Elija una opcion usando (1, 2, 3, 4, 5, 6.).")
    print("1. Crear un animal.")
    print("2. Listar todos los animales.")
    print("3. Borrar un animal por ID(Posicion).")
    print("4. Borrar un animal por nombre.")
    print("5. Borrar todos los animales.")
    print("6. Listar un animal por ID(Posicion)")
    print("************************************************")
    print("")
    print("")
    option = input("Elija un opcion: ")

    if option == "1" :
        animal.append(input("Ingrese animal: ").lower())
        print("Se creo un nuevo animal con exito")
    elif option == "2" :
        print(animal)
        
    elif option == "3":
        delete_animal = int(input("Ingrese el indice del animal a borrar:"))
        if   delete_animal < len(animal) :
            print("Se borro el animal con exito")
        else:
            print("Error el indice no existe vuelve a intentarlo") 
    elif option == "4" :
        print(f"Estos son los animales que hay: {animal}")
        name = input("Ingrese el nombre del animal a borrar: ").lower()
        if animal.count(name) > 0 :
            animal.remove(name)
            print("Se borro el animal con exito")
        else:
            print(f"{name.upper()} Este animal no esta vuelve a intentarlo")
    elif option == "5" :
        animal.clear()
        print("Se eliminaron todos los animales con exito")
    elif option == "6" :
        show = int(input("Ingrese el indice del animal a mostrar: "))
        if len(animal) > show:
            print(animal[show])
        else:
            print("El indice ingresado no existe vuelve a intentarlo")
    else:
        print("Esa opcion no esta disponible vueva a intentarlo")





