from re import M


class Automovil:
    def __init__(self, modelo: str, marca: str, color: str) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado ='en reposo'
        self._motor = Motor(cilindros = 4)

    
    def acelerar (self, tipo: str = 'despacio') -> None:
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en movimiento'


class Motor:
    def __init__ (self, cilindros: int, tipo: str = 'gasolina') -> None:
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0


    def inyecta_gasolina(self, cantidad: int):
        if (cantidad < 5):
            self._temperatura = 20
        else:
            self._temperatura = 50


def run():
    toyota = Automovil('yaris', 'toyota', 'rojo')

    toyota._motor = Motor(7, 'petroleo')
    toyota.acelerar('rapido')

    print(f'La temperatura del motor es {toyota._motor._temperatura}')
    print(f'El tipo de motor es: {toyota._motor.tipo}')

if __name__ == '__main__':
    run()

