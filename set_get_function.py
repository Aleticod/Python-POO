class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = 0

    # Funcion getter
    @property
    def region (self):
        return self.__region

    # Funcion setter
    @region.setter
    def region (self, region):
        if region in self.__pais:
            self.__region = region

        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')



def run():
    casilla = CasillaDeVotacion(123, ['CDM', 'Morelas'])
    print(casilla.region)
    casilla.region = 'CDM'
    print(casilla.region)
    print(casilla.__region)


if __name__ == '__main__':
    run()