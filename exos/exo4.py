from utilitary import *


class Person:
    def __init__(self, p_name, p_surname, p_address, p_nbr):
        self.name = p_name
        self.surname = p_surname
        self.address = p_address
        self.nbr = p_nbr



    def display(self):
        print("Nom : ", self.name)
        print("Prénom : ", self.surname)
        print("Adresse : ", self.address)
        print("Numéro : ", self.nbr)


# Algorithme définissant une suite mathématique
def exo_4():
    print("\n\n\n\n======== Exercice 4 - Classe Personne ========\n")
    p1 = Person("Eddine", "Kheir", "CACA", "055055")
    p1.display()

