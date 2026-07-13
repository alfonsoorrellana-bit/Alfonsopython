peliculas = {
    'P101': ['Avengers Infinity War', 'accion', 150, 'B', 'Español', False],
    'P102': ['Dark', 'intriga', 125, 'C', 'Ingles', True],
    'P103': ['Toy Story 5', 'ciencia ficcion', 120, 'A', 'Ingles', False],
    'P104': ['Son como niños', 'comedia', 90, 'A', 'Español', True],
    'P105': ['It 2', 'terror', 118, 'C', 'Español', True],
    'P106': ['Star Wars', 'accion', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}


def mostrar_menu():
    print("===MENÚ PRINCIPAL===")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")

def pedir_entero(mensaje):
        while True:
            valor = input(mensaje)
            if valor.isdigit():
                return int(valor)
            print("Debe ingresar valores enteros")

def buscar_cupos_por_genero():
    genero = input("Ingrese género a consultar: ").strip().lower()
    total = 0
    for codigo, datos in peliculas.items():
        if datos[1].strip().lower() == genero:
            total += cartelera.get(codigo, [0, 0])[1]
    print(f"El total de cupos disponibles es: {total}")


def buscar_peliculas_por_precio():
    minimo = None
    while minimo is None:
        entrada = input("Ingrese precio mínimo: ")
        if entrada.isdigit():
            minimo = int(entrada)
        else:
            print("Debe ingresar valores enteros")
    maximo = None
    while maximo is None:
        entrada = input("Ingrese precio máximo: ")
        if entrada.isdigit():
            maximo = int(entrada)
        else:
            print("Debe ingresar valores enteros")
    resultados = []
    for codigo, datos in peliculas.items():
        precio = cartelera.get(codigo, [0, 0])[0]
        if minimo <= precio <= maximo:
            resultados.append(f"{datos[0]}--{codigo}")
    print(f"Las películas encontradas son: {resultados}")

def actualizar_precio():
    while True:
        codigo = input("Ingrese código de película: ").strip().upper()
        if codigo not in cartelera:
            print("El código no existe")
        else:
            precio = None
            while precio is None:
                entrada = input("Ingrese nuevo precio: ")
                if entrada.isdigit():
                    precio = int(entrada)
                else:
                    print("Debe ingresar valores enteros")
            cartelera[codigo][0] = precio
            print("Precio actualizado")
        continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
        if continuar != 's':
            break
        
def agregar_pelicula():
    codigo = input("Ingrese código de película: ").strip().upper()
    if not codigo:
        print("El código no puede estar vacío")
        return
    if codigo in peliculas or codigo in cartelera:
        print("El código ya existe")
        return
    titulo = input("Ingrese título: ").strip()
    genero = input("Ingrese género: ").strip().lower()
    duracion = pedir_entero("Ingrese duración (minutos): ")
    clasificacion = input("Ingrese clasificación: ").strip()
    idioma = input("Ingrese idioma: ").strip()
    es_3d = input("¿Es 3D? (s/n): ").strip().lower() == 's'
    precio = pedir_entero("Ingrese precio: ")
    cupos = pedir_entero("Ingrese cupos: ")
    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    print("Película agregada")


def eliminar_pelicula():
    codigo = input("Ingrese código de película: ").strip().upper()
    if codigo in peliculas:
        peliculas.pop(codigo, None)
        cartelera.pop(codigo, None)
        print("Película eliminada")
    else:
        print("El código no existe")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ").strip()
        if not opcion.isdigit():
            print("Debe ingresar valores enteros")
            continue
        opcion = int(opcion)
        if opcion == 1:
            buscar_cupos_por_genero()
        elif opcion == 2:
            buscar_peliculas_por_precio()
        elif opcion == 3:
            actualizar_precio()
        elif opcion == 4:
            agregar_pelicula()
        elif opcion == 5:
            eliminar_pelicula()
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida")


if __name__ == '__main__':
    main()
