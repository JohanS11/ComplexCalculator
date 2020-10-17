import unittest, ClassicToQuantum as cq ,libreria as lib, math as m

class TestClassicToQuantum(unittest.TestCase):
    def testdeberiacalcprobabilidad(self):
        self.assertEqual(cq.observableprobabilidad((
            [(2,1),
            (-1,2),
            (0,1),
            (1,0),
            (3,-1),
            (2,0),
            (0,-2),
            (-2,1),
            (1,-3),
            (0,-1)]),7),10.88)

    def testdeberiacalcprobabilidad2(self):
        self.assertEqual(cq.observableprobabilidad((
            [(2,1),
            (-1,2),
            (0,1),
            (1,0),
            (3,-1),
            (2,0),
            (0,-2),
            (-2,1),
            (1,-3),
            (0,-1)]),2),2.18) 

                               
    def testdeberiacalcamplitudtransicion(self):
        self.assertEqual(cq.amplitudtransicion([(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)],
                               [(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]),(-0.021,-0.13))

    def testdeberiacalcmedia(self):
        self.assertEqual(cq.media([[(1,0),(0,-1)],
                [(0,1),(2,0)]],
                [[(m.sqrt(2)/2,0)],
                [(0,m.sqrt(2)/2)]]),2.5)

    def testdeberiacalcvarianza(self):
        self.assertEqual(cq.varianza([[(1,0),(0,-1)],
                [(0,1),(2,0)]],
                [[(m.sqrt(2)/2,0)],
                [(0,m.sqrt(2)/2)]]),0.25)
    
    def testdeberiacalcvalorespropios(self):
        self.assertEqual(cq.eigenvalues([[(0,0),(1,0)],
                                         [(1,0),(0,0)]]),[-1,1])
    
    def testEjercicio_4_3_1(self):
        
        print("")
        print("----Ejercicio 4.3.1----")
        Sx = [[(0,0),(1,0)],
             [(1,0),(0,0)]]

        Sy = [[(0,0),(0,-1)],
             [(0,1),(0,0)]]

        Sz = [[(1,0),(0,0)],
             [(0,0),(-1,0)]]
            
        valoresp1 = str(cq.eigenvalues(Sx))
        valoresp2 = str(cq.eigenvalues(Sy))
        valoresp3 = str(cq.eigenvalues(Sz))
        vectores1 = str(cq.eigenvectors(Sx))
        vectores2 = str(cq.eigenvectors(Sy))
        vectores3 = str(cq.eigenvectors(Sz))

        print("Valores propios Sx :: " + valoresp1)
        print("Valores propios Sy :: " + valoresp2)
        print("Valores propios Sz :: " + valoresp3)
        print("-----------------")
        print("Estados a los que puede ir Sx \n"+vectores1)
        print("Estados a los que puede ir Sy \n"+vectores2)
        print("Estados a los que puede ir Sz \n"+vectores3)

    def testEjercicio_4_3_2(self):
        print("")
        print("----Ejercicio 4.3.2----")
        initialState =  [(0,0),(0,-1)]
        estado1 = [(0,1),(1,0)]
        estado2 = [(0,-1),(1,0)]

        print("Probabilidad de transicion a 1 :: "+ str(cq.amplitudtransicion(initialState,estado1)))
        print("Probabilidad de transicion a 2 :: "+ str(cq.amplitudtransicion(initialState,estado2)))

    def testEjercicio_4_4_1(self):
        print("")
        print("----Ejercicio 4.4.1----")

        U1 = [[(0,0),(1,0)],
             [(1,0),(0,0)]]

        U2 = [[(m.sqrt(2)/2,0),(m.sqrt(2)/2,0)],
             [(m.sqrt(2)/2,0),(-m.sqrt(2)/2,0)]]
        
        multiplicacion = lib.multimatrices(U1,U2)
        print("Matriz U1 Unitaria? "+str(lib.isunitaria(U1)))
        print("Matriz U2 Unitaria? "+str(lib.isunitaria(U2)))
        print("Multiplicación de U1 y U2 es unitaria? "+str(lib.isunitaria(multiplicacion)))
        
    def testEjercicio_4_4_2(self):
        print("")
        print("----Ejercicio 4.4.2----")

        matrizAdyacencia = [[(0,0),(1/m.sqrt(2),0),(1/m.sqrt(2),0),(0,0)],
                            [(0,1/m.sqrt(2)),(0,0),(0,0),(1/m.sqrt(2),0)],
                            [(1/m.sqrt(2),0),(0,0),(0,0),(0,1/m.sqrt(2))],
                            [(0,0),(1/m.sqrt(2),0),(-1/m.sqrt(2),0),(0,0)],]

        estadoInicial = [[(1,0)],
                        [(0,0)],
                        [(0,0)],
                        [(0,0)]]

        estadofinal = cq.dinamica(matrizAdyacencia,estadoInicial,3)
        estadofinal = lib.transpuestamatriz(estadofinal)
        probabilidad = cq.observableprobabilidad(estadofinal,3)


        print("Estado del sistema despues de 3 clicks: "+str(estadofinal))
        print("La probabilidad de encontrar la bola en la posición 3 es: "+ str(probabilidad))

    def testdeberiagraficarprobabilidades(self):
        cq.graphproba( [ [0,0] ,[0,0] ,[0,0] ,
                        [1/6,0],[1/6,0],[1/3,0],
                        [1/6,0],[1/6,0]] )

if __name__ == '__main__' :
    unittest.main()