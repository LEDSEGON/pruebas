import math

informacion = [
    {'tipo': 'carro', 'X': 140, 'Y': 30},
    {'tipo': 'moto', 'X': 60, 'Y': 3},
    {'tipo': 'carro', 'X': 150, 'Y': 35},
    {'tipo': 'moto', 'X': 40, 'Y': 2},
    {'tipo': 'moto', 'X': 30, 'Y': 3},
    {'tipo': 'moto', 'X': 50, 'Y': 5},
    {'tipo': 'carro', 'X': 170, 'Y': 50},
]

nuevo_dato = {'X': 135, 'Y': 25}
formula = []

for info in informacion:
    nueva_formula = {info['tipo']: math.sqrt(((nuevo_dato['Y'] - info['Y']) ** 2) + ((nuevo_dato['X'] - info['X']) ** 2))}
    formula.append(nueva_formula)


carros = filter(lambda x: 'carro' in x, formula)
carros = list(carros)

motos = filter(lambda x: 'moto' in x, formula)
motos = list(motos)

carros_ordenados = sorted(carros, key=lambda x: list(x.values())[0])
motos_ordenadas = sorted(motos, key=lambda x: list(x.values())[0])

print(carros_ordenados)
print(motos_ordenadas)
