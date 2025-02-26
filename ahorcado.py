print ("BIENVENIDO A EL JUEGO DEL AHORCADO")
player = str(input("Ingrese nombre del jugador: "))

palabras = ["perro", "programacion", "camiseta", "zapato"]

intentos = 0
intentoserror = 0
i = 0


opcion = int(input("qué palabra deseas adivinar (1 a 4): "))
if opcion == 1: 
    while intentos < 5 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabras[0]:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 5:
            print(f"Has adivinado la palabra, {palabras[0]}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabras[0]} :c")
            break
elif opcion == 2: 
    while intentos < 12 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabras[1]:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 12:
            print(f"Has adivinado la palabra, {palabras[1]}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabras[1]} :c")
            break
elif opcion == 3: 
    while intentos < 8 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabras[2]:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 8:
            print(f"Has adivinado la palabra, {palabras[2]}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabras[2]} :c")
            break
elif opcion == 4: 
    while intentos < 6 and intentoserror < 9:
        i = i +1
        letra = str(input(f"{player}, ingrese letra {i}: "))
        if letra in palabras[3]:
            print ("Correcto")
            intentos = intentos + 1
        else:
            print("FALLASTE")
            intentoserror = intentoserror + 1 
        if intentos == 6:
            print(f"Has adivinado la palabra, {palabras[3]}, felicitaciones")
            break
        if intentoserror == 9:
            print(f"Has perdido el juego, la palabra era: {palabras[3]} :c")
            break
        
            


    
