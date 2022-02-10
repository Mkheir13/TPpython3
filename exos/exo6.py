from utilitary import *


# Algorithme de développement limité de la fonction exponentielle et sinus
def exo_6():
    print("\n\n\n\n======== Exercice 6 - Développement limité ========\n")
    x = input_float("Choisissez un x (entre 73 et -15) : ")
    while True:
        print("Liste des fonctionnalités disponibles :\n")
        print(f"1 > Développement limité de l'exponentielle de {x}")
        print(f"2 > Développement limité du sinus de {x}")
        print(f"3 > Développement limité de l'exponentielle & du sinus de {x}")
        print("0 > Quitter\n")
        choice = input_positive_int("Choisissez la fonctionnalité voulu : ")
        match choice:
            case 0:
                return
            case 1:
                # Partie exponentielle
                lim_exp(x)
                break
            case 2:
                # Partie sinus
                lim_sin(x)
                break
            case 3:
                # Partie exponentielle
                lim_exp(x)
                # Partie sinus
                lim_sin(x)
                break
            case _:
                print("Cette fonctionnalité n'existe pas...")
