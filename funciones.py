import csv

def agregarproductos():
    salir = False
    with open ("inventario.csv", "a", newline="") as archivocsv: #abrir archivo csv
        escribir = csv.writer(archivocsv)
        escribir.writerow(["ID", "Nombre", "Categoria", "Precio"])
    while salir == False:
        id = int(input("Ingrese la ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        categoria_valida = ["electronica", "textil", "calzado"]
        categoria = ""
        while categoria not in categoria_valida: #si la categoria ingresada no esta en la lista categoria_valida, pregunta de nuevo
            categoria = input("Ingrese la categoria (electronica, textil, calzado)")
        precio= int(input("Ingrese el precio del producto: "))

        with open ("inventario.csv", "a", newline="") as archivocsv:
            escribir = csv.writer(archivocsv)
            escribir.writerow([id,nombre,categoria,precio])
        salir = input("Desea procesar otro producto? (si/no)")
        salir = salir.lower()
        if salir == "si":
            salir = False
        else:
            salir = True



def leerinventario():
    with open ("inventario.csv", "r", newline="") as archivocsv:
        leer = csv.reader(archivocsv)
        for fila in leer:
            print(fila)

def clasificar():
    with open ("inventario.csv", "r", newline="") as archivocsv:
        leer = csv.reader(archivocsv)
        electronica = []
        textil = []
        calzado = []
        for categoria in leer: #revisa la palabra en el indice 2 y si esta entre las categorias validas la agrega a listas separadas
            if categoria[2] == "electronica":
                electronica.append(categoria)
            elif categoria[2] == "textil":
                textil.append(categoria)
            elif categoria[2] == "calzado":
                calzado.append(categoria)
    with open ("clasificacion_productos.txt", "w", newline="") as archivo:
        archivo.write("electronica: ")
        for elemento in electronica:
            archivo.write(str(elemento))
        archivo.write("\ntextil: ")
        for elemento in textil:
            archivo.write(str(elemento))
        archivo.write("\ncalzado: ")
        for elemento in calzado:
            archivo.write(str(elemento))     
    print("Archivo generado")      
