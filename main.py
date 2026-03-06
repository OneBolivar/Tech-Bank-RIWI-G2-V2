from autentificiacion import autentificacion
from saludo import saludo 
from registro_operaciones import mostrar_historial

cuenta={
    'saldo':1000,
    'pin': "1234"
}

saludo()

autentificacion(cuenta)
mostrar_historial()


