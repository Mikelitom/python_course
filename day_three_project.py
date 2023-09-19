"""
Analizador de texto - Proyexto Dia 2
"""

print('- Analizador de Texto -')
print('-----------------------')

texto = input('Ingresa tu texto: ')

print('-----------------------')

lower_texto = texto.lower()

primera_letra = input('Letra uno: ')
segunda_letra = input('Letra dos: ')
tercera_letra = input('Letra tres: ')

cantidad_uno = lower_texto.count(primera_letra.lower())
cantidad_dos = lower_texto.count(segunda_letra.lower())
cantidad_tres = lower_texto.count(tercera_letra.lower())

lista_palabras = texto.split()
total_palabras = len(lista_palabras)
LISTA_INVERSA = ' '.join(lista_palabras[::-1])
print('-----------------------')

print(f'El total de {primera_letra.upper()}: {cantidad_uno}')
print(f'El total de {segunda_letra.upper()}: {cantidad_dos}')
print(f'El total de {tercera_letra.upper()}: {cantidad_tres}')

print('-----------------------')

print(f'El total de palabras del texto es: {total_palabras}')

print('-----------------------')

print(f'Primera letra del texto: {texto[0]}')
print(f'Ultima letra del texto: {texto[-1]}')

print('-----------------------')

print(f'El texto inverso es: {LISTA_INVERSA}')

print('-----------------------')

print(f'Esta "python" en el tecto? {"python" in lower_texto}')
