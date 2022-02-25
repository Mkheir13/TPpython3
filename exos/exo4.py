from utilitary import *


# Définition de la class Person
class Person:
    # Fonction d'initialisation
    def __init__(self):
        print("\nCréation d'une nouvelle personne\n")
        self.name = input("Choisissez un nom : ")
        self.surname = input("Choisissez un prénom : ")
        self.address = input("Choisissez une adresse : ")
        self.nbr = input("Choisissez un numéro : ")

    # Fonction de modification d'une personne
    def change(self):
        print(f"\nChangement de {self.name} {self.surname}")
        self.name = input("Choisissez un nouveau nom : ")
        self.surname = input("Choisissez un nouveau prénom : ")
        self.address = input("Choisissez une nouvelle adresse : ")
        self.nbr = input_positive_int("Choisissez un nouveau numéro : ")

    # Fonction d'affichage des éléments d'une personne
    def display(self):
        print(f"\nFiche de {self.name} {self.surname}")
        print("Nom : ", self.name)
        print("Prénom : ", self.surname)
        print("Adresse : ", self.address)
        print("Numéro : ", self.nbr)


# Mise en pratique de la création d'un objet Person, son affichage et sa modification
def exo_4():
    print("\n\n\n\n======== Exercice 4 - Classe Personne ========\n")
    p1 = Person()
    p1.display()
    p1.change()
    p1.display()

