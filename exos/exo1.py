from utilitary import *


#
def exo_1():
    nbr_syracus = input_positive_int("Entrez un nombre : ")
    index = 0
    print(f"n{index} = {int(nbr_syracus)}, ", end="")
    while nbr_syracus != 1:
        if (nbr_syracus % 2) == 0:
            nbr_syracus = nbr_syracus / 2
            print(f"n{index} = {int(nbr_syracus)}, ", end="")
        else:
            nbr_syracus = (nbr_syracus * 3 + 1)
            print(f"n{index} = {int(nbr_syracus)}, ", end="")
        index += 1
    print(f"{index+1} = 4, {index+2} = 2, {index+3} = 1, et ce jusqu'à l'infini... ")