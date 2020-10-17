import libreria as lib, math as m
import numpy as np
import matplotlib.pyplot as plot
import requests as req

def dinamica(M,v,t):

    """ Método que hace cambios en el estado del sistema dado el vector estado inicial y matriz de adjacencia
    :type v: list
    :param v: Vector 1 escrito de la forma [(a,b),(c,d)]

    :type w: list
    :param w: Vector 2 escrito de la forma [(a,b),(c,d)]

    :raises:

    :rtype: float
    """
    tempM = M
    for i in range(t-1):
        tempM = lib.multimatrices(tempM,M)

    return lib.multimatrices(tempM,v)
    
def observableprobabilidad(v,x):
    
    """ Description calcula la probabilidad de encontrar una particula en una posición x 
    :type v: Matriz
    :param v: Ket indicando el estado del sistema

    :type x: int
    :param x: Posición a la cual se le calculará la probabilidad

    :raises:

    :rtype: float
    """
    return round((lib.modulo(v[x])**2/lib.norma(v)**2) * 100,2)

def media(omega, ket):
    
    """ Description Calcula el valor promedio de omega en un estado(Ket) dado
    :type omega: Matriz
    :param omega: 

    :type ket: Vector columna
    :param ket:

    :raises: Exception en caso de que omega no sea hermitiana

    :rtype:
    """
    if (not lib.ishermitian(omega)):
        raise Exception("Omega debe ser hemitiana")
    producto = lib.transpuestamatriz(lib.multimatrices(omega,ket))
    ketN = lib.transpuestamatriz(ket)
    return round(lib.productointernovectores(producto,ketN)[0],2)


def delta(omega,ket):

    promedio = media(omega,ket)
    identidad = lib.matrizIdentidad(omega)
    res = lib.multiescalarmatriz(promedio,identidad)
    return lib.restarmatrices(omega,res)


def varianza(omega,ket): 

    """ Description calcula la varianza en relación a omega y un estado dado
    :type omega: Matriz
    :param omega: 

    :type ket: Matriz 
    :param ket: estado

    :raises: Exception en caso de que omega no sea hermitiana

    :rtype: float 
    """
    if (not lib.ishermitian(omega)):
        raise Exception("Omega debe ser hemitiana")
    delta1 = delta(omega,ket)
    rta = lib.multimatrices(delta1,delta1)
    return media(rta,ket)

def amplitudtransicion(keth1,keth2):

    """ Description calcula la amplitud de transitar del primer vector al segundo
    :type keth1: List
    :param keth1: Estado1

    :type keth2: List
    :param keth2: Estado2

    :raises:

    :rtype: Tuple
    """
    normav1 = lib.norma(keth1)  
    normav2 = lib.norma(keth2)
    rta = normav1 * normav2
    return lib.division(lib.productointernovectores(keth1,keth2),(rta,0))

def eigenvalues(omega):
    
    """ Description calcula los valores propios de omega
    :type omega: Matriz 
    :param omega: 

    :raises: 

    :rtype: matriz
    """
    mat1 =[[] for x  in range(len(omega))]
    for i in range(len(omega)):
        for j in range(len(omega[0])):
            mat1[i].append(complex(omega[i][j][0],omega[i][j][1]))
    rta1 , rta2 = np.linalg.eigh(mat1)
    return [rta1[0],rta1[1]]    

#print(eigenvalues([[(-1,0),(0,-1)],[(0,1),(1,0)]]))

def eigenvectors(omega):

    """ Description calcula los vectores propios de omega
    :type omega: Matriz 
    :param omega: 

    :raises:

    :rtype: Matriz con los vectores propios de omega
    """
    
    mat1 =[[] for x  in range(len(omega))]
    for i in range(len(omega)):
        for j in range(len(omega[0])):
            mat1[i].append(complex(omega[i][j][0],omega[i][j][1]))
    rta1 , rta2 = np.linalg.eigh(mat1)
    return rta2

def graphproba(v):
    data = len(v)
    x = np.array([ x for x in range( data )])
    y = np.array([ round(v[x][0]*100,2) for x in range( data )])

    plot.bar( x,y , color ='b', align='center')
    plot.title('Probabilidades')
    plot.show()









