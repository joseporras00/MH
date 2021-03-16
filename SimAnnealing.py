import random
import math
import TSPGenerator

def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud

def obtenerVecino(solucion, datos):
    ##Obtención de los vecinos
    vecinos = []
    l=len(solucion)
    for i in range(l):
        for j in range(i+1, l):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    ##Obtengo un vecino aleatorio
    vecino=vecinos[random.randint(0, len(vecinos) - 1)]
    longitud = evaluarSolucion(datos, vecino)

    return vecino, longitud

def simAnnealing(datos,t0):
    t=t0
    l=len(datos)
    ##Creamos una solucion aleatoria
    ciudades = list(range(l))
    solucion = []
    for i in range(l):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        solucion.append(ciudad)
        ciudades.remove(ciudad)
    longitud = evaluarSolucion(datos, solucion)
    #print("Longitud de la ruta: ", longitud)
    #print("Temperatura: ", t)

    it=0
    while t > 0.05:
        ##Obtenemos un vecino al azar
        vecino = obtenerVecino(solucion, datos)
        incremento = vecino[1]-longitud

        if incremento < 0:
            longitud = vecino[1]
            solucion = vecino[0]
        elif random.random() < math.exp(-abs(incremento) / t):
            longitud = vecino[1]
            solucion = vecino[0]

        it+=1
        t=0.99*t
        #print("Longitud de la ruta: ", longitud)
        #print("Temperatura: ", t)
    return solucion, longitud

def main():
    datos=TSPGenerator.generador(10)
    results=[]
    t0=10
    for i in range(0,10)
    
        distances=[]
        bestDist=math.inf
        worstDist=0
        sumDist=0
        for c in range(0,101):
            s=simAnnealing(datos,t0)
            distances.append(s[1])
            sumDist+=s[1]
            if(s[1]<bestDist):
                bestDist=s[1]
            if(s[1]>worstDist):
                worstDist=s[1]

        optimalOcurr=distances.count(bestDist)
        results.append([i,bestDist, worstDist, sumDist/100,optimalOcurr, optimalOcurr/100])
        i+=5
    with open("SimAnnealingResults.csv", "w") as file:
        file.write(",".join(["N","best Dist", "worst Dist", "media dist", "opt ocurr", "opt aver"])
        for res in results:
                   file.write(",".join(str(e) for e in res])+"\n")
        #print("--------------")
        #print("Solucion final: ",s[0])
        #print("Longitud de la ruta final: ",s[1])

if __name__ == "__main__":
    main()
