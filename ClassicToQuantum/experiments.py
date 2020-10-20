import libreria as lib, math as m, numpy as np
import matplotlib.pyplot as plot

def probquantum(omega, ket, n):

    """ Description Calculates the probability of a Quantum System
    :type omega: Matrix
    :param omega:

    :type ket: Matriz 
    :param ket:

    :type n:
    :param n:

    :raises:

    :rtype: Matrix
    """
    temp = omega[:]
    for i in range(n):
        omega = lib.multimatrices(omega, temp)
    return finalState(omega)

def finalState(omega):
    
    """ Description Calculates the final state after a dinamic
    :type omega: Matrix
    :param omega:

    :raises:

    :rtype: Matrix
    """
    row, column = len(omega), len(omega[0])
    for i in range(row):
        for j in range(column):
            omega[i][j] = lib.modulo(omega[i][j]) ** 2
    return omega

def booleanExperiment(n, omega, ket):
    
    """ Description Simulates the marble experiment with boolean coeficients.
    :type n: int
    :param n:

    :type omega: Matrix
    :param omega:

    :type ket: vector
    :param ket:

    :raises:

    :rtype: Matrix
    """
    for i in range(n):
        ket = lib.accion(omega, ket)
    return ket
    

def probabilisticsystem(omega, ket, n):
    
    """ Description Determines the probability of the system
    :type omega: matrix
    :param omega:

    :type ket: Matrix
    :param ket:

    :type n: int
    :param n:

    :raises:

    :rtype: Matrix
    """
    for i in range(n):
        ket = lib.accion(omega, ket)
    return ket

def multipleslitexperiment(omega, ket, n):
    
    """ Description Simulates the multiple slit experiment with real coeficients
    :type omega: Matrix
    :param omega:

    :type ket: Matrix
    :param ket:

    :type n: int 
    :param n:

    :raises:

    :rtype: Matrix
    """
    return probabilisticsystem(omega, ket, n)


def multipleSlitQuantumExperiment(omega, ket, n):
    
    """ Description Simulates the multiple slit experiment with complex coeficients
    :type omega: Matrix
    :param omega:   

    :type ket: Matrix
    :param ket:

    :type n: int 
    :param n:

    :raises:

    :rtype: Matrix
    """
    return probquantum(omega, ket, n)


def graphProbabilitiesVector(vector,title):
    
    """ Description makes a graphic of the probability distribution vectors
    :type vector: list 
    :param vector:

    :raises:

    :rtype: None
    """
    x = []
    for i in range(len(vector)):
        x.append('x'+str(i))

    plot.bar( x,vector , align='center')
    plot.title(title)
    plot.show()

