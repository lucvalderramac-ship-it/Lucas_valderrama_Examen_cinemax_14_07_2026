def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe seleccionar una opción válida")
            continue
        if opcion < 1 or opcion > 6:
            print("Debe seleccionar una opción válida")
        else:
            return opcion


def buscar_codigo(codigo, diccionario):
    codigo = codigo.upper()
    for clave in diccionario:
        if clave.upper() == codigo:
            return True
    return False


def cupos_genero(genero, peliculas, cartelera):
    genero = genero.lower()
    total = 0
    for cod in peliculas:
        if peliculas[cod][1].lower() == genero:
            total += cartelera[cod][1]
    print("El total de cupos disponibles es:", total)


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    lista = []
    for cod in cartelera:
        precio = cartelera[cod][0]
        cupos = cartelera[cod][1]
        if precio >= p_min and precio <= p_max:
            if cupos != 0:
                lista.append(peliculas[cod][0] + "--" + cod)

    lista.sort()

    if len(lista) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print("Las películas encontradas son:", lista)


def actualizar_precio(codigo, nuevo_precio, cartelera):
    existe = buscar_codigo(codigo, cartelera)
    if not existe:
        return False

    for clave in cartelera:
        if clave.upper() == codigo.upper():
            cartelera[clave][0] = nuevo_precio

    return True


def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True


def validar_genero(genero):
    return genero.strip() != ""


def validar_duracion(duracion):
    if duracion > 0:
        return True
    return False


def validar_clasificacion(clasificacion):
    validas = ["A", "B", "C"]
    if clasificacion in validas:
        return True
    return False


def validar_idioma(idioma):
    if idioma.strip() == "":
        return False
    else:
        return True


def validar_precio(precio):
    return precio > 0


def validar_cupos(cupos):
    if cupos >= 0:
        return True
    else:
        return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(codigo, peliculas):
        return False

    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    if not buscar_codigo(codigo, peliculas):
        return False

    cod = codigo.upper()
    for clave in list(peliculas.keys()):
        if clave.upper() == cod:
            del peliculas[clave]
            del cartelera[clave]

    return True


peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

opcion = 0
while opcion != 6:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    opcion = leer_opcion()

    if opcion == 1:
        genero = input("Ingrese género a consultar: ")
        cupos_genero(genero, peliculas, cartelera)

    elif opcion == 2:
        valores_ok = False
        while valores_ok == False:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    valores_ok = True
                else:
                    print("Debe ingresar valores enteros")
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(p_min, p_max, peliculas, cartelera)

    elif opcion == 3:
        continuar = "s"
        while continuar == "s":
            codigo = input("Ingrese código de película: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                nuevo_precio = 0

            if nuevo_precio <= 0:
                print("El precio debe ser un número entero mayor que cero")
            else:
                resultado = actualizar_precio(codigo, nuevo_precio, cartelera)
                if resultado == True:
                    print("Precio actualizado")
                else:
                    print("El código no existe")

            continuar = input("¿Desea actualizar otro precio (s/n)?: ")

    elif opcion == 4:
        codigo = input("Ingrese código de película: ")
        titulo = input("Ingrese título: ")
        genero = input("Ingrese género: ")

        try:
            duracion = int(input("Ingrese duración (minutos): "))
        except ValueError:
            duracion = 0

        clasificacion = input("Ingrese clasificación: ")
        idioma = input("Ingrese idioma: ")
        es_3d_texto = input("¿Es 3D? (s/n): ")

        try:
            precio = int(input("Ingrese precio: "))
        except ValueError:
            precio = 0

        try:
            cupos = int(input("Ingrese cupos: "))
        except ValueError:
            cupos = -1

        if codigo.strip() == "" or buscar_codigo(codigo, peliculas):
            print("El código ya existe")
        elif not validar_titulo(titulo):
            print("El título no es válido")
        elif not validar_genero(genero):
            print("El género no es válido")
        elif not validar_duracion(duracion):
            print("La duración no es válida")
        elif not validar_clasificacion(clasificacion):
            print("La clasificación no es válida")
        elif not validar_idioma(idioma):
            print("El idioma no es válido")
        elif es_3d_texto != "s" and es_3d_texto != "n":
            print("Debe ingresar s o n")
        elif not validar_precio(precio):
            print("El precio no es válido")
        elif not validar_cupos(cupos):
            print("Los cupos no son válidos")
        else:
            if es_3d_texto == "s":
                es_3d = True
            else:
                es_3d = False
            agregado = agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera)
            if agregado:
                print("Película agregada")
            else:
                print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese código de película a eliminar: ")
        eliminado = eliminar_pelicula(codigo, peliculas, cartelera)
        if eliminado:
            print("Película eliminada")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")