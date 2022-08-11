import random


def ordenamiento_mezcla (lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        
        # iterador para recorrer la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda [i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

def run():

    tamanio = int(input('Ingrese el tamanio de la lista: '))

    lista_desordenada = [random.randint(0, 30) for i in range(tamanio)]
    print(lista_desordenada)
    print('-' * 20)
    lista_ordenada = ordenamiento_mezcla(lista_desordenada)
    print(lista_ordenada)


if __name__ == '__main__':
    run()