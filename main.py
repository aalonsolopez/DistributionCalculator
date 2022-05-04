import math as ma
import numpy as np

# Función que elige entre las dos distribuciones


def chooseDistribution():
    option = -1
    while(option > 1 or option < 0):
        print("Pick a Distribution to generate a random number:")
        print("0: Poisson")
        print("1: Exponential")
        sel = input()
        option = int(sel)
    return option

# Función con el display para introducir la valor de 0 a 1.


def inputValue():
    print("Enter a valid number (from 0 to 1):")
    value = input()
    return value


# Función con el display para introducir la lambda


def inputLambda():
    print("Introduce una Lambda para la distribución")
    pick = input()
    return pick

# Funcion que ejecuta la distribución de Poisson


def poissonDistributionRandomGen(lambdaparam):
    a = pow(ma.e, -float(lambdaparam))
    b = float(1)
    n = int(0)
    np.random.seed(0)
    arr = np.random.uniform(0, 1, 100)
    i = int(0)
    while(b >= a and i < 100):
        b = arr[i] * b
        i = i + 1
        n = n + 1
    return n

# Función que ejecuta la distribución de Exponencial


def exponentialDistributionRandomGen(lambdaparam):
    logparam = inputValue()
    division = float(1 / float(lambdaparam))
    result = division * float(ma.log(float(logparam)))
    print(abs(result))

# Función que contiene la totalidad del programa


def main():
    lamb = inputLambda()
    val = int(chooseDistribution())
    if val == 0:
        print(poissonDistributionRandomGen(lamb))
    else:
        print(exponentialDistributionRandomGen(lamb))

main()
