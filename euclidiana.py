import math

class Euclidiana:
    def __init__(self):
        self.informacion = [
            {'tipo': 'carro', 'X': 140, 'Y': 30},
            {'tipo': 'moto', 'X': 60, 'Y': 3},
            {'tipo': 'carro', 'X': 150, 'Y': 35},
            {'tipo': 'moto', 'X': 40, 'Y': 2},
            {'tipo': 'moto', 'X': 30, 'Y': 3},
            {'tipo': 'moto', 'X': 50, 'Y': 5},
            {'tipo': 'carro', 'X': 170, 'Y': 50},
        ]

    def calcular_distancias(self, nuevo_dato):
        formula = []
        for info in self.informacion:
            nueva_formula = {info['tipo']: math.sqrt(((nuevo_dato['Y'] - info['Y']) ** 2) + ((nuevo_dato['X'] - info['X']) ** 2))}
            formula.append(nueva_formula)
        carros = filter(lambda x: 'carro' in x, formula)
        motos = filter(lambda x: 'moto' in x, formula)
        carros_ordenados = sorted(carros, key=lambda x: list(x.values())[0])
        motos_ordenadas = sorted(motos, key=lambda x: list(x.values())[0])
        return carros_ordenados, motos_ordenadas
    