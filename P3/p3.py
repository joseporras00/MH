import random
import math
import re

def evaluarNodos(grafo1, grafo2):
    aux2=datos[1][::2]
    aux=datos[2][::2]

    print(aux)
    print(aux2)


    l=len(aux)
    l2=len(aux2)
    contador=0
    for i in range(l):
        for j in range(l2):
            if aux[i]==aux2[j]:
                contador=contador+1
                break

    if contador==l:
        return true
    else:
        return false

def crearGrafoRestriccion(grafo)
    aux=[]
    for i in range(len(grafo1)):
        aux.append(i)
        i=i+2
    for i in range(len(grafo1)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud

def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud

def obtenerMejorVecino(solucion, datos):
    ##Obtención de los vecinos
    vecinos = []
    l=len(solucion)
    for i in range(l):
        for j in range(i+1, l):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    ##Obtención del mejor vecino
    mejorVecino = vecinos[0]
    mejorLongitud = evaluarSolucion(datos, mejorVecino)
    for vecino in vecinos:
        longitud = evaluarSolucion(datos, vecino)
        if longitud < mejorLongitud:
            mejorLongitud = longitud
            mejorVecino = vecino
    return mejorVecino, mejorLongitud

def hillClimbing(datos):
    l=len(datos)
    ##Creamos una solucion aleatoria
    ciudades = list(range(l))
    solucion = []
    for i in range(l):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        solucion.append(ciudad)
        ciudades.remove(ciudad)
    longitud = evaluarSolucion(datos, solucion)

    ##Obtenemos el mejor vecino hasta que no haya vecinos mejores
    vecino = obtenerMejorVecino(solucion, datos)
    while vecino[1] < longitud:
        solucion = vecino[0]
        longitud = vecino[1]
        vecino = obtenerMejorVecino(solucion, datos)

    return solucion, longitud

def iterated(datos):
    l=len(datos)
    minLong=99999999
    ciudades=list(range(l))
    solucion=[]
    for i in range(l):
        x=random.randint(0,len(ciudades) - 1)
        ciudad=ciudades[x]
        ciudades.remove(ciudad)
    longitud=evaluarSolucion(datos,solucion)

    vecino=obtenerMejorVecino(solucion,datos)
    contador=1
    while vecino[1] < longitud:
        solucion=vecino[0]
        longitud=vecino[1]
        vecino=obtenerMejorVecino(solucion,datos)
        contador=contador+1

    while contador + 2< (len(datos)-1):
        aux=contador
        aux1=0
        newSolucion=[]

        for i in range(1):
            if aux <(len(datos)-1):
                newSolucion.append(solucion[aux])
                aux=aux+1
            else:
                newSolucion.append(solucion[aux1])
                aux1=aux1+1

        auxLong=evaluarSolucion(datos,newSolucion)

        if auxLong < minLong:
            auxVecino=obtenerMejorVecino(newSolucion,datos)
            contaodr=contaodr+2
            while auxVecino[1]<auxLong:
                newSolucion=auxVecino[0]
                auxLong=auxVecino[1]
                auxVecino=obtenerMejorVecino(newSolucion,datos)
                contaodr=contador+1
            minLong=auxLong

    if minLong < longitud:
        return newSolucion, auxLongitud
    else:
        return solucion, longitud


def mejorado(datos):
    iteraciones=20
    result=[]
    for i in range(1,10):
        distancia=[]
        bestDist=math.inf
        worstDist=0
        sumDist=0
        for j in range(iteraciones):
            s=iterated(datos)
            distancia.append(s[1])
            sumDist+=s[1]
            if s[1] < bestDist:
                bestDist=s[1]
            elif s[1] > worstDist:
                worstDist=s[1]

        optimalOcurr=distances.count(bestDist)
        results.append([i,bestDist,worstDist,sumDist/iteraciones,optimalOcurr/iteraciones])
        for res in results:
            print(",".join([str(s) for s in res]) + "\n")

def ils(inicial, datos):

    iteraciones = 20
    minSol = inicial[0]
    minLong = inicial[1]

    while iteraciones > 0:

        solucion = hillClimbing(datos)
        if solucion[1] < minLong :
            minSol = solucion[0]
            minLong = solucion[1]
        iteraciones = iteraciones - 1
    return minSol, minLong
    
def main():

    datos = []
    with open("BD.txt") as f:
        lineas=[linea.strip("\n") for linea in f.readlines()]
        for linea in lineas:
            datos.append(re.split(r":| ",linea))

    aux=datos
    inicial=hillClimbing(datos)
    resultados=[]
    
    for i in range(0,10):
        print(i,"\n")
        distancias=[]
        minDist=math.inf
        maxDist=0
        suma=0
        for c in range(0,100):
            sol=ils(inicial,datos)
            distancias.append(sol[1])
            suma+=sol[1]
            if(sol[1]<minDist):
                minDist=sol[1]
            if(sol[1]>maxDist):
                maxDist=sol[1]

        aciertos=distancias.count(minDist)
        resultados.append([i,sol, aciertos])
        i+=1
    with open("Grafos.csv", "w") as file:
        file.write(",".join(["N", "Grafo","Aciertos"]))
        for res in resultados:
                   file.write(",".join(str(e) for e in res)+"\n")







if __name__ == "__main__":
    main()


