import unittest, libreria as lib, math as m

class Test_complejos(unittest.TestCase):

    def testdeberiasumar(self):
        self.assertEqual(lib.sumar((1,2),(3,4)),(4,6))

    def testdeberiarestar(self):
        self.assertEqual(lib.restar((1,2),(3,4)),(-2,-2))

    def testdeberiamultiplicar(self):
        self.assertEqual(lib.multiplicar((2,3),(4,5)),(-7,22))

    def testdeberiadividir(self):
        self.assertEqual(lib.division((5,4),(-2,-4)),(-13/10,3/5))
    
    def testdeberiacalcmodulo(self):
        self.assertEqual(lib.modulo((5,3)),m.sqrt(34))

    def testdeberiacalconjugado(self):
        self.assertEqual(lib.conjugado((-5,-10)),(-5,10))
    
    def testdeberiapasarapolar(self):
        self.assertEqual(lib.topolar((3,4)),(5,0.93))
    
    def testdeberiapasaracartesiano(self):
        self.assertEqual(lib.tocartesian(5,m.pi/4),(3.54,3.54))
    
    def testdeberiacalcfase(self):
        self.assertEqual(lib.fase((5,6)),0.88)
    

if __name__ == '__main__':
    unittest.main()