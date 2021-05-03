import re

datos = []
with open("BD.txt") as f:
    lineas=[linea.strip("\n") for linea in f.readlines()]
    for linea in lineas:
        datos.append(re.split(r":| ",linea))



print(datos[2])
    
