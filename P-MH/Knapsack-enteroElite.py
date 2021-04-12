import random

def evaluarSolucion(solucion, precios, pesos, pesoMax):
    precio = 0
    peso = 0
    for i in range(len(solucion)):
        precio += precios[i]*solucion[i]
        peso += pesos[i]*solucion[i]

    if peso > pesoMax:
        return 0
    else:
        return precio

def aplicarOperadoresGeneticos(elite,poblacion, k, cProb, mProb):

    #elite
    minimo=999999
    posicion=0
    for i in range(len(poblacion)):
        if poblacion[i][1]<minimo:
            minimo=poblacion[i][1]
            posicion=i

    poblacion[posicion]=elite

    #Seleccionar padres mediante torneo tamaño k    
    datos1=[]
    datos2=[]
    for i in range(k):
        datos1.append(random.randint(0,len(poblacion)-1))
        datos2.append(random.randint(0,len(poblacion)-1))
    
    temp1=0
    for n in datos1:
        if poblacion[n][1]>temp1:
            temp1=n

    temp2=0
    for n in datos2:
        if poblacion[n][1]>temp2:
            temp2=n
    
    #Cruzar padres con probabilidad cProb
    if random.randint(0,100) <= cProb:
        if temp1 != temp2:
            aux1=poblacion[temp1][0]
            aux2=poblacion[temp2][0]
            l1=len(aux1)
            threshold=random.randint(1,l1-1)
            t1=aux1[threshold:]
            t2=aux2[threshold:]
            poblacion[temp1][0]=aux1[:threshold]
            poblacion[temp2][0]=aux2[:threshold]
            poblacion[temp1][0].extend(t2)
            poblacion[temp2][0].extend(t1)

    #Mutar padres con probabilidad mProb
    if random.randint(0,100) <= mProb:
        aux1=poblacion[temp1][0]
        aux2=poblacion[temp2][0]
        l1=len(aux1)
        p1=random.randint(0,l1-1)
        p2=random.randint(0,l1-1)

        aux1[p1]=random.randint(0,l1-1)
        aux2[p2]=random.randint(0,l1-1)

        poblacion[temp1][0]=aux1
        poblacion[temp2][0]=aux2    

    max=0
    for i in range(len(poblacion)):
        if max<poblacion[i][1]:
            elite=poblacion[i]

    return poblacion,elite #Devolver la nueva poblacion (sin evaluar)

def main():
    elite=0
    pesos = [ 34, 45, 14, 76, 32 ]
    precios = [ 340, 210, 87, 533, 112 ]
    pesoMax = 110 #Peso máximo que se puede poner en la mochila
    nSoluciones = 50 #Tamaño de la poblacion
    maxGeneraciones = 20 #Numero de generaciones
    k = 3 #Tamaño torneo selector de padres
    cProb = 20 #Probabilidad de cruce
    mProb = 20 #Probabilidad de mutacion
    results=[]

    l=len(pesos)
    ##Creamos n soluciones aleatorias que sean válidas
    poblacion = []
    for i in range(nSoluciones):
        objetos = list(range(l))
        solucion = []
        peso = 0
        while peso < pesoMax:
            objeto = objetos[random.randint(0, len(objetos) - 1)]
            peso += pesos[objeto]
            if peso <= pesoMax:
                solucion.append(objeto)

        s = []
        for i in range(l):
            s.append(0)
        for i in solucion:
            s[i] +=1

        poblacion.append([s,evaluarSolucion(s,precios,pesos,pesoMax)])

    max=0
    for i in range(len(poblacion)):
        if max<poblacion[i][1]:
            elite=poblacion[i]

    with open("IntElite.csv", "w") as file:
        file.write(",".join(["Gen 1"])+"\n")
        for res in poblacion:
            file.write(",".join(str(e) for e in res)+"\n")
    it=1
    while it < maxGeneraciones:
        nSoluciones,elite = aplicarOperadoresGeneticos(elite,poblacion,k,cProb,mProb)
        #Modelo generacional
        poblacion = []
        for solucion in nSoluciones:
            poblacion.append([solucion[0],evaluarSolucion(solucion[0],precios,pesos,pesoMax)])
        with open("IntElite.csv", "a") as file:
                file.write(",".join(["Next Gen"])+"\n")
                for res in poblacion:
                    file.write(",".join(str(e) for e in res)+"\n")
        it+=1

        
    

if __name__ == "__main__":
    main()
