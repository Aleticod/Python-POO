# Hotel class abstraction

# class <nombre_de_la_clase>(<super_clase>):
class Hotel:
    # Constructor
    # def __init__ (self, <params>):
    def __init__ (self, numero_maximo_huespedes: int, lugares_estacionamiento: int):
        self.numero_maximo_huespedes = numero_maximo_huespedes
        self.lugares_estacionamiento = lugares_estacionamiento
        self.huespedes = 0


    # Auxiliary methods
    # def <nombre_del_metodo> (self, <params>):
    def anadir_huespedes(self, cantidad_huespedes: int):
        self.huespedes += cantidad_huespedes


    def checkout(self, cantidad_huespedes: int):
        self.huespedes -= cantidad_huespedes


    def ocupacion_total(self) -> int:
        return self.huespedes


def run():
    hotel_platzi = Hotel(numero_maximo_huespedes = 50, lugares_estacionamiento = 20)
    hilton = Hotel(10, 60)
    print(hotel_platzi.lugares_estacionamiento)
    print(hotel_platzi.huespedes)
    print(hilton.numero_maximo_huespedes)
    print(hilton.lugares_estacionamiento)
    
    hilton.anadir_huespedes(3)
    hilton.checkout(1)
    print(hilton.ocupacion_total())



if __name__ == '__main__':
    run()
