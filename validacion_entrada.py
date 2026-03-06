from deposito import deposito
from Reglas_de_Negocio import validacion_limite_retiro
from retiro_diario import control_de_retiro
def validar_monto(tipo_operacion, cuenta):
    while True:
        try:
            monto = int(input(f"Ingrese el monto a {tipo_operacion}: "))
            
            if monto < 0:
                    print("Error: El monto no puede ser negativo.")
            else:
                    print(f"Ingreso correcto del monto a {tipo_operacion}: {monto}")
                    if(tipo_operacion=="Retirar"):
                        if(validacion_limite_retiro(monto, cuenta)== True): 
                            if (control_de_retiro(monto, cuenta) == True):
                                break
                    else:
                        deposito(monto, cuenta)
                        break
                    return monto

        except ValueError:
            print("ERROR! Debe ingresar un número entero")