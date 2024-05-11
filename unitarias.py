import unittest
from euclidiana import Euclidiana

class TestEuclidiana(unittest.TestCase):
    def test_calcular_distancias(self):
        euclidiana = Euclidiana()
        nuevo_dato = {'X': 135, 'Y': 1.3}
        carros_ordenados, motos_ordenadas = euclidiana.calcular_distancias(nuevo_dato)
        # Aquí puedes agregar afirmaciones (assertions) para verificar si los resultados son correctos
        self.assertEqual(len(carros_ordenados), 3)
        self.assertEqual(len(motos_ordenadas), 4)

if __name__ == '__main__':
    unittest.main()
