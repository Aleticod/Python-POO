# Algoritmo de busqueda lineal
import random

def busqueda_linela(lista, objetivo) -> bool:
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    
    return match


def run():
    tamanio = int(input('Ingrese el tamanio de la lista: '))
    objetivo = int(input('Que numero quieres encontrar: '))

    lista = [random.randint(0, 100) for i in range(tamanio)]
    print (lista)
    busqueda = busqueda_linela(lista, objetivo)
    if busqueda:
        print('El elementos si se encontro dentro de la lista')
    else:
        print('El elemento no esta en la lista')

    # Operador ternario
    print(f'El elemento {objetivo} {"esta" if busqueda else "no esta"} en la lista')


if __name__ == '__main__':
    run()