from utilitary import *
import random


# Algorithme résolution d'une équation du second degré
def exo_3():
    print("\n\n\n\n======== Exercice 3 - 421 ========\n")
    nbr_game = input_nonzero_int("Combien de parties voulez vous jouer : ")
    win = 0
    for i in range(nbr_game):
        dice = 3
        found_dice = []
        print(f"\n============ PARTIE n°{i + 1}")
        for j in range(3):
            kept_dice = 0
            good_dice = []
            dice_to_sub = 0
            if dice == 3:
                # dices = [dice_roll(dice_to_sub, found_dice, good_dice, kept_dice) for _ in range(dice)]
                dice1, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)
                dice2, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)
                dice3, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} {dice2} {dice3} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub
                found_dice.sort(reverse=True)
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coup{'' if j == 0 else 's'}")
                    win += 1
                    break
                elif j == 2:
                    print(f"Partie {i + 1} perdue")
                continue
            if dice == 2:
                # dices = [dice_roll(dice_to_sub, found_dice, good_dice, kept_dice) for _ in range(dice)]
                dice1, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)
                dice2, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)
                print(
                    f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} {dice2} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub
                found_dice.sort(reverse=True)
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coup{'' if j == 0 else 's'}")
                    win += 1
                    break
                elif j == 2:
                    print(f"Partie {i + 1} perdue")
                continue
            if dice == 1:
                dice1, dice_to_sub, kept_dice = dice_roll(dice_to_sub, found_dice, good_dice, kept_dice)
                print(f"Lancer {j + 1} avec {dice} dé{'s' if dice > 1 else ''} : {dice1} je {'ne garde rien' if kept_dice == 0 else f'garde {good_dice}'}. Trouvé pour l'intant : {found_dice}")
                dice -= dice_to_sub
                found_dice.sort(reverse=True)
                if found_dice == [4, 2, 1]:
                    print(f"Partie {i + 1} gagnée en {j + 1} coup{'' if j == 0 else 's'}")
                    win += 1
                    break
                elif j == 2:
                    print(f"Partie {i + 1} perdue")
                continue
    print(f"Vous avez joué {nbr_game} parties, {win} gagnées pour {nbr_game-win} perdues, soit {round(win/nbr_game*100, 2)}% de gain")


def dice_roll(dice_to_sub, found_dice, good_dice, kept_dice):
    dice = random.randint(1, 6)
    if dice in [4, 2, 1] and dice not in found_dice:
        found_dice.append(dice)
        good_dice.append(dice)
        dice_to_sub += 1
        kept_dice += 1
    return dice, dice_to_sub, kept_dice
