class Lavadora:

    def __init__ (self):
        pass

    def lavar(self, temperatura = 'frio'):
        self._llenar_tanque_de_agua (temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    
    def _llenar_tanque_de_agua(self, temperatura: str):
        print(f'Llenando el tanque con agua a la temperatura de {temperatura}')



    def _anadir_jabon(self):
        print(f'Anadiendo jabon')



    def _lavar(self):
        print(f'Se esta lavando la ropa')


    def _centrifugar(self):
        print(f'Se esta centrifugando la ropa')


def run ():
    lavar_ropa = Lavadora()
    lavar_ropa.lavar('caliente')


if __name__ == '__main__':
    run()