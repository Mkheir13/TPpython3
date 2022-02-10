from utilitary import *


# Algorithme calculant la valeur de Fibonacci selon le n rentré
def exo_7():
    print("\n\n\n\n======== Exercice 7 - Fibonacci ========\n")
    n = input_positive_int("Choisissez un positif :")
    print(f"\nFibonacci de {n} est {fibonacci(n)}")
