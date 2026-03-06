def validacion_limite_retiro (monto, saldo):
    while True:
        if monto > saldo:
            print("Monto excede el saldo en cuenta")
            monto = int(input("Por favor ingresa el monto a retirar nuevamente: "))
        else: 
            print("Monto a retirar valido")
            break