import libreria as lib, math as m, numpy as np
import matplotlib.pyplot as plot, experiments as exp, unittest

class TestExperiments(unittest.TestCase):
    def testdeberiagenerarcanicas(self):
        matriz = [[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]]

        initialState = [[(1,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)]]

        exp.booleanExperiment(2019,matriz,initialState)

    def testnodeberiagenerarcanicas(self):
        matriz = [[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
         [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]]

        initialState = [[(6,0)],
                        [(1,0)],
                        [(2,0)],
                        [(4,0)],
                        [(3,0)],[(3,0)]]
        exp.booleanExperiment(2019,matriz,initialState)
        exp.graphProbabilitiesVector([0,0.25,0.10,0.55,0.05,0],"Classic marbles")


        
    def testMultipleSlitClassicExperiment(self):
        matriz = [[0,0,0,0,0,0,0,0,0,0,0],
                             [(1.0/3.0),0,0,0,0,0,0,0,0,0,0],
                             [(1.0/3.0),0,0,0,0,0,0,0,0,0,0],
                             [(1.0/3.0),0,0,0,0,0,0,0,0,0,0],
                             [0,(1.0/3.0),0,1,0,0,0,0,0,0,0],
                             [0,(1.0/3.0),0,0,0,1,0,0,0,0,0],
                             [0,(1.0/3.0),(1.0/3.0),0,0,0,1,0,0,0,0],
                             [0,0, (1.0/3.0),0,0,0,0,1,0,0,0],
                             [0,0,    (1.0/3.0),(1.0/3.0),0,0,0,0,1,0,0],
                             [0,   0,    0,    (1.0/3.0),0,0,0,0,0,1,0],
                             [0,   0,    0,    (1.0/3.0),0,0,0,0,0,0,1]]

        state0 = [[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
        #exp.multipleslitexperiment(matriz,state0,5)
        exp.graphProbabilitiesVector([0,0,0,0,0,0.075,0.325,0.075,0.325,0.075,0.075,0.075],"Multiple Slit Classic")


    def testMultipleSlitQuantumExperiment(self):
        matriz = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
                                ,[[0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                [[0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                [[0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                [[0,0],[-0,1.0/m.sqrt(3.0)],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                [[0,0],[0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                [[0,0],[-0,1.0/m.sqrt(3.0)],[0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]],
                                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
                                [[0,0],[0,0],[0,1.0/m.sqrt(3.0)],[-0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
                                [[0,0],[0,0],[0,0],[0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0]],
                                [[0,0],[0,0],[0,0],[-0,1.0/m.sqrt(3.0)],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]]];
        initialState = [[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]];
        exp.graphProbabilitiesVector([0,0,0,0,0.075,0.075,0.325,0,0.325,0.075,0.075],"Multiple Slit Classic")
        

if __name__ == '__main__' :
    unittest.main()

