from utilitary import *
import random


# Jeu du 421
def exo_3():
    print("\n\n\n\n======== Exercice 3 - 421 ========\n")
    nbr_game = input_nonzero_int("Combien de parties voulez vous jouer : ")
    win = 0
    for i in range(nbr_game):  # Boucle des parties selon le nombre voulu
        dice = 3  # Initialisation du nombre de dés pour chaque partie
        found_dice = []  # Initialisation des nombres trouvés pour chaque partie
        print(f"\n============ PARTIE n°{i + 1}")
        for j in range(3):  # Boucle des tours pour chaque partie (3 max)
            kept_dice = 0  # Nombre de dés gardé à chaque tour
            good_dice = []  # Quels bons nombres ont été trouvés
            dice_to_sub = 0  # Nombre de dés à soustraire des dés à lancer au prochain tour
            if dice == 3:  # Lancer de dé s'il faut en lancer 3
                dice1, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)  # Lancer du dé n°1
                dice2, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)  # Lancer du dé n°2
                dice3, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)  # Lancer du dé n°3
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} {dice2} {dice3} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub  # Soustraction des dés trouvés au nombre de dé à lancer
                found_dice.sort(reverse=True)  # Rangement dans l'ordre des dés trouvé pour la vérification
                if found_dice == [4, 2, 1]:  # Vérification si la partie est gagnée
                    print(f"Partie {i + 1} gagnée en {j + 1} coup{'' if j == 0 else 's'}")
                    win += 1  # +1 au compteur de parties gagnées
                    break
                elif j == 2:  # Vérification si la partie est perdue (4, 2, 1 non trouvés au 3ᵉ tour)
                    print(f"Partie {i + 1} perdue")
                continue
            if dice == 2:  # Lancer de dé s'il faut en lancer 2
                dice1, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)  # Lancer du dé n°1
                dice2, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)  # Lancer du dé n°2
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} {dice2} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub  # Soustraction des dés trouvés au nombre de dé à lancer
                found_dice.sort(reverse=True)  # Rangement dans l'ordre des dés trouvé pour la vérification
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coup{'' if j == 0 else 's'}")
                    win += 1  # +1 au compteur de parties gagnées
                    break
                elif j == 2:  # Vérification si la partie est perdue (4, 2, 1 non trouvés au 3ᵉ tour)
                    print(f"Partie {i + 1} perdue")
                continue
            if dice == 1:  # Lancer de dé s'il faut en lancer 1
                dice1, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice) # Lancer du dé n°1
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub  # Soustraction des dés trouvés au nombre de dé à lancer
                found_dice.sort(reverse=True)  # Rangement dans l'ordre des dés trouvé pour la vérification
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coup{'' if j == 0 else 's'}")
                    win += 1  # +1 au compteur de parties gagnées
                    break
                elif j == 2:  # Vérification si la partie est perdue (4, 2, 1 non trouvés au 3ᵉ tour)
                    print(f"Partie {i + 1} perdue")
                continue
    print(f"Vous avez joué {nbr_game} parties, {win} gagnées pour {nbr_game-win} perdues, soit {round(win/nbr_game*100, 2)}% de gain")


# Algorithme de simulation d'un lancer de dé
def dice_roll(dice_to_sub, found_dice, good_dice, kept_dice):
    rolled_dice = random.randint(1, 6)  # Tirage aléatoire du nombre du dé
    if rolled_dice in [4, 2, 1] and rolled_dice not in found_dice:  # Vérification si le nombre tiré est 4, 2 ou 1, et qu'il n'a pas déjà été trouvé
        found_dice.append(rolled_dice)  # Ajout du dé aux dés trouvés de la partie
        good_dice.append(rolled_dice)  # Ajout du dé aux dés trouvés du tour
        dice_to_sub += 1  # Ajout de 1 au nombre de dés à retirer des lancers à la fin du tour
        kept_dice += 1  # Ajout de 1 au nombre de dés gardés ce tour
    return rolled_dice, dice_to_sub, kept_dice  # Retour de la valeur du dé jeté, la nouvelle valeur du nombre de dés à jeter en moins, et du nombre de dés gardés
