var = 1
from os import system
from colorama import Back, Fore, init
init(autoreset=True)
import locale
language = str(locale.getdefaultlocale())
language.find("es_")
if True:
    while True:
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
                print("Ver.: 4.0")
                print("F_calculator es una calculadora de interfaz")
                print("de texto desarrollada por Fernando Jelvez.")
                print(" Esta versión implementa soporte de idiomas")
            else:
                print("ERROR, RESPUESTA NO RECONOCIDA")
            print("1. salir", "2. volver a empezar")
            option = int(input("opción: "))
            if option == 1:
                system("exit")
            else:
                system("cls")
        except NameError:
            print(Fore.RED + "ERROR")
        except SyntaxError:
            print(Fore.RED + "ERROR")
        except SyntaxError:
            print(Fore.RED + "ERROR")
        print("ENTER")
        input()
        system("cls")
else:
    languaje.find("en_")
    if True:
            while True:
                try:
                    print(Back.GREEN + "F_calculator")
                    print("1. Calculate", "2. Credits")
                    option = int(input("option: "))
                    if option == 1:
                        entrada = input(str())
                        salida = eval(entrada)
                        print(Fore.CYAN + "The result is:", + salida)
                        input("ENTER")
                        system("cls")
                    elif option == 2:
                        print("F_Calculator")
                        print("Ver.: 4.0")
                        print("F_calculator is a text interface calculator")
                        print("developed by Fernando Jelvez.")
                        print(" This version implements languaje support")
                    else:
                        print("ERROR, NOT RECOGNIZED ANSWER")
                    print("1. Exit", "2. Start over")
                    option = int(input("option: "))
                    if option == 1:
                        system("exit")
                    else:
                        system("cls")
                except NameError:
                    print(Fore.RED + "ERROR")
                except SyntaxError:
                    print(Fore.RED + "ERROR")
                except SyntaxError:
                    print(Fore.RED + "ERROR")
                print("ENTER")
                input()
                system("cls")
    else:
        print("Languaje Error")
input()

