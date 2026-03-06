from Reglas_de_Negocio import validacion_limite_retiro
cuenta = {
    'Saldo': 1000,
}
monto = float(input("Ingrese el monto a retirar: "))
validacion_limite_retiro(monto, cuenta)
