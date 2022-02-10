from utilitary import *


#
def exo_1():
    nbr_siriacus = input_positive_int("Entrez un nombre : ")
    while nbr_siriacus != 1:
        if (nbr_siriacus % 2) == 0:
            nbr_siriacus = nbr_siriacus / 2
            print(nbr_siriacus)
        else:
            nbr_siriacus = (nbr_siriacus * 3 + 1)
            print(nbr_siriacus)