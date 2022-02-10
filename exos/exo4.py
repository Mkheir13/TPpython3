from utilitary import *


# Algorithme définissant une suite mathématique
def exo_4():
    print("\n\n\n\n======== Exercice 4 - Programmer une suite ========\n")
    square_root = math.sqrt(2)
    index = 1
    n = input_positive_int("Entrer un n: ")
    print(f"\nR({index}) =  {square_root}")
    while index < n:
        square_root = math.sqrt(2 + square_root)
        index += 1
        if index % 10 == 0:
            print(f"R({index}) = {square_root}")
    print(f"\nLe résultat de R({n}) est {square_root}")
    print("Cette suite tend vers le résultat positif de la résolution de l’équation x²-x-2 qui est 2")
