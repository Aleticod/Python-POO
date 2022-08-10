import random


def busqueda_binaria(lista, inicio, fin, objetivo):
    
    if inicio > fin:
        return False
    
    medio = (fin + inicio) // 2
    if lista[medio] == objetivo:
        return True
    elif lista [medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, fin, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)


def run():
    tamano = int(input('Ingrese el tamanio de la lista: '))
    objetivo = int(input('Ingrese el numero a encontrar: '))

    lista = sorted([random.randint(0, 100) for i in range(tamano)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)

    print(f'El numero {objetivo} {"esta" if encontrado else "no esta"} en la lista')


if __name__ == '__main__':
    run()