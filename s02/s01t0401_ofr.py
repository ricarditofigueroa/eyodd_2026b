"""
Escribe un programa que calcule 
la suma de los "n" numeros naturales.
por ejemplo si n = 100, el programa
claculara la suma del 1 al 100
42
"""
# import biblioteca time
import time

# tomando el inicial tiempo
timestamp_01 = time.time()

# programa que calcula la suma 
# de los "n" numeros naturales
n = 100
total_sum = 0

# ciclo for
for number in range(1,n+1):
    total_sum = total_sum + number
    # 1: Sum <- 0 + 1
    # Sum = 1
    # 2: Sum <- 1 + 2
    # Sum = 3
    # 3: Sum <- 3 + 1
    # ...
    # 100: Sum <- Sum_(-1) + 100
print(f"La suma de 1 hasta {n} es: {total_sum}")
    #Actualización del programa de suma

    # tomando el tiemo final 
timestamp_02 = time.time()

# impresion del tiempo de ajecucion
print(f"tiempo de ejecucion: {(timestamp_02 - timestamp_01) * 1e6:.2f} μs")