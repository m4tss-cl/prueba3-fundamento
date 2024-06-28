import csv
from funciones import agregarproductos, leerinventario, clasificar

op = 0
while op != 4:
    print("Bienvenido al Sistema de Gestión de Inventario")
    print("Seleccione una opción:")
    print("""1. Agregar producto al inventario
2. Leer el inventario
3. Clasificar productos y generar archivo de texto
4. Salir""")
    op = int(input("Seleccione opcion: "))

    if op == 1:
        agregarproductos()
    elif op ==2:
        leerinventario()
    elif op ==3:
        clasificar()
    elif op==4:
        print("Adios")