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