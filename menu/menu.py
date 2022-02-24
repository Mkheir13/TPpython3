from exos import *
from utilitary import *


# Fonction de lancement du menu pour le choix des exercices disponibles
def menu():
    while True:
        print("\n\nListe des exercices disponibles :\n")
        print("Exercice 1 > Suite de Syracuse")
        print("Exercice 2 > Jeu des allumettes")
        print("Exercice 3 > 421")
        print("Exercice 4 > Classe Personne")
        print("Exercice 5 > Classe Étudiant")
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
            case _:
                print("Cet exercice n'est pas disponible...")
        if not input_continue():
            print("Très bien, au revoir...")
            return
