from flask import Flask, render_template
import math
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

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
        data = []
        for info in self.informacion:
            distancia = math.sqrt(((nuevo_dato['Y'] - info['Y']) ** 2) + ((nuevo_dato['X'] - info['X']) ** 2))
            data.append({'tipo': info['tipo'], 'X': info['X'], 'Y': info['Y'], 'distancia': distancia})
        return data
    
def generar_grafica():
    euclidiana = Euclidiana()
    nuevo_dato = {'X': 135, 'Y': 25}
    data = euclidiana.calcular_distancias(nuevo_dato)

    x_carro = [d['X'] for d in data if d['tipo'] == 'carro']
    y_carro = [d['Y'] for d in data if d['tipo'] == 'carro']
    x_moto = [d['X'] for d in data if d['tipo'] == 'moto']
    y_moto = [d['Y'] for d in data if d['tipo'] == 'moto']

    plt.scatter(x_carro, y_carro, color='blue', label='Carro')
    plt.scatter(x_moto, y_moto, color='red', label='Moto')
    plt.scatter(nuevo_dato['X'], nuevo_dato['Y'], color='green', label='Nuevo Dato')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfica de Dispersión')
    plt.legend()
    plt.grid(True)
    
    # Verificar si el directorio 'static' existe, si no, crearlo
    if not os.path.exists('static'):
        os.makedirs('static')
        
    plt.savefig('static/grafica.png')  # Guardar la imagen en el directorio static
    plt.close()

generar_grafica()  # Generar la gráfica antes de iniciar el servidor Flask

@app.route('/')
def index():
    euclidiana = Euclidiana()
    nuevo_dato = {'X': 135, 'Y': 25}
    data = euclidiana.calcular_distancias(nuevo_dato)
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)