import unittest, libreria as lib, math as m


class Test_complejos(unittest.TestCase):

    def testdeberiasumar(self):
        self.assertEqual(lib.sumar((1,2),(3,4)),(4,6))

    def testdeberiasumar2(self):
        self.assertEqual(lib.sumar((5,2),(8,7)),(13,9))

    def testdeberiasumar3(self):
        self.assertEqual(lib.sumar((11,2),(8,4)),(19,6))

    def testdeberiarestar(self):
        self.assertEqual(lib.restar((1,2),(3,4)),(-2,-2))
    
    def testdeberiarestar2(self):
        self.assertEqual(lib.restar((-1,-4),(-5,-7)),(4,3))
    
    def testdeberiarestar3(self):
        self.assertEqual(lib.restar((10,5),(10,5)),(0,0))

    def testdeberiamultiplicar(self):
        self.assertEqual(lib.multiplicar((2,3),(4,5)),(-7,22))

    def testdeberiamultiplicar2(self):
        self.assertEqual(lib.multiplicar((4,3),(5,7)),(-1,43))

    def testdeberiamultiplicar3(self):
        self.assertEqual(lib.multiplicar((1,4),(2,8)),(-30,16))

    def testdeberiadividir(self):
        self.assertEqual(lib.division((5,4),(-2,-4)),(-13/10,3/5))

    def testdeberiadividir2(self):
        self.assertEqual(lib.division((1,4),(2,8)),(1/2,0))

    def testdeberiadividir3(self):
        self.assertEqual(lib.division((6,4),(3,3)),(5/3,-1/3))
    
    def testdeberiacalcmodulo(self):
        self.assertEqual(lib.modulo((5,3)),m.sqrt(34))
    
    def testdeberiacalcmodulo2(self):
        self.assertEqual(lib.modulo((10,2)),m.sqrt(104))
    
    def testdeberiacalcmodulo3(self):
        self.assertEqual(lib.modulo((1,5)),m.sqrt(26))

    def testdeberiacalconjugado(self):
        self.assertEqual(lib.conjugado((-5,-10)),(-5,10))
    
    def testdeberiapasarapolar(self):
        self.assertEqual(lib.topolar((3,4)),(5,0.93))
    
    def testdeberiapasaracartesiano(self):
        self.assertEqual(lib.tocartesian(5,m.pi/4),(3.54,3.54))
    
    def testdeberiacalcfase(self):
        self.assertEqual(lib.fase((5,6)),0.88)

    def testdeberiacalcfase2(self):
        self.assertEqual(lib.fase((10,7)),0.61)
    

if __name__ == '__main__':
    unittest.main()