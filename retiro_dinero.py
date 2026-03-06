from registro_operaciones import historial_operaciones

def retirar_dinero(valor, cuenta):
    cuenta['saldo']-= valor
    print(f"Has retirado {valor}. Tu nuevo saldo es {cuenta['saldo']}.")
    historial_operaciones("Retirar", valor, cuenta['saldo'])