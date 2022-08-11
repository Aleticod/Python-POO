import random

def ordenamiento_insercion(lista: list) -> list:

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        
        lista[posicion_actual] = valor_actual
    return lista

def run():
    tamanio = int(input('Ingrese el tamanio de la lista: '))

    lista_desordenada = [random.randint(0, 50) for i in range (tamanio)]
    print(lista_desordenada)
    lista_ordenada = ordenamiento_insercion(lista_desordenada)
    print(lista_ordenada)


if __name__ == '__main__':
    run()