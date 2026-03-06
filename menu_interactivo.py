from registro_operaciones import historial_operaciones
from gestion_saldo import gestionsaldo
from validacion_entrada import validar_monto
from deposito import deposito

def menu(cuenta):
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    print("1- Consultar Saldo")
    print("2- Retiro de saldo")
    print("3- Depositar Dinero")
    Ejecucion = int(input("Elija una opcion: "))
    if Ejecucion == 1:
        gestionsaldo()
        historial_operaciones("Consulta", 0, cuenta['saldo'])
    elif Ejecucion == 2:
        validar_monto("Retirar", cuenta)
    elif Ejecucion == 3:
        validar_monto("Depositar", cuenta)
    else:
        print("Opcion invalida")