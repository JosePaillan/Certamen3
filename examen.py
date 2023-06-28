import os
os.system("CLS")

menu="""
1. Registrar producto
2. Buscar producto
3. Listar productos
4. salir
Digite opcion:
"""

codnumerico = []
nombre = []
categoria = []
precio = []
cantidadstock = []

nombre2 = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")

def registrare():
    while True:
        try:
            cod = int(input("Ingrese codigo numerico de 6 digitos: "))
            if cod >= 100000 and cod < 1000000:
                codnumerico.append(cod)
                print(codnumerico)
                break
            else:
                print("Intente nuevamente")
        except:
            print("Error excepcion")
    while True:
        try:
            nom = input("Ingrese el nombre del producto: ")
            if len(nom) >= 2 and len(nom) <= 50:
                nombre.append(nom)
                print(nombre)
                break
            else:
                print("Intente nuevamente")
        except:
            print("Error excepcion")
    while True:
        try:
            cat = input("Ingrese su forma de encomienda paquete o sobre: ")
            if cat == "paquete" or cat == "sobre":
                categoria.append(cat)
                print(categoria)
                break
            else:
                print("Categoria invalida, Intente nuevamente")
        except:
            print("Error excepcion")
    while True:
        try:
            pre = int(input("Ingrese el precio: "))
            if pre > 0:
                precio.append(pre)
                print(precio)
                break
            else:
                print("Intente nuevamente")
        except:
            print("Error excepcion")
    while True:
        try:
            stock = int(input("Ingrese la cantidad stock del producto: "))
            if stock > 0:
                cantidadstock.append(stock)
                print(cantidadstock)
                break
            else:
                print("Intente nuevamente")
        except:
            print("Error excepcion")

def buscare():
    buscar = int(input("Ingrese codigo numerico de 6 digitos a buscar: "))
    print(f" codigo numerico a buscar: {buscar} \n")
    print("| CODIGO NUMERICO | NOMBRE | CATEGORIA | PRECIO | CANTIDAD STOCK |")
    print("--+--------+----------------------+------------+----+-------------")
    for i in range(len(codnumerico)):
        if buscar == codnumerico[i] and buscar >= 100000 and buscar < 1000000:
            print(f"| {codnumerico[i]:12d} | {nombre[i]:10s} | {categoria[i]:8s} | {precio[i]:6d} | {cantidadstock[i]:6d}")
            print("--+--------+----------------------+------------+----+------------------")

def listare():
    print("| CODIGO NUMERICO | NOMBRE | CATEGORIA | PRECIO | CANTIDAD STOCK | STOCK |")
    print("--+--------+----------------------+------------+----+-------------")
    conts  = 0
    for i in range(len(codnumerico)):
        if cantidadstock[i] < 5:
            s = "STOCK BAJO"
            conts += 1
        else:
            s = "STOCK ALTO"
        print(f"| {codnumerico[i]:12d} | {nombre[i]:10s} | {categoria[i]:8s} | {precio[i]:6d} | {cantidadstock[i]:14d} | {s} |")
        print("--+--------+----------------------+------------+----+---------------------")  
        print(f"CANTIDAD DE STOCK BAJOS: {conts}")      
while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            input(f"""Gracias {nombre2} {apellido} por su compra o visita a nuestro nuevo sistema
                     Version sistema 1.0""")
            break
        elif opc == 1:
           registrare()
        elif opc == 2:
            buscare()
        elif opc == 3:
            listare()
    except:
        print("Error Excepcion")