import random


def ordenamiento_burbuja(lista):
    longitud = len(lista)
    for i in range (longitud):      # O(n)
        for j in range (longitud - i - 1): # O(n) * O(n) = O(n**2)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def run():

    tamano = int(input('Ingrese el tamano de la lista: '))
    lista_desordenada = [random.randint(0, 50) for i in range(tamano)]
    print(lista_desordenada)
    lista_ordenada = ordenamiento_burbuja(lista_desordenada)
    print(lista_ordenada)


if __name__ == '__main__':
    run()