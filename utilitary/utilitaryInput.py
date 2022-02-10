# Fonction de choix pour continuer ou pas à faire des exercices
def input_continue():
    print("\n\nVoulez-vous essayer un autre exercice ? (O / N)\n> ", end="")
    while True:
        test = input()
        if test == "O" or test == "o":
            return True
        elif test == "N" or test == "n":
            return False
        else:
            print("Choisissez une réponse valide !")
            continue


# Fonction pour choisir un seul caractère
def input_single_chr():
    letter = input("Choisissez un caractère : ")
    while len(letter) > 1 or len(letter) == 0:
        print("Vous devez choisir un seul caractère !")
        letter = input("Choisissez un caractère : ")
    return letter


# Fonction pour choisir un entier
def input_int(txt):
    test: int
    toReturn: int
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = int(number)
            break
        except ValueError:
            print("Vous devez choisir un entier !")
    return test


# Fonction pour choisir un entier positif
def input_positive_int(txt):
    test: int
    toReturn: int
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = int(number)
            if test < 0:
                print("Vous devez choisir un entier positif !")
                continue
            break
        except ValueError:
            print("Vous devez choisir un entier positif !")
    return test


# Fonction pour choisir un entier non nul
def input_nonzero_int(txt):
    test: int
    toReturn: int
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = int(number)
            if test == 0:
                print("Vous devez choisir un entier non nul !")
                continue
            break
        except ValueError:
            print("Vous devez choisir un entier non nul !")
    return test


# Fonction pour choisir un nombre
def input_float(txt):
    test: float
    toReturn: float
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = float(number)
            break
        except ValueError:
            print("Vous devez choisir un nombre !")
    return test


# Fonction pour choisir un nombre positif
def input_positive_float(txt):
    test: float
    toReturn: float
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = float(number)
            if test < 0:
                print("Vous devez choisir un nombre positif !")
                continue
            break
        except ValueError:
            print("Vous devez choisir un nombre positif !")
    return test


# Fonction pour choisir un nombre non nul
def input_nonzero_float(txt):
    test: float
    toReturn: float
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = float(number)
            if test == 0:
                print("Vous devez choisir un nombre non nul !")
                continue
            break
        except ValueError:
            print("Vous devez choisir un nombre non nul !")
    return test
