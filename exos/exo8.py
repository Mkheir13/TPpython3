from utilitary import *


# Algorithme de comparaison entre une suite se définissant par Fibonacci et le Nombre d'Or
def exo_8():
    print("\n\n\n\n======== Exercice 8 - Le nombre d'or & Fibonacci ========\n")
    a = input_positive_int("Entrer un n : ")
    suite_o = 1
    index = 1
    print(f"\nO({index}) = {suite_o}")
    while index < a:
        suite_o = fibonacci(index + 1) / fibonacci(index)
        index += 1
        if index % 5 == 0:
            print(f"O({index}) = {suite_o}")
    print(f"Le résultat de O({index}) = {suite_o}")
    nombre_d_or = (1 + math.sqrt(5)) / 2
    print(f"Le nombre d'or = {nombre_d_or}\n")
    print("\nOn constate que la suite O tend vers le nombre d'or")
