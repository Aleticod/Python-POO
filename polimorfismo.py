class Persona:
    # ATRIBUTES

    # CONSTRUCTOR WITH PARAMETERS

    def __init__(self, nombre = "") -> None:
        self.__nombre = nombre

    # METHODS OR PROPERTIES
    # Getter
    @property
    def nombre (self):
        return self.__nombre


    # Setter
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # AUXILIARY METHODS
    def avanza(self):
        print(f'{self.__nombre} anda caminando')



class Ciclista (Persona):
    # ATRIBUTES

    # CONSTRUCTOR WITH PARAMETERS
    def __init__(self, nombre = "") -> None:
        super().__init__(nombre)

    # METHODS OR PROPERTIES

    # AUXILIARY METHODS
    # Polimorfismo
    def avanza(self):
        print(f'{self.nombre} anda en bicicleta')
        #return super().avanza()

def run ():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista()
    ciclista.nombre = 'Pedro'
    ciclista.avanza()


if __name__ == '__main__':
    run()