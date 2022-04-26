# Teste para calcular area
import unittest

class Triangulo():
    def EhTriangulo(self):
        if self.a < (self.b + self.c):
            if self.b < (self.a + self.c):
                if self.c < (self.a + self.b):
                    return True
        return False

    def EhEscaleno(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return True
        else:
            return False

    def EhEquilatero(self):
        if self.a == self.b == self.c:
            return True
        else:
            return False

    def EhIsosceles(self):
        if self.a == self.b == self.c:
            return False
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        else:
            return False

class MyCalcTest(unittest.TestCase):
    def testEhTriangulo(self):
        triangulo = Triangulo()
        triangulo.a = 3
        triangulo.b = 4
        triangulo.c = 5
        self.assertTrue(triangulo.EhTriangulo())

    def testEhEscaleno(self):
        tri = Triangulo()
        tri.a = 3
        tri.b = 4
        tri.c = 5
        self.assertTrue(tri.EhEscaleno())

    def testEhEquilatero(self):
        tri = Triangulo()
        tri.a = 3
        tri.b = 3
        tri.c = 3
        self.assertTrue(tri.EhEquilatero())

    def testEhIsosceles(self):
        tri = Triangulo()
        tri.a = 2
        tri.b = 2
        tri.c = 5
        self.assertTrue(tri.EhIsosceles())

if __name__ == '__main__':
    unittest.main()
