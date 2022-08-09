import time

# COMPLEJIDAD TEMPORAL

# Decorador
def time_decorator(function):
    
    def wrapper(n: int):
        initial_time = time.time()
        function(n)
        final_time = time.time()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed) + ' segundos')

    return wrapper


# @time_decorator
def factorial(n: int) -> int:
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta


# @time_decorator
def factorial_r(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)



def run():
    n = 990

    comienzo = time.time()
    factorial(n)
    final = time .time()
    print(final - comienzo)
    
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)

if __name__ == '__main__':
    run()