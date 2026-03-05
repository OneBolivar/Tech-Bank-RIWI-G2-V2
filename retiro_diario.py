#importar la función retirar_dinero del módulo retiro cuando este lista

def control_de_retiro (monto, cuenta):
     if cuenta[ 'Retiro_diario'] + monto > cuenta['Limite_de_retiro']:
          print("Se ha superado el límite máximo de retiro permitido. su tope diario es de 500")
          return False
     else:
        cuenta[ 'Retiro_diario'] += monto
        #retirar_dinero(monto, cuenta) #descomentar esta línea cuando la función retirar_dinero esté lista
        return True