# Teste para calcular area
import unittest

class Area():
    def quadrada(self):
        return self.lado1 * self.lado2

    def cubica(self):
        return self.lado1 * self.lado2 * self.lado3

class MyCalcTest(unittest.TestCase):
    def testAreaQuadrada(self):
        area = Area()
        area.lado1 = 3
        area.lado2 = 9
        self.assertEqual(27, area.quadrada())

    def testAreaCubica(self):
        area = Area()
        area.lado1 = 2
        area.lado2 = 2
        area.lado3 = 2
        self.assertEqual(8, area.cubica())

if __name__ == '__main__':
    unittest.main()
