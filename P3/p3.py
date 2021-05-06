import random
import math
import re

#No entiendo muy bien como lo hacen
def contieneGrafo(grafo, registro):
    found=false
    currentReg=0

    stack=[]
    for i in range(len(grafo)):
        if(grafo[i][0]==registro[currentReg][0]:
           stack.append([0,i])

    while stack and not found:
        current=stack.pop()
        currentReg=current[0]
        currentNode=grafo[current[1]]

        currentReg+=1
        if(currentReg is len(registro)):
            found=true
        else:
            dif=registro[currentReg][1] - registro[currentReg-1][1]
            for i in range(len(grafo)):
                if grafo[i][0] is registro[currentReg][0]:
                    if diff in currentNode[1][i]:
                        stack.append([currentReg,i])

    return found
        

def evaluarNodos(registro1, registro2):
    aux=registro1[::2]
    aux2=registro22[::2]


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

def crearGrafo(registro)
    grafo=registro
    l=list(range(len(grafo)))
    aux=l[1::2]
    for i in aux:
        grafo[i]=[-99,99]
    return grafo

def evaluarRestricciones(grafoRest, registro):
    l=list(range(len(grafoRest)))
    aux=l[1::2]
    l2=list(range(len(grafo)))
    aux2=l2[1::2]
    
    ret=1
    while ret!=0:
        for i in aux2:
            print(grafo[i+1])
            for j in aux:
                print(grafoRest[j+1][1])
                if grafoRest[j]==grafo[i]:
                    if grafo[i+1]>=grafoRest[j+1][0]:
                        ret=0            
                        break

    return ret
    
def obtenerVecinos(solucion, datos):
    ##Obtención de los vecinos
    vecinos = []
    l=len(datos)
    for i in range(l):
        valido=evaluarNodos(solucion[0],datos[i])
        if valido:
            vecinos.append(datos[i])

    ##Obtención del mejor vecino
    #mejorVecino = vecinos[0]
    #mejorLongitud = evaluarSolucion(datos, mejorVecino)
    #for vecino in vecinos:
    #    longitud = evaluarSolucion(datos, vecino)
    #    if longitud < mejorLongitud:
    #       mejorLongitud = longitud
    #        mejorVecino = vecino
    return vecinos

def hillClimbing(datos):
    l=len(datos)
    ##Creamos una solucion aleatoria
    registros = list(range(l))
    solucion = []
    #for i in range(l):
    registro = registros[random.randint(0, len(ciudades) - 1)]
    solucion.append(registro)
        #ciudades.remove(ciudad)
    grafo = crearGrafo(registro)

    ##Obtenemos los vecinos 
    vecinos = obtenerVecinos(solucion, datos)
    lvec=len(vecinos)
    for i in range(lvec):
        grafo = mejorarGrafo(grafo,vecinos[i])

    aciertos=0
    for i in range(l):
        valido=contieneGrafo(grafo,datos[i])
        if valido:
            aciertos+=1

    return grafo, aciertos


def ils(inicial, datos):

    iteraciones = 20
    minSol = inicial[0]
    maxAciertos = inicial[1]

    while iteraciones > 0:

        solucion = hillClimbing(datos)
        if solucion[1] > maxAciertos :
            grafo = solucion[0]
            aciertos = solucion[1]
        iteraciones = iteraciones - 1
    return grafo, aciertos
    
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
        for c in range(0,100):
            sol=ils(inicial,datos)
            #resultados.append(sol)
            #suma+=sol[1]
            #if(sol[1]<minDist):
            #    minDist=sol[1]
            #if(sol[1]>maxDist):
            #    maxDist=sol[1]

        #aciertos=distancias.count(minDist)
        resultados.append([i,sol[0], sol[1]])
        i+=1
    with open("Grafos.csv", "w") as file:
        file.write(",".join(["N", "Grafo","Aciertos"]))
        for res in resultados:
                   file.write(",".join(str(e) for e in res)+"\n")







if __name__ == "__main__":
    main()


