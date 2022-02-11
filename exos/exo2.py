from xml.dom import NoModificationAllowedErr
from utilitary import *
import random


# Algorithme qui permette de connaître ses chances de gagner au tiercé, quarté, quinté et autres impôts volontaires
def exo_2():
    print("\n\n\n\n======== Exercice 2 - Jeu des allumettes ========\n")
    nom_joueur = input("Entrer votre nom : ")
    nbr_allumettes = input_positive_int("Choisir le nombre d'allumettes de départ : ")
    nbr_espace = nbr_allumettes
    nbr_tours = nbr_allumettes
    allumettes = []
    allumettes = ("|"*nbr_allumettes)
    rand = random.randint(1, 3)
    liste = [nom_joueur, "l'ordinateur"]
    name = random.choice(liste)

    print(f"{name} commence")
    while nbr_tours > 0:
        if nbr_allumettes > 1:
            if nbr_tours % 2 == 0:
                name = "Ordinateur"
            else:
                name = nom_joueur
            print(" ", allumettes, end=f" {name} enleve : {rand} \n")
            nbr_allumettes -= rand
            allumettes = ("|"*nbr_allumettes)
            allumettes =  " "*(nbr_espace - nbr_allumettes) + allumettes
            if nbr_allumettes > 3:
                rand = random.randint(1, 3)
            elif nbr_allumettes == 1:
                if name == "Ordinateur":
                    name = nom_joueur
                else:
                    name = "Ordinateur"
                print(" "*(nbr_espace - 1), " |", end=f" {name} enleve : 1 \n")
                print(f"{name} a perdu :-(")
                nbr_allumettes = 0
            else:
                rand = random.randint(1, 1)
        nbr_tours -= 1

    if name == "Ordinateur":
        print(f"{nom_joueur} a gagner :-)")
    else:
        print("L'ordinateur a gagner :-)")