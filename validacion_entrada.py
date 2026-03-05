# Se crea funcion con parametro basado en el tipo de operacion "retirar" & "depositar"
def validar_monto(tipo_operacion):
    while True:
        monto = int(input(f"Ingrese el monto a {tipo_operacion}: "))