import math as m 

def sumar(compA,compB):
    
    """ Description
    Retorna la suma de dos números complejos 
    (a,bi) +( c,di) = (a+c),(b+d)i

    :type tuple
    :param compA: Número complejo escrito en pares ordenados de la forma (a,b)

    :type tuple
    :param compB: Número complejo escrito en pares ordenados de la forma (a,b)
    :raises:

    :rtype:"""
        
    rtaReal = float(compA[0]+compB[0])
    rtaImag = float(compA[1]+compB[1])
    resultado = (rtaReal,rtaImag)
    return resultado

def restar(compA,compB):

    
    """ Description
    Retorna la resta de dos números complejos 
    (a,bi) - (c+di) = (a-c),(b-d)i
    :type tuple
    :param compA: Número complejo escrito en pares ordenados de la forma (a,b)

    :type tuple
    :param compB: Número complejo escrito en pares ordenados de la forma (a,b)

    :raises:

    :rtype:
    """

    rtaReal = float(compA[0]-compB[0])
    rtaImag = float(compA[1]-compB[1])
    resultado = (rtaReal,rtaImag)
    return resultado

def multiplicar(compA,compB):
    
    """ Description
    Retorna la multiplicación de dos números complejos
    (a,bi) * (c,di) = (a*c-b*d,a*d+b*c)
    :type tuple
    :param compA: Número complejo escrito en pares ordenados de la forma (a,b)

    :type tuple
    :param compB: Número complejo escrito en pares ordenados de la forma (a,b)

    :raises:

    :rtype:
    """
    rtaReal = float(compA[0] * compB[0] - compA[1] * compB[1])
    rtaImaginaria = float(compA[1] * compB[0] + compA[0] * compB[1])
    resultado = (rtaReal,rtaImaginaria)
    return resultado

def division(compA,compB):
    
    """ Description
    Retorna la división entre dos números enteros
    (a,b) / (c,d) = ((a*c + b*d)/(c**2 + d**2) + (c*b-a*d)/(c**2 + d**2))

    :type tuple: 
    :param compA: Número complejo escrito en pares ordenados de la forma (a,b)

    :type tuple:
    :param compB: Número complejo escrito en pares ordenados de la forma (a,b)

    :raises: ZeroDivisionError en caso de que la división esté indefinida

    :rtype:
    """
    numerador1 = compA[0] * compB[0] + compA[1] * compB[1]
    denominador = compB[0] ** 2 + compB[1] ** 2
    numerador2 = compA[1] * compB[0] - compA[0] * compB[1]
    try:
        resultado = (float(numerador1/denominador),float(numerador2/denominador))
    except ZeroDivisionError:
        print("La división para estos complejos no está indefinida")
    return resultado    

def modulo(comp):

    """ Description
    Retorna el modulo del número complejo
    (a,bi) = (a**2 + b**2)**0.5

    :type tuple:
    :param comp: Número complejo escrito en pares ordenados de la forma (a,b)

    :raises:

    :rtype:
    """
    resultado = float(m.sqrt((comp[0])**2+(comp[1])**2))
    return resultado    

def conjugado(comp):

    """ Description
    :type tuple
    :param comp: Número complejo escrito en pares ordenados de la forma (a,b)

    :raises:

    :rtype:
    """
    return (comp[0],comp[1] * -1)

def topolar(comp):
    
    """ Description
    :type tuple:
    :param comp: Número complejo escrito en pares ordenados de la forma (a,b)

    :raises:

    :rtype:
    """
    mod = modulo(comp)
    tetha = m.atan(comp[1]/comp[0])
    return (round((mod),2),round((tetha),2))

def tocartesian(r,tetha):

    """ Description
    :type float: 
    :param float: Módulo del vector 

    :type float:
    :param tetha: Ángulo de apertura del vector escrito en radianes 

    :raises:

    :rtype:
    """
    x = round(r * m.cos(tetha),2)
    y = round(r * m.sin(tetha),2)
    return (x,y)

def fase(comp):

    """ Description
    Calcula la fase del complejo

    :type tuple:
    :param comp: Complejo escrito de la forma (a,b)

    :raises:

    :rtype:
    """
    resultado = m.atan(comp[1]/comp[0])
    return round(resultado,2)

def sumavectores(v,w):
    
    """ Description: Adiciona dos vectores con dimensiones equivalentes
    :type v: list
    :param v: Vector 1 escrito de la forma [(1,2),(3,5)...(x,y)]

    :type w: list
    :param w: Vector 2 escrito de la forma [(1,2),(3,5)...(x,y)]

    :raises: Exception en caso de que los vectores no tengan el mismo tamaño

    :rtype: list - Vector resultante escrito de la forma [(a,b),(c,d),..(x,y)]
    """
    if (len(v) != len(w)):
        raise Exception("Los vectores tienen diferentes longitudes no se pueden sumar")
    else:
        rta = []
        for i in range(len(v)):
            rta.append(sumar(v[i],w[i]))
    return rta

def restavectores(v,w):
    
    """ Description: Sustrae dos vectores con dimensiones equivalentes
    :type v: list
    :param v:Vector 1 escrito de la forma [(1,2),(3,5)...(x,y)]

    :type w: list
    :param w: Vector 2 escrito de la forma [(1,2),(3,5)...(x,y)]
 
    :raises: Exception en caso de que los vectores no tengan el mismo tamaño

    :rtype: list - Vector resultante escrito de la forma [(a,b),(c,d),..(x,y)]
    """
    if (len(v) != len(w)):
        raise Exception("Los vectores tienen diferentes longitudes no se pueden restar")
    else:
        rta = []
        for i in range(len(v)):
            rta.append(restar(v[i],w[i]))
    return rta

def inversovector(v):
    
    """ Description: Retorna el inverso aditivo del vector insertado
    :type v: list
    :param v: Vector escrito de la forma [(1,2),(3,5)...(x,y)]

    :raises: 

    :rtype: Vector resultante escrito de la forma [(a,b),(c,d),..(x,y)]
    """
    return escalarporvector(-1,v)

def escalarporvector(r,v):

    """ Description: Retorna un vector multiplicado por un escalar (r*V)
    :type r: int / float 
    :param r: Escalar que será multiplicado por el vector

    :type v: list 
    :param v: Vector escrito de la forma [(a,b),(c,d)...(x,y)]

    :raises: 

    :rtype: list- Vector escrito de la forma [(ra,rb),(rc,rd)...(rx,ry)]
    """
    for i in range(len(v)):
        v[i] = ((v[i][0] * r, v[i][1] * r))
    return v 

def sumarmatrices(M,N):
    
    """ Description Adiciona dos matrices M,N
    :type M: matrix 
    :param M: Matriz 1 escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :type N: matrix
    :param N: Matriz 2 escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises: Exception - en caso que las matrices no tengan tamaños equivalentes

    :rtype: matrix- matriz resultante de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]
    """
    if (len(M) != len(N)):
        raise Exception("Las matrices no se puede sumar porque tienen tamaños distintos")
    else:
        rta = []
        for i in range(len(M)):
            rta.append(sumavectores(M[i],N[i]))
    return rta

def restarmatrices(M,N):
    
    """ Description resta dos matrices M,N
    :type M: matrix 
    :param M: Matriz 1 escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :type N: matrix
    :param N: Matriz 2 escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises: Exception - en caso que las matrices no tengan tamaños equivalentes

    :rtype: matrix- matriz resultante de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]
    """
    if (len(M) != len(N)):
        raise Exception("Las matrices no se puede restar porque tienen tamaños distintos")
    else:
        rta = []
        for i in range(len(M)):
            rta.append(restavectores(M[i],N[i]))
    return rta

def inversomatriz(M):

    """ Description: retorna el inverso aditivo de la matriz M
    :type M: matrix 
    :param M: Matriz escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]
 
    :raises:

    :rtype: matrix - Matriz resultante de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]
    """
    for i in range(len(M)):
        M[i] = inversovector(M[i])
    return M

def multiescalarmatriz(r,M):

    """ Description retorna la multiplicación entre r y M 
    :type r: int / float
    :param r: Escalar que será multiplicado por la matriz

    :type M: matrix 
    :param M: Matriz escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises:

    :rtype: matrix
    """
    for i in range(len(M)):
        M[i] = escalarporvector(r,M[i])
    return M

def transpuestamatriz(M):
    """ Description calcula la matriz transpuesta de M
    :type M: matrix
    :param M: Matriz escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises:

    :rtype: matrix
    """
    trans = []
    if (len(M[0]) == 1):
        for elem in range(len(M)):
            trans.append(M[elem][0])
    else:
        for fil in range(len(M[0])):
            fila = []
            for col in range(len(M)):
                fila.append(M[col][fil])
            trans.append(fila)
    return trans

def transpuestavector(v):

    """ Description Calcula el vector transpuesto de v
    :type v: list
    :param v: Vector escrito de alguna de estas dos formas:
     1. [(1,2),(3,5)...(x,y)]
     2. [[(1,2)],[(3,5)],[(6,5)]...,[(x,y)]]

    :raises:

    :rtype: list / matrix 
    """
    rta = []
    for comp in v:
        if  (type(comp) is tuple):
            rta.append([comp])
        else:
            rta.append(comp[0])
    return rta

def conjugadomatriz(M):

    """ Description: calcula la matriz conjugada de M
    :type M: matrix
    :param M: Matriz escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises:

    :rtype: matrix
    """
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = conjugado(M[i][j])  
    return M

def conjugadovector(v):

    """ Description calcula el vector conjugado de v
    :type v: list / matrix 
    :param v: Vector escrito de alguna de estas dos formas:
     1. [(1,2),(3,5)...(x,y)]
     2. [[(1,2)],[(3,5)],[(6,5)]...,[(x,y)]]

    :raises:

    :rtype: list / matrix
    """
    rta = []
    for comp in v:
        if  (type(comp) is tuple):
            rta.append(conjugado(comp))
        else:
            rta.append([conjugado(comp[0])])
    return rta

def dagamatriz(M):

    """ Description retorna la matriz adjunta de M
    :type M: matrix 
    :param M: Matriz escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises:

    :rtype: matrix
    """
    return conjugadomatriz(transpuestamatriz(M))

def dagavector(v):

    """ Description retorna el vector adjunto de v 
    :type v: list / matrix 
    :param v: Vector escrito de alguna de estas dos formas:
     1. [(1,2),(3,5)...(x,y)]
     2. [[(1,2)],[(3,5)],[(6,5)]...,[(x,y)]]

    :raises:

    :rtype: matrix / list
    """
    return (transpuestavector(conjugadovector(v)))
        
def multimatrices(M,N):

    """ Description: calcula la multiplicación de dos matrices M y N
    :type M: matrix
    :param M: Matriz 1 escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :type N: matrix
    :param N: Matriz 2 escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :raises: Exception en caso de que las matrices tengan tamaños compatibles

    :rtype: matrix
    """
    if (len(M[0]) != len(N)):
        raise Exception("Las matrices no tienen tamaños compatibles")
    else:
        rta = [[(0,0)] * len(N[0]) for j in range(len(M))]
        #print(rta)
        for fila in range(len(M)):
            for col in range(len(N[fila])):
                for it in range(len(rta)):
                    new = multiplicar(M[fila][it],N[it][col])
                    old = rta[fila][col] 
                    rta[fila][col] = (new[0]+old[0], new[1]+old[1])
    return rta
      

def accion(M,v):

    """ Description Calcula la acción de un vector sobre una matriz
    :type M: matrix 
    :param M: Matriz escrita de la forma [[(a,b),(d,c)],[(x,y),(f,g)]]

    :type v: list
    :param v: Vector escrito de la forma [(a,b),(c,d)]

    :raises: exception en caso de que no tengan tamaños compatibles

    :rtype: matrix
    """
    if (len(M[0]) != len(v)):
        raise Exception("El tamaño de la matriz y el vector no son compatibles") 
    else: 
        vector = transpuestavector(v)
        return multimatrices(M,vector)

def productointernovectores(v,w):

    """ Description calcula el producto interno entre dos vectores
    :type v: list 
    :param v: Vector 1 escrito de la forma [(a,b),(c,d)]

    :type w: list 
    :param w: Vector2  escrito de la forma [(a,b),(c,d)]

    :raises: exception en caso que los vectores no tengan tamaños compatibles

    :rtype: tuple
    """
    if (len(v) != len(w)):
        raise Exception("Los vectores no tienen tamaños compatibles")
    else:
        v = dagavector(v)
        rta = []
        aux = 0
        aux1 = 0
        for i in range(len(v)):
            rta.append(multiplicar(v[i][0],w[i]))

        for i in range(len(rta)):
            aux += rta[i][0]
            aux1 += rta[i][1]
        return (aux,aux1)
         
def norma(v):

    """ Description calcula la norma (magnitud) del vector v
    :type v: list
    :param v: Vector escrito de la forma [(a,b),(c,d)]

    :raises:

    :rtype: float
    """
    rta = 0
    for comp in v:
        rta += comp[0]**2 + comp[1]**2
    return round(m.sqrt(rta),2)


def calcdistanciaentrevectores(v,w):

    """ Description calcula la distancia entre dos vectores v y w
    :type v: list
    :param v: Vector 1 escrito de la forma [(a,b),(c,d)]

    :type w: list
    :param w: Vector 2 escrito de la forma [(a,b),(c,d)]

    :raises:

    :rtype: float
    """
    resta = restavectores(v,w)
    return norma(resta)


def matrizIdentidad(M):

    """ Description retoran la matriz identidad de M
    :type M: matrix 
    :param M: Matriz de la forma [[(a,b),(c,d)],[(f,h),(g,l)]]

    :raises:

    :rtype: matrix, matriz identidad [[(1,0),(0,0)],[(0,0),(1,0)]]
    """
    identidad = [[(0,0) for i in range(len(M))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
            if (i==j):
                identidad[i][j]=(1,0)
            else:
                identidad[i][j]=(0,0)
    return identidad
                



def isunitaria(M):

    """ Description Decide si una matriz es unitaria o no, la matriz debe ser cuadrada
    :type M: matrix
    :param M: Matriz de la forma [[(a,b),(c,d)],[(f,h),(g,l)]]
    
    :raises: Exception en caso que la matriz no sea cuadrada

    :rtype: boolean
    """
    if (len(M) != len(M[0])):
        raise Exception("La matriz no es cuadrada")
    
    ident = matrizIdentidad(M)
    return multimatrices(M,dagamatriz(M)) == multimatrices(dagamatriz(M),M) == ident


def ishermitian(M):

    """ Description Decide si una matriz es hermitania o no, la matriz debe ser cuadrada
    :type M:  matrix
    :param M: Matriz de la forma [[(a,b),(c,d)],[(f,h),(g,l)]]
    
    :raises:

    :rtype: boolean
    """
    if (len(M) != len(M[0])):
        raise Exception("La matriz no es cuadrada")

    return M == dagamatriz(M)

def productoTensor(M,N):
    """ Description Calcula el producto tensor de las matrices M y N
    :type M:  matrix
    :param M: Matriz de la forma [[(a,b),(c,d)],[(f,h),(g,l)]]
    
    :type N:  matrix
    :param N: Matriz de la forma [[(a,b),(c,d)],[(f,h),(g,l)]]
    :raises:

    :rtype: matrix
    """
    aux = []
    subLista = []
    conta = len(N)
    for i in M:
        #print(i)
        valorB = 0
        valorA = 0
        while valorA < conta:
            for num1 in i:
                #print("1")
                #print(num1)
                for num2 in N[valorB]:
                    #print("2")
                    #print(num2)
                    subLista.append(multiplicar(num1,num2))
            aux.append(subLista)
            subLista = []
            valorA +=1
            valorB += 1
    for i in range(len(aux)):
        print(*aux[i])
    return aux


#productoTensor([[(0,0),(1,0)],[(1,0),(0,0)]],[[(1/m.sqrt(2),0),(1/m.sqrt(2),0)],[(1/m.sqrt(2),0),(-1/m.sqrt(2),0)]])
#print(multiplicar((0, 0),(0.7071067811865475, 0)))
#print(accion([[(-1,0),(1,1),(0,0)],[(2,-1),(0,0),(1,0)],[(0,0),(1,-1),(0,1)]],[(1,0),(0,1),(1,1)]))
#productoTensor([[(0,1),(1,0)],[(1,1),(2,0)]],[[(1,0),(0,1)]])
#print(multiplicar((1,-3),(2,-1)))
#print(productointernovectores([(0,1/m.sqrt2(2)),(0,1/m.sqrt(2))],[]))
#print(productointernovectores([[(0,1)],[(1,-1)]]))
#print(multimatrices([[(0,1),(-1,1)],[(2,0),(1,0)]],dagamatriz([[(1,0),(-1,0)],[(0,-1),(0,2)]])))
#productoTensor([[(0,0),(1/6,0),(5/6,0)],
       #               [(1/3,0),(1/2,0),(1/6,0)],
        #              [(2/3,0),(1/3,0),(0,0)]],[[(0,0),(1/6,0),(5/6,0)],
         #             [(1/3,0),(1/2,0),(1/6,0)],
          #            [(2/3,0),(1/3,0),(0,0)]])