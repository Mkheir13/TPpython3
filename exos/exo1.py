from utilitary import *


# Algorithme qui donne le plus grand nombre sur 10 nombres demandés
def exo_1():
    print("\n\n\n\n======== Exercice 1 - Le plus grand ========\n")
    number = input_float("Entrer le nombre n°1 : ")
    i = 1
    stock_max = number
    stock_index = i
    while i < 10:
        number = input_float(f"Entrez le nombre n°{i + 1} : ")
        i += 1
        if stock_max < number:
            stock_max = number
            stock_index = i
    print(f"\nLe plus grand de ces nombres est : {stock_max}")
    print(f"C'était le nombre numéro : {stock_index}")
