"""
genetarors

los generadores son funciones que pueden 
paudar su ejecucion.

cuando se invoca una funcion generadora
devuelve un objeto generador (aka iterador)

el codigo dentro  de la funcion no se eejecuta 
de imedianto solo se copia. 

la funcion se ejecuta unicamente cuadno
iteras sobre el generador.

"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4

# se invoca funciones generadora
my_iterator = my_generator()

# se itera manuelamente sobre el generador
# print(next(my_iterator)) # iprime 1
# print(next(my_iterator)) # iprime 2
# print(next(my_iterator)) # iprime 3
# print(next(my_iterator)) # iprime 4

# los iteradores se puede iterar con un for
for value in my_interator:
    print(value)
