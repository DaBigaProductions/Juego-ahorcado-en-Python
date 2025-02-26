print ("BIENVENIDO A EL JUEGO DEL AHORCADO")
player = str(input("Ingrese nombre del jugador: "))

palabra1 = "perro"
palabra2 = "programacion"
palabra3 = "camiseta"
palabra4 = "zapato"
intentos = 0
intentoserror = 0
i = 0


opcion = int(input("qué palabra deseas adivinar (1 a 4): "))
if opcion == 1: 
    while intentos < 5 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabra1:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 5:
            print(f"Has adivinado la palabra, {palabra1}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabra1} :c")
            break
elif opcion == 2: 
    while intentos < 12 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabra2:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 12:
            print(f"Has adivinado la palabra, {palabra2}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabra2} :c")
            break
elif opcion == 3: 
    while intentos < 8 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabra3:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 8:
            print(f"Has adivinado la palabra, {palabra3}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabra3} :c")
            break
elif opcion == 4: 
    while intentos < 6 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabra4:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 6:
            print(f"Has adivinado la palabra, {palabra4}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabra4} :c")
            break
        
            


    
