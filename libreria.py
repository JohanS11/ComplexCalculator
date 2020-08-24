import math as m 
import numpy as np

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
    rtaReal = compA[0] * compB[0] - compA[1] * compB[1]
    rtaImaginaria = compA[1] * compB[0] + compA[0] * compB[1]
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
    if (len(v) != len(w)):
        raise Exception("Los vectores tienen diferentes longitudes no se pueden sumar")
    else:
        rta = []
        for i in range(len(v)):
            rta.append(sumar(v[i],w[i]))
    return rta

def restavectores(v,w):
    if (len(v) != len(w)):
        raise Exception("Los vectores tienen diferentes longitudes no se pueden restar")
    else:
        rta = []
        for i in range(len(v)):
            rta.append(restar(v[i],w[i]))
    return rta

def inversovector(v):
     return escalarporvector(-1,v)

def escalarporvector(r,v):
    for i in range(len(v)):
        v[i] = ((v[i][0] * r, v[i][1] * r))
    return v 

def sumarmatrices(M,N):
    if (len(M) != len(N)):
        raise Exception("Las matrices no se puede sumar porque tienen tamaños distintos")
    else:
        rta = []
        for i in range(len(M)):
            rta.append(sumavectores(M[i],N[i]))
    return rta

def inversomatriz(M):
    for i in range(len(M)):
        M[i] = inversovector(M[i])
    return M

def multiescalarmatriz(r,M):
    for i in range(len(M)):
        M[i] = escalarporvector(r,M[i])
    return M

def transpuestamatriz(M):
    
    trans = []
    for fil in range(len(M[0])):
        fila = []
        for col in range(len(M)):
            fila.append(M[col][fil])
        trans.append(fila)
    return trans

def transpuestavector(v):
    rta = []
    for comp in v:
        if  (type(comp) is tuple):
            rta.append([comp])
        else:
            rta.append(comp[0])
    return rta

def conjugadomatriz(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = conjugado(M[i][j])  
    return M

def conjugadovector(v):
    rta = []
    for comp in v:
        if  (type(comp) is tuple):
            rta.append(conjugado(comp))
        else:
            rta.append([conjugado(comp[0])])
    return rta

def dagamatriz(M):
    return conjugadomatriz(transpuestamatriz(M))

def dagavector(v):
    return (transpuestavector(conjugadovector(v)))
        
def multimatrices(M,N):

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
    if (len(M[0]) != len(v)):
        raise Exception("El tamaño de la matriz y el vector no son compatibles") 
    else: 
        vector = transpuestavector(v)
        return multimatrices(M,vector)

def productointernovectores(v,w):

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
    rta = 0
    for comp in v:
        rta += comp[0]**2 + comp[1]**2
    return round(m.sqrt(rta),2)


def calcdistanciaentrevectores(v,w):

    resta = restavectores(v,w)
    return norma(resta)


