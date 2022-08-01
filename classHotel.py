# Hotel class abstraction
class Hotel:
    def __init__ (self, numero_maximo_huespedes: int, lugares_estacionamiento: int):
        self.numero_maximo_huespedes = numero_maximo_huespedes
        self.lugares_estacionamiento = lugares_estacionamiento
        self.huespedes = 0


def run():
    hotel_platzi = Hotel(numero_maximo_huespedes = 50, lugares_estacionamiento = 20)
    hilton = Hotel(10, 60)
    print(hotel_platzi.lugares_estacionamiento)
    print(hotel_platzi.huespedes)
    print(hilton.numero_maximo_huespedes)
    print(hilton.lugares_estacionamiento)


if __name__ == '__main__':
    run()
