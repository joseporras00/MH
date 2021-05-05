import re

datos = []
with open("BD.txt") as f:
    lineas=[linea.strip("\n") for linea in f.readlines()]
    for linea in lineas:
        datos.append(re.split(r":| ",linea))



    
aux2=datos[1][::2]
aux=datos[2][::2]

print(aux)
print(aux2)


l=len(aux)
l2=len(aux2)
contador=0
for i in range(l):
    print(contador)
    for j in range(l2):
        #print(j,aux2[j])
        if aux[i]==aux2[j]:
            contador=contador+1
            break


print(aux)

#for j in range(l2):
        #if aux[i]==aux2[j]:
            #aux.pop(i)
