def linea_mas_larga(datos):
    lmaslarga = datos[0]
    for linea in datos:
        if len(linea) > len(lmaslarga):
            lmaslarga = linea
    if len(lmaslarga)>=4:
        return lmaslarga

def main():
    elite=[]
    datos=[]

    with open("BD.txt") as f:
        lineas=[linea.strip("\n") for linea in f.readlines()]
        for linea in lineas:
            datos.append(linea.split(sep=":"))
    print(datos[2])

    grafo1=linea_mas_larga(datos)
    print(grafo1)

    


        
    

if __name__ == "__main__":
    main()
