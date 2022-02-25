from exos import *


class Student(Person):
    def __init__(self, notes):
        super().__init__()
        self.notes = notes

    def display_student(self):
        self.display()
        print(f"\n\nRésultats de {self.name} {self.surname} :\n")
        tot = 0
        for key, value in self.notes.items():
            print(f"{key} : {value} =>  Moyenne : {round(sum(value) / len(value), 2)}")
            tot += round(sum(value) / len(value), 2)
        tot /= 7
        print(f"\nMoyenne générale : {round(tot, 2)}")


def exo_5():
    print("\n\n\n\n======== Exercice 5 - Classe Étudiant ========\n")
    p1 = Student({
        "Histoire": [18.5, 19, 20],
        "Math": [15, 13.5, 14],
        "Français": [10, 12, 11.5],
        "Anglais": [20, 19.5, 20],
        "Italien": [15, 16.5, 16],
        "EPS": [14, 11, 13.5],
        "Philosophie": [14, 16, 14.5]
    })
    p1.display_student()
