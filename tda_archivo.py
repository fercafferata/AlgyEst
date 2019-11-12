import shelve


def abrir(ruta):
    return shelve.open(ruta)


def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except Exception:
        return None


def guardar(archivo, dato):
    try:
        archivo[str(len(archivo))] = dato
        return True
    except Exception:
        return None


def modificar(archivo, dato, pos):
    try:
        archivo[str(pos)] = dato
        return True
    except Exception:
        raise None

