from utilitary import *


# Algorithme de calcul d'intégrale
def exo_5():
    print("\n\n\n\n======== Exercice 5 - Calcul de surface ========\n")
    a = input_int("Entrer A : ")
    b = input_int("Entrer B : ")
    p = input_positive_float("Entrer P : ")
    if b < a:
        print("Le calcul de cette intégrale est impossible, A doit être inférieur à B")
        return
    else:
        u0 = a * a * p
        s = u0
        n = 1
        while a + p * n < b:
            un = (a + p * n) * (a + p * n) * p
            s = un + s
            n = n + 1
        print(f"\nCalcul de l'intégrale de la fonction y = x * x avec {a} <= x < {b} et p = {p}")
        print(f"Résultat : {s}")
