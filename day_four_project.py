"""
Adivina El Numero
"""
from random import randint

print('---------------------')
print('- ADIVINA EL NUMERO -')
print('---------------------')

nombre_jugador = input('Dime tu nombre: ')

print('---------------------')


print(f'Hola {nombre_jugador},')
print('acabo de pensar un numero del 1 al 100\nTienes 8 intentos para adivinarlo')

numero_aleatorio = randint(1,100)

INTENTOS_RESTANTES = 8
print(numero_aleatorio)

while INTENTOS_RESTANTES > 0:
    print('---------------------')
    valor_usuario = int(input('Ingrese su respuesta: '))
    if valor_usuario == numero_aleatorio:
        print(f'Correcto, {nombre_jugador}')
        break
    else:
        print(f'Incorrecto! {nombre_jugador}, te quedan {INTENTOS_RESTANTES} intentos.')
        INTENTOS_RESTANTES -= 1

        if valor_usuario < numero_aleatorio:
            print('El numero es mayor.')
        else:
            print('El numero es menor.')

if INTENTOS_RESTANTES == 0:
    print('Has perdido.')
