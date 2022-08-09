class Millas:
    def __init__ (self):
        self._distancia = 0


    # Funcion para obtener el valor de _distancia
    def obtener_distancia(self):
        print('Llamamos al metodo getter')
        return self._distancia


    # Funcion para definir el valor de _distancia
    def definir_distancia(self, recorrido):
        print('Llamada al metodo setter')
        self._distancia = recorrido


    # Funcion para elimiar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia


    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


avion = Millas()
avion.distancia = 200

print(avion.distancia)