from utilitary import *


# Algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts volontaires
def exo_2():
    print("\n\n\n\n======== Exercice 2 - Le tiercé ========\n")
    a = input_positive_int("Entrer le nombre de chevaux partants : ")
    b = input_positive_int("Entrer le nombre de chevaux joués : ")
    x = factorielle(a) / factorielle(a - b)
    y = factorielle(a) / (factorielle(b) * factorielle(a - b))
    print(f"\nDans l'ordre : une chance sur  {x} de gagner")
    print(f"Dans le désordre : une chance sur {y} de gagner")
