def validacion_limite_retiro (monto, cuenta):
    while True:
        if monto > cuenta['saldo']:
            print("Monto excede el saldo en cuenta")
            return False
        else: 
            print("Monto dentro del saldo")
            return True
            