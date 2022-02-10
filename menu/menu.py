from exos import *
from utilitary import *


# Fonction de lancement du menu pour le choix des exercices disponibles
def menu():
    while True:
        print("\n\nListe des exercices disponibles :\n")
        print("Exercice 1 > Le plus grand")
        print("Exercice 2 > Le Tiercé")
        print("Exercice 3 > Equation second degré")
        print("Exercice 4 > Programmer une suite")
        print("Exercice 5 > Calcul de Surface")
        print("Exercice 6 > Développement limiter")
        print("Exercice 7 > Fibonacci")
        print("Exercice 8 > Le nombre d’or & Fibonacci")
        print("0 > Quitter\n")
        choice = input_positive_int("Choisissez l'exercice voulu : ")
        match choice:
            case 0:
                print("Très bien, au revoir...")
                return
            case 1:
                exo_1()
            case 2:
                exo_2()
            case 3:
                exo_3()
            case 4:
                exo_4()
            case 5:
                exo_5()
            case 6:
                exo_6()
            case 7:
                exo_7()
            case 8:
                exo_8()
            case _:
                print("Cet exercice n'est pas disponible...")
        if not input_continue():
            print("Très bien, au revoir...")
            return
