import random
import math

def generador(nCiudades):
    tsp = []
    for i in range(nCiudades):
        distancias = []
        for j in range(nCiudades):
            if j == i:
                distancias.append(0)
            elif j < i:
                distancias.append(tsp[j][i])
            else:
                distancias.append(random.randint(10, 1000))
        tsp.append(distancias)
    return tsp

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

def simAnnealingLog(datos,t0):
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
        t=(0.99*t0)/math.log(it+1)
        #print("Longitud de la ruta: ", longitud)
        #print("Temperatura: ", t)
    return solucion, longitud

def simAnnealingGeo(datos,t0):
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
        t=(0.99**it)*t0
        #print("Longitud de la ruta: ", longitud)
        #print("Temperatura: ", t)
    return solucion, longitud

def simAnnealingCauchy(datos,t0):
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
        t=t0/(1+it)
        #print("Longitud de la ruta: ", longitud)
        #print("Temperatura: ", t)
    return solucion, longitud

def main():
    datos=generador(10)
    results=[]
    t0=10
    
    distances=[]
    Logdistances=[]
    Geodistances=[]
    Cauchydistances=[]
    bestDist=math.inf
    
    for c in range(0,101):
        s=simAnnealing(datos,t0)
        s0=simAnnealingLog(datos,t0)
        s1=simAnnealingGeo(datos,t0)
        s2=simAnnealingCauchy(datos,t0)
        distances.append(s[1])
        Logdistances.append(s0[1])
        Geodistances.append(s1[1])
        Cauchydistances.append(s2[1])
        if(s[1]<bestDist):
            bestDist=s[1]
        if(s0[1]<bestDist):
            bestDist=s0[1]
        if(s1[1]<bestDist):
            bestDist=s1[1]
        if(s2[1]<bestDist):
            bestDist=s2[1]
        
    optimalOcurr=distances.count(bestDist)
    optimalOcurrLog=Logdistances.count(bestDist)
    optimalOcurrGeo=Geodistances.count(bestDist)
    results.append([i,optimalOcurr, optimalOcurr/100,optimalOcurrLog, optimalOcurrLog/100,optimalOcurrGeo, optimalOcurrGeo/100,optimalOcurrCauchy, optimalOcurrCauchy/100])
        
    with open("SimAnnealingComp.csv", "w") as file:
        file.write(",".join(["N", "opt ocurr", "opt aver","Log opt ocurr","Log opt aver", "Geo opt ocurr","Geo opt aver", "Cauchy opt ocurr","Cauchy opt aver"])+"\n")
    for res in results:
        file.write(",".join(str(e) for e in res)+"\n")
    #print("--------------")
    #print("Solucion final: ",s[0])
    #print("Longitud de la ruta final: ",s[1])

if __name__ == "__main__":
    main()
