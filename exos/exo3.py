from utilitary import *
import random


# Algorithme résolution d'une équation du second degré
def exo_3():
    print("\n\n\n\n======== Exercice 3 - 421 ========\n")
    nbr_game = input_nonzero_int("Combien de parties voulez vous jouer : ")
    for i in range(nbr_game):
        dice = 3
        found_dice = []
        print(f"============ PARTIE n°{i + 1}")
        for j in range(3):
            kept_dice = 0
            good_dice = []
            dice_to_sub = 0
            if dice == 3:
                dice1 = random.randint(1, 6)
                if dice1 in [4, 2, 1] and dice1 not in found_dice:
                    found_dice.append(dice1)
                    good_dice.append(dice1)
                    dice_to_sub += 1
                    kept_dice += 1
                dice2 = random.randint(1, 6)
                if dice2 in [4, 2, 1] and dice2 not in found_dice:
                    found_dice.append(dice2)
                    good_dice.append(dice2)
                    dice_to_sub += 1
                    kept_dice += 1
                dice3 = random.randint(1, 6)
                if dice3 in [4, 2, 1] and dice3 not in found_dice:
                    found_dice.append(dice3)
                    good_dice.append(dice3)
                    dice_to_sub += 1
                    kept_dice += 1
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} {dice2} {dice3} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub
                found_dice.sort(reverse=True)
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coups")
                    break
                if j == 2:
                    print(f"Partie {i + 1} perdue")
                continue
            if dice == 2:
                dice1 = random.randint(1, 6)
                if dice1 in [4, 2, 1] and dice1 not in found_dice:
                    found_dice.append(dice1)
                    good_dice.append(dice1)
                    dice_to_sub += 1
                    kept_dice += 1
                dice2 = random.randint(1, 6)
                if dice2 in [4, 2, 1] and dice2 not in found_dice:
                    found_dice.append(dice2)
                    good_dice.append(dice2)
                    dice_to_sub += 1
                    kept_dice += 1
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} {dice2} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub
                found_dice.sort(reverse=True)
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coups")
                    break
                if j == 2:
                    print(f"Partie {i + 1} perdue")
                continue
            if dice == 1:
                dice1 = random.randint(1, 6)
                if dice1 in [4, 2, 1] and dice1 not in found_dice:
                    found_dice.append(dice1)
                    good_dice.append(dice1)
                    dice_to_sub += 1
                    kept_dice += 1
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub
                found_dice.sort(reverse=True)
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i+1} gagnée en {j + 1} coups")
                    break
                if j == 2:
                    print(f"Partie {i + 1} perdue")
                continue
