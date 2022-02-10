import math


# Fonction factorielle
def factorielle(nbr: float):
    i = 1
    fac = 1
    while i < nbr + 1:
        fac *= i
        i += 1
    return fac


# Fonction de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Fonction exponentielle
def expo(x, b):
    dev_limit_exp = x ** b / factorielle(b)
    return dev_limit_exp


# Fonction développement limité de l'exponentielle
def lim_exp(x):
    if x > 73:
        print(f"\nL'exponentielle de {x} n'est pas calculable (x doit être inférieur à 73)")
        return
    if x < -15:
        print(f"\nL'exponentielle de {x} n'est pas calculable (x doit être supérieur à -15)")
        return
    if x < 0:
        int_max_exp = -4 * x + 20
    else:
        int_max_exp = 2 * x + 20
    exp_python = math.exp(x)
    index_exp = 0
    exp_n = expo(x, index_exp)
    index_exp += 1
    while index_exp < int_max_exp:
        exp_n += expo(x, index_exp)
        index_exp += 1
    print(f"\nValeur de l'exponentielle de {x} : {exp_n}")
    print(f"Valeur de l'exponentielle de {x} à partir de la bibliothèque math : {exp_python}")
    if exp_n == exp_python:
        print("Les deux valeurs sont les mêmes")
    elif exp_n > exp_python:
        print("La valeur de la bibliothèque python est plus petite")
    elif exp_n < exp_python:
        print("La valeur de la bibliothèque python est plus grande")
    print(f"Le résultat de notre fonction exponentielle de {x} tend vers : {int_max_exp}")


# Fonction du sinus
def sinus(x, c):
    part1_dev_sinus = (-1 ** (c - 1))
    part2_dev_sinus = (x ** (2 * c - 1))
    part3_dev_sinus = factorielle(2 * c - 1)
    dev_limit_sin = part1_dev_sinus * part2_dev_sinus / part3_dev_sinus
    return dev_limit_sin


# Fonction développement limité du sinus
def lim_sin(x):
    if x > 1:
        print(f"\nLe sinus de {x} n'est pas calculable (x doit être inférieur à 1)")
        return
    if x < 0:
        print(f"\nLe sinus de {x} n'est pas calculable (x doit être supérieur à 0)")
        return
    int_max_sin = 5
    index_sin = 1
    sin_n = x
    index_sin += 1
    sin_python = math.sin(x)
    while index_sin < int_max_sin:
        sin_n += sinus(x, index_sin)
        index_sin += 1
    print(f"\nValeur du sinus de {x} : {sin_n}")
    print(f"Valeur du sinus de {x} à partir de la bibliothèque math : {sin_python}")
    if sin_n == sin_python:
        print("Les deux valeurs sont les mêmes")
    elif sin_n > sin_python:
        print("La valeur de la bibliothèque python est plus petite")
    elif sin_n < sin_python:
        print("La valeur de la bibliothèque python est plus grande")
    print(f"Le résultat de notre fonction sinus de {x} tend vers : {int_max_sin}")
