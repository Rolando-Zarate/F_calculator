from os import system
while True:
    try:
        print("F_calculatorNC")
        print("1.Calcular 2.'Acerca de'") 
        option = int(input("Opción: "))
        if option == 1:
            try:
                entrada=str(input())
                salida=eval(entrada)
                print("El resultado es:", + salida)
            except ValueError:
                print("ERROR (ValueError)")
            except SyntaxError:
                print("ERROR (SyntaxError)")
            input()
        elif option == 2:
            print("F_calculatorNC es el sucesor de F_calculator tiene")
            print("mejor desempeño y menos errores.")
            print(" Desarrollado por Fernado jelvez")
            print("Ver:Beta")
            print("Enter")
            input()
        else:
            print("ERROR: ELIJA UNA OPCIÓN VALIDA")
        system("cls")
        print("1.Volver a empezar 2.Salir")
        option = int(input("Opción: "))
        if option == 1:
            system("cls")
            continue
        elif option == 2:
            exit
        else:
            print("ERROR: ELIJA UNA OPCIÓN VALIDA")
    except ValueError:
        print("ERROR: DEBE DAR EL NÚMERO DE LA OPCIÓN")
        print("Enter")
        input()
        system("cls")
input()
