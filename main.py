from autentificiacion import autentificacion
from saludo import saludo 

cuenta={
    'saldo':1000,
    'pin': "1234"
}

saludo()

codigo =input("DIGITE EL PIN DE SU CUENTA: ")
autentificacion(codigo,cuenta)


