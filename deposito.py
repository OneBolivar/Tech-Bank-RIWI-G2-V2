from registro_operaciones import historial_operaciones
def deposito(valor,cuenta):
  cuenta['saldo']+= valor
  print (" Su Deposito fue exitoso, su nuevo saldo es:", cuenta['saldo']) 
  historial_operaciones("Depositar", valor, cuenta['saldo'])


