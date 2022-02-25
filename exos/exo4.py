from utilitary import *


class Person:
    def __init__(self):
        print("\nCréation d'une nouvelle personne\n")
        self.name = input("Choisissez un nom : ")
        self.surname = input("Choisissez un prénom : ")
        self.address = input("Choisissez une adresse : ")
        self.nbr = input("Choisissez un numéro : ")

    def change(self):
        print(f"\nChangement de {self.name} {self.surname}")
        self.name = input("Choisissez un nouveau nom : ")
        self.surname = input("Choisissez un nouveau prénom : ")
        self.address = input("Choisissez une nouvelle adresse : ")
        self.nbr = input("Choisissez un nouveau numéro : ")

    def display(self):
        print(f"\nFiche de {self.name} {self.surname}")
        print("Nom : ", self.name)
        print("Prénom : ", self.surname)
        print("Adresse : ", self.address)
        print("Numéro : ", self.nbr)


def exo_4():
    print("\n\n\n\n======== Exercice 4 - Classe Personne ========\n")
    p1 = Person()
    p1.display()
    p1.change()
    p1.display()

