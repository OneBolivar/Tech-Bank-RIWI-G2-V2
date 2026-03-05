# Se crea funcion con parametro basado en el tipo de operacion "retirar" & "depositar"
def validar_monto(tipo_operacion):
    while True:
        try:
            monto = int(input(f"Ingrese el monto a {tipo_operacion}: "))
            
            if monto < 0:
                    print("Error: El monto no puede ser negativo.")
            else:
                    print(f"Ingreso correcto del monto a {tipo_operacion}: {monto}")
                    return monto
        except ValueError:
            print("ERROR! Debe ingresar un número entero")