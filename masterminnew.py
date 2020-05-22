# Créé par ordinateur, le 10/11/2017 avec EduPython
from random import * # la librairie random est plus leger que lycée
mot_a_trouve="" #Variable contenant le code a trouve
couleur = "BRVJOM" #chaine de caractere contenant les couleurs

for i in range(4):
    de=randint(0,5)
    print(de)
    mot_a_trouve=mot_a_trouve+couleur[de]
    print(mot_a_trouve)

mot_saisie = input("Entre votre essai parmis BRVJOM et fesant 4 lettres :")
longueur_mot=len(mot_saisie)

test = 0
while test == 0:
    test=1
    if longueur_mot<4:
        print("mot trop court . Veuiller saisie un mot de lettre ")
        test=0
    elif longueur_mot>4:
        print("mot trop court . Veuiller saisie un mot de lettre ")
        test = 0
    else :
        for i in range(4):
            if mot_saisie[i].upper() !="B" and mot_saisie[i].upper() !="R" and mot_saisie[i].upper() !="V" and mot_saisie[i].upper() !="J" and mot_saisie[i].upper() !="O" and mot_saisie[i].upper() !="M":
