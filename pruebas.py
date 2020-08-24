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

    def testdeberiasumarvectores(self):
        self.assertEqual(lib.sumavectores([(1,3),(2,3),(1,5)],[(5,4),(2,6),(2,5)]),[(6,7),(4,9),(3,10)])

    #def testnodeberiasumarvectores(self):
     #   self.assertRaises(Exception("Los vectores tienen diferentes longitudes no se pueden sumar"),lib.sumaVectores([(1,3),(1,2),(2,3),(1,5)],[(5,4),(2,6),(2,5)]))

    def testdeberiarestarvectores(self):
        self.assertEqual(lib.restavectores([(1,3),(2,3),(1,5)],[(5,4),(2,6),(2,5)]),[(-4,-1),(0,-3),(-1,0)])

    def testdeberiasacarinverso(self):
        self.assertEqual(lib.inversovector([(1,2),(3,-4),(-3,1)]),[(-1,-2),(-3,4),(3,-1)])
    
    def testdeberiasumarmatrices(self):
        self.assertEqual(lib.sumarmatrices([[(5,-1),(2,2)],[(0,3),(3,0)]],[[(1,2),(3,4)],[(5,6),(7,8)]]),[[(6,1),(5,6)],[(5,9),(10,8)]])
    
    def testdebeeriasacarinversomatriz(self):
        self.assertEqual(lib.inversomatriz([[(1,2),(4,5)],[(2,-1),(-4,-2)]]),[[(-1,-2),(-4,-5)],[(-2,1),(4,2)]])
    
    def testdeberiacalcularescalarporvector(self):
        self.assertEqual(lib.multiescalarmatriz(2,[[(1,3),(5,3)],[(1,4),(5,5)]]),[[(2,6),(10,6)],[(2,8),(10,10)]])
    
    def testdeberiacalculartranspuestamatriz(self):
        self.assertEqual(lib.transpuestamatriz([[(1,2),(2,3)],[(5,4),(6,6)]]),[[(1,2),(5,4)],[(2,3),(6,6)]])
    
    def testdeberiacalculartranspuestavector(self):
        self.assertEqual(lib.transpuestavector([(1,2),(1,4)]),[[(1, 2)], [(1, 4)]])
        self.assertEqual(lib.transpuestavector([[(1,2)],[(1,4)]]),[(1,2),(1,4)])

    def testdeberiacalcularconjugada(self):
        self.assertEqual(lib.conjugadomatriz([[(1,2),(2,3)],[(5,4),(6,6)]]),[[(1,-2),(2,-3)],[(5,-4),(6,-6)]])

    def testdeberiacalculardaga(self):
        self.assertEqual(lib.dagamatriz([[(1,2),(2,3)],[(5,4),(6,6)]]),[[(1,-2),(5,-4)],[(2,-3),(6,-6)]])

    def testdeberiamultiplicarmatrices(self):
        self.assertEqual(lib.multimatrices([[(1,3),(2,3)],[(4,2),(5,1)]],[[(1,2),(2,3),(4,1)],[(1,4),(3,2),(1,1)]]),[[(-15, 16), (-7, 22), (0, 18)], [(1, 31), (15, 29), (18, 18)]])

    def testdeberiacalcularaccion(self):
        self.assertEqual(lib.accion([[(1,3),(2,3)],[(4,2),(5,1)]],[(1,2),(2,3)]),[[(-10, 17)], [(7, 27)]])

    def testdeberiacalcularproductointerno(self):
        self.assertEqual(lib.productointernovectores([(1,0),(0,1),(1,-3)],[(2,1),(0,1),(2,0)]),(5,7))
    
    def testdeberiacalcularlanorma(self):
        self.assertEqual(lib.norma([(3.1,7.1),(6.6,-6.0)]),11.81)
    
    def testdeberiacalculardistancia(self):
        self.assertEqual(lib.calcdistanciaentrevectores([(1,2),(2,4),(5,0)],[(0,2),(1,2),(4,0)]),2.65)

    def testdeberiaserunitaria(self):
        self.assertTrue(lib.isunitaria([[(2/3,0),(-2/3,1/3)],[(2/3,1/3),(2/3,0)]]))

    def testdeberiaserhermitian(self):
        self.assertTrue(lib.ishermitian([[(7,0),(6,5)],[(6,-5),(-3,0)]]))
    
if __name__ == '__main__' :
    unittest.main()