from utilitary import *


# Algorithme résolution d'une équation du second degré
def exo_3():
    print("\n\n\n\n======== Exercice 3 - Equation second degré ========\n")
    print("Résoudre l'équation du second degré : Ax² + Bx + C = 0")
    a = input_nonzero_float("Entrer A : ")
    b = input_float("Entier B : ")
    c = input_float("Entier C : ")
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("\nL'équation n'admet pas de solutions")
    elif discriminant == 0:
        print("\nL'équation n'admet qu'une seule solution : ")
        x0 = -b / (2 * a)
        print(f"La solution double de  {a}x² + {b}x + {c} = 0 est :  {x0}")
    else:
        print("\nL'équation admet deux solutions distinctes : ")
        x1 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
        x2 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
        print(f"Les solutions de {a}x² + {b}x + {c} = 0 sont : {x1} et {x2}")
