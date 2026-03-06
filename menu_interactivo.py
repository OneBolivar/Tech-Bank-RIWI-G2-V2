from registro_operaciones import historial_operaciones

def menu(cuenta):
    print("=" * 30)
    print("             Menu")
    print("=" * 30)
    print("1- Consultar Saldo")
    print("2- Retiro de saldo")
    print("3- Depositar Dinero \n")
    Ejecucion = int(input("Elija una opcion: "))
    if Ejecucion == 1:
        historial_operaciones("Consulta", 0, cuenta['saldo'])
    elif Ejecucion == 2:
        print("Aqui va la logica  de retiro ")
    elif Ejecucion == 3:
        print("Opcion de depositar")
    else:
        print("Opcion invalida")
