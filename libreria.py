import math as m 

def sumar(compA,compB):
    rtaReal = float(compA[0]+compB[0])
    rtaImag = float(compA[1]+compB[1])
    resultado = (rtaReal,rtaImag)
    return resultado

def restar(compA,compB):
    rtaReal = float(compA[0]-compB[0])
    rtaImag = float(compA[1]-compB[1])
    resultado = (rtaReal,rtaImag)
    return resultado

def multiplicar(compA,compB):
    rtaReal = compA[0] * compB[0] - compA[1] * compB[1]
    rtaImaginaria = compA[1] * compB[0] + compA[0] * compB[1]
    resultado = (rtaReal,rtaImaginaria)
    return resultado

def division(compA,compB):
    numerador1 = compA[0] * compB[0] + compA[1] * compB[1]
    denominador = compB[0] ** 2 + compB[1] ** 2
    numerador2 = compA[1] * compB[0] - compA[0] * compB[1]
    resultado = (float(numerador1/denominador),float(numerador2/denominador))
    return resultado    

def modulo(comp):
    resultado = float(m.sqrt((comp[0])**2+(comp[1])**2))
    return resultado    

def conjugado(comp):
    return (comp[0],comp[1] * -1)

def topolar(comp):
    
    mod = modulo(comp)
    tetha = m.atan(comp[1]/comp[0])
    return (round((mod),2),round((tetha),2))

def tocartesian(r,tetha):
    x = round(r * m.cos(tetha),2)
    y = round(r * m.sin(tetha),2)
    return (x,y)

def fase(comp):
    resultado = m.atan(comp[1]/comp[0])
    return round(resultado,2)