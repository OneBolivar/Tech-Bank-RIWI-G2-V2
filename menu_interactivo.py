from registro_operaciones import historial_operaciones
from gestion_saldo import gestionsaldo

def menu():
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    print("1- Consultar Saldo")
    print("2- Retiro de saldo")
    print("3- Depositar Dinero")
    Ejecucion = int(input("Elija una opcion: "))
    if Ejecucion == 1:
        gestionsaldo()
    elif Ejecucion == 2:
        print()
    elif Ejecucion == 3:
        print()
    else:
        print("Opcion invalida")