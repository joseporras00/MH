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

def aplicarOperadoresGeneticos(poblacion, k, cProb, mProb):

    #Seleccionar padres mediante torneo tamaño k    
    datos1=[]
    datos2=[]
    for i in k:
        datos1.append(random.rand(0,len(poblacion)-1))
        datos2.append(random.rand(0,len(poblacion)-1))
    
    temp1=0
    for n in datos1:
        if poblacion[n]>temp1:
            temp1=n

    temp2=0
        for n in datos2:
        if poblacion[n]>temp2:
            temp2=n
    
    #Cruzar padres con probabilidad cProb
    if random.randint(0,1) <= cProb:
        aux1=poblacion[temp1]
        aux2=poblacion[temp2]
        l1=len(aux1)
        l2=len(aux2)
        poblacion[temp1]=aux1[0:l1/2]+aux2[l1/2:l2]
        poblacion[temp2]=aux2[0:l2/2]+aux1[l2/2:l1]

    #Mutar padres con probabilidad mProb
    if random.randint(0,1) <= mProb:
        aux1=poblacion[temp1]
        aux2=poblacion[temp2]
        p1=random.rand(0,l1-1)
        p2=random.rand(0,l2-1)
        if aux1[p]==0:
            aux1[p]=1
        else:
            aux1[p]=0

        if aux2[p]==0:
            aux2[p]=1
        else:
            aux2[p]=0

        poblacion[temp1]=aux1
        poblacion[temp2]=aux2    
        


    return poblacion #Devolver la nueva poblacion (sin evaluar)

def main():
    pesos = [ 34, 45, 14, 76, 32 ]
    precios = [ 340, 210, 87, 533, 112 ]
    pesoMax = 100 #Peso máximo que se puede poner en la mochila
    nSoluciones = 25 #Tamaño de la poblacion
    maxGeneraciones = 1 #Numero de generaciones
    k = 3 #Tamaño torneo selector de padres
    cProb = 0.5 #Probabilidad de cruce
    mProb = 0.1 #Probabilidad de mutacion

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
                objetos.remove(objeto)

        s = []
        for i in range(l):
            s.append(0)
        for i in solucion:
            s[i] = 1
        poblacion.append([s,evaluarSolucion(s,precios,pesos,pesoMax)])

    it=1
    while it < maxGeneraciones:
        nSoluciones = aplicarOperadoresGeneticos(poblacion,k,cProb,mProb)
        #Modelo generacional
        poblacion = []
        for solucion in nSoluciones:
            poblacion.append([solucion[0],evaluarSolucion(solucion[0],precios,pesos,pesoMax)])
        it+=1

if __name__ == "__main__":
    main()
