# Definicion

from numpy import percentile


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    
    def saluda(self, otra_persona) -> str:
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'


def run():
    david = Persona('David', 35)
    erika = Persona('Erika', 32)

    print(david.saluda(erika))


if __name__ == '__main__':
    run()