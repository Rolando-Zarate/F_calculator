var = 1
import math
from os import system
from colorama import Back, Fore, init
init(autoreset=True)
while var == 1:
    try:
        print(Back.GREEN + "F_calculator")
        print("1. Calcular", "2. Creditos")
        option = int(input("opción: "))
        if option == 1:
             entrada = input(str())
             salida = eval(entrada)
             print(Fore.CYAN + "el resultado es:", + salida)
             input("ENTER")
             system("cls")
        elif option == 2:
            print("F_Calculator")
            print("Ver.: 3.0.1")
            print("F_calculator es una calculadora de interfaz")
            print("de texto desarrollada por Fernando Jelvez.")
            print(" Esta nueva versión es capaz de hacer lo mismo")
            print("y más que la anterior con menor tamaño y mas simple")
        else:
            print("ERROR, RESPUESTA NO RECONOCIDA")
        print("1. salir", "2. volver a empezar")
        option = int(input("opción: "))
        if option == 1:
            exit()
        else:
            system("cls")
    except:
        print(Fore.RED, + "ERROR")
input()

