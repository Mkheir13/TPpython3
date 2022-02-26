from utilitary import *
import random

# Algorithme qui permet de simuler une partie du jeu des allumettes contre l'ordinateur
def exo_2():
    print("\n\n\n\n======== Exercice 2 - Jeu des allumettes ========\n")
    nom_joueur = input("Entrer votre nom : ")
    nb_allumettes = input_positive_int("Choisir le nombre d'allumettes de départ : ")
    nb_espace = nb_allumettes
    bol = True
    nb_tours = nb_allumettes
    
    print("{} commence".format(nom_joueur if not bol else "l\'ordinateur"))
    while nb_tours > 0:
        rand = random.randint(1, 3)
        if nb_allumettes > 0:
            bol = not bol
            if bol:
                rand = input_positive_int_onethree(f"{'|' * nb_allumettes:>{nb_espace}} {nom_joueur} enleve : ") #permet d'afficher les allumettes qu'enleve le joueur
                nb_allumettes -= rand
            else:
                if nb_allumettes < 3:
                    rand = random.randint(1, 2)
                elif nb_allumettes < 2:
                    rand = 1
                else:
                    rand = random.randint(1, 3)
                print(f"{'|' * nb_allumettes:>{nb_espace}}", end=f" Ordinateur enleve : {rand} \n") #permet d'afficher les allumettes qu'enleve l'ordinateur
                nb_allumettes -= rand
        nb_tours -= 1
    print("{} a perdu :-(".format(nom_joueur if not bol else "l\'ordinateur"))
    print("{} a gagné :-)".format(nom_joueur if bol else "l\'ordinateur"))