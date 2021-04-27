def main():
    elite=[]
    datos=[]

    with open("BD.txt") as f:
        lineas=[linea.strip("\n") for linea in f.readlines()]
        for linea in lineas:
            datos.append(linea.split(sep=":"))
    print(datos[2])

    


        
    

if __name__ == "__main__":
    main()
