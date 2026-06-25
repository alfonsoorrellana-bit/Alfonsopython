# # ejemplo de manipulacion de datos en una lista
# listado=[3, 6.5, 4, 5,["Link", "Zelda"], {"pkm":"weeddle"}]
# #        0   1   2  3        4                  5

# print(listado[5]["pkm"])# muestra weeddle, por que es el valor del key "pkm"

# for e in listado:
#     print(e)

# listado.append({"dia": "lunes", "temp": 25.7, "humedad":29})
# print("-"*50)
# input()
# for e in listado:
#     print(e)

# # ejemplo de return

# def suma():
#     return 5+7

# print(suma()*4)

# def calculaIVA(neto):
#     return neto*1.19

# print("El valor a pagar sera:" , calculaIVA(2000))


# def verificarNumero():
#     while True:
#         try:
#             num=int(input("Ingrese un numero: "))
#             if num<0:
#                 print("debe ingresar un numero mayor o igual a 0")
#             else:
#                 return num
#         except Exception as e:
#             print("Solo numero enteros positivos")
print 

pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"}, #3
]
def mostrarPinturas():
    if not pinturas:
        print("No hay pinturas para mostrar")
        return

    for indice, pintura in enumerate(pinturas, start=1):
        print(
            f"{indice}.- color: {pintura['color']}, capacidad: {pintura['capacidad']} ml, formato: {pintura['formato']}"
        )


def pedirIndice(mensaje):
    while True:
        try:
            ele = int(input(mensaje))
            if 1 <= ele <= len(pinturas):
                return ele - 1
            print("Numero fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un numero entero.")


def quitarPintura():
    if not pinturas:
        print("No hay pinturas para eliminar.")
        return

    mostrarPinturas()
    indice = pedirIndice("Que pintura va a eliminar?: ")
    eliminada = pinturas.pop(indice)
    print(f"Se elimino la pintura color {eliminada['color']}.")


def agregarPintura():
    color = input("Que color sera?: ")
    capacidad = int(input("Que capacidad sera?: "))
    formato = input("Que formato sera?: ")
    pinturas.append({"color": color, "capacidad": capacidad, "formato": formato})
    print("Pintura agregada correctamente.")


def actualizarPintura():
    if not pinturas:
        print("No hay pinturas para actualizar.")
        return

    mostrarPinturas()
    indice = pedirIndice("Que pintura va a actualizar?: ")
    print("1.- Color")
    print("2.- Capacidad")
    print("3.- Formato")

    dato = int(input("Que dato de la pintura va a actualizar?: "))
    if dato == 1:
        nuevo_valor = input("Ingrese el nuevo color: ")
        pinturas[indice]["color"] = nuevo_valor
    elif dato == 2:
        nuevo_valor = int(input("Ingrese la nueva capacidad: "))
        pinturas[indice]["capacidad"] = nuevo_valor
    elif dato == 3:
        nuevo_valor = input("Ingrese el nuevo formato: ")
        pinturas[indice]["formato"] = nuevo_valor
    else:
        print("Dato invalido")
        return

    print("Pintura actualizada correctamente.")


def mayorCap(lista):
    if not lista:
        return 0
    return max(p["capacidad"] for p in lista)


def buscarColor(lista, color_buscado):
    for pintura in lista:
        if pintura.get("color") == color_buscado:
            return "disponible"
    return "no existe"


def menuPinturas():
    while True:
        try:
            print("-" * 60)
            print("1.- Agregar Pintura")
            print("2.- Quitar Pintura")
            print("3.- Actualizar Pintura")
            print("4.- Mostrar Pinturas")
            print("5.- Mostrar mayor capacidad")
            print("9.- Salir")
            op = int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregarPintura()
                case 2:
                    quitarPintura()
                case 3:
                    actualizarPintura()
                case 4:
                    mostrarPinturas()
                case 5:
                    print(
                        f"El recipiente con mayor capacidad tiene: {mayorCap(pinturas)} ml"
                    )
                case 9:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion invalida")
        except ValueError:
            print("Debe ingresar un numero valido.")
        except Exception as e:
            print("Error: ", e)


if __name__ == "__main__":
    menuPinturas()
