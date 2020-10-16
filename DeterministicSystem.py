import libreria as lib, math as m

def calcState(M,v,t):

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
    
    rta = lib.multimatrices(tempM,v)

    return rta
    
def calcObservable(v,x):
    return (lib.modulo(v[x])**2/lib.norma(v)**2)

'''
print(calcObservable([(m.sqrt(5)/m.sqrt(30),2/m.sqrt(30)),
                      (-2/m.sqrt(30),-m.sqrt(5)/m.sqrt(30)),
                      (0,m.sqrt(2/5))],1))
print(calcObservable([(m.sqrt(5)/m.sqrt(30),2/m.sqrt(30)),
                      (-2/m.sqrt(30),-m.sqrt(5)/m.sqrt(30)),
                      (0,m.sqrt(2/5))],0)) 
print(calcObservable([(m.sqrt(5)/m.sqrt(30),2/m.sqrt(30)),
                      (-2/m.sqrt(30),-m.sqrt(5)/m.sqrt(30)),
                      (0,m.sqrt(2/5))],2))     
'''

def valorpromedio(omega, ket):
    
    """ Description Calcula el valor promedio de omega en un Ket dado
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

    promedio = valorpromedio(omega,ket)
    identidad = lib.matrizIdentidad(omega)
    res = lib.multiescalarmatriz(promedio,identidad)
    return lib.restarmatrices(omega,res)


def varianza(omega,ket): 
    if (not lib.ishermitian(omega)):
        raise Exception("Omega debe ser hemitiana")
    delta1 = delta(omega,ket)
    rta = lib.multimatrices(delta1,delta1)
    return valorpromedio(rta,ket)


print("promedio")
print(valorpromedio([[(1,0),(0,-1)],
                [(0,1),(2,0)]],
                [[(m.sqrt(2)/2,0)],
                [(0,m.sqrt(2)/2)]]))

print("varianza")
print(varianza([[(1,0),(0,-1)],
                [(0,1),(2,0)]],
                [[(m.sqrt(2)/2,0)],
                [(0,m.sqrt(2)/2)]]))
def amplitudTransicion(v1,v2):
    #for i in range(len(v2)):
     #   v2[i] = lib.conjugado(v2[i])

    normav1 = lib.norma(v1)
    normav2 = lib.norma(v2)
    rta = normav1 * normav2
    return lib.division(lib.productointernovectores(v1,v2),(rta,0))


    
"""
print("PUNTO 9 ")    
print(calcObservable([(-0.4999999999999999, 0.4999999999999999),(0.4999999999999999, 0.4999999999999999),(0,0)],0))
calcState([[(1/m.sqrt(2),0),(0,1/m.sqrt(2)),(0,0)],
           [(1/m.sqrt(2),0),(0,-1/m.sqrt(2)),(0,0)],
           [(0,0),(0,0),(0,-1)]],
           [[(0,1)],
           [(0,0)],
           [(0,0)]],2)

print("holaa")


calcState([[(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
           [(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
           [(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)],
           [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
           [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
           [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)]],
           [[(4,0)],
           [(1,0)],
           [(5,0)],
           [(3,0)],
           [(10,2)],
           [(2,0)]],3)

####ESTADO OBSERVABLES####
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],0))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],1))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],2))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],3))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],4))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],5))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],6))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],7))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],8))
print(calcObservable([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],9))


### AMPLITUD DE TRANSICION DE PSY A FI ##
#print(lib.productointernovectores([(0,m.sqrt(2)/2),(-m.sqrt(2)/2,0)],[(m.sqrt(2)/2,0),(0,-m.sqrt(2)/2)]))
#print(amplitudTransi([(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)],
 #                               [(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]))

print("")
print(lib.productointernovectores([(1,0),(0,0),(0,0),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)],
                               [(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]))                             
#print(productopunto([(2,-1),(-1,-2),(0,-1),(1,0),(3,1),(2,0),(0,2),(-2,-1),(1,3),(0,1)],
#                                [(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]))

#print(lib.norma([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]))
#print(lib.modulo((-2,1))**2/(6.78)**2)

##varianza##
print("varianza")
print(varianza([ [(0,0),(0,-1)],
                 [(0,1),(0,0)]],
                 [(1/m.sqrt(2),0),(0,1/m.sqrt(2))]))

###DINAMICA MATRIZ###

calcState([      [(0,0),(0,0),(1/18,0),(2/18,0),(5/18,0),(10/18,0)],
                 [(0,0),(0,0),(2/18,0),(1/18,0),(10/18,0),(5/18,0)],
                 [(1/9,0),(2/9,0),(1/6,0),(2/6,0),(1/18,0),(2/18,0)],
                 [(2/9,0),(1/9,0),(2/6,0),(1/6,0),(2/18,0),(1/18,0)],
                 [(2/9,0),(4/9,0),(1/9,0),(2/9,0),(0,0),(0,0)],
                 [(4/9,0),(2/9,0),(2/9,0),(1/9,0),(0,0),(0,0)]],
                 [[(1/2000,0)],
                 [(9/1000,0)],
                 [(0.045,0)],
                 [(0.855,0)],
                 [(9/2000,0)],
                 [(0.0855,0)]]
                ,20)

"""
"""
calcState([      [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(-1/m.sqrt(6),1/m.sqrt(6)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(-1/m.sqrt(6),-1/m.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                 [(0,0),(1/m.sqrt(6),-1/m.sqrt(6)),(-1/m.sqrt(6),1/m.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0)],
                 [(0,0),(0,0),(-1/m.sqrt(6),-1/m.sqrt(6)),(0,0),(0,0),(0,0),(1,0),(0,0)],
                 [(0,0),(0,0),(1/m.sqrt(6),-1/m.sqrt(6)),(0,0),(0,0),(0,0),(0,0),(1,0)]],
                 [[(1,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)]],2)         


calcState([      [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(1/2,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                 [(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(1/3,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                 [(0,0),(1/3,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
                 [(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
                 [(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(1,0)]],
                 [[(1,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)]],4)


calcState([      [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
                 [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
                 [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],
                 [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
                 [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
                 [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)]],
                 [[(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(0,0)],
                 [(1,0)]],2019)

calcState([      [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
   [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],
   [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
    [(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
    [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0)]],
    [[(6,0)],
    [(0,0)],
    [(3,0)],
    [(5,0)],
    [(3,0)],
    [(8,0)]],5000)
"""



