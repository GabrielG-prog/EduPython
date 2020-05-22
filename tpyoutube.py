# recuperer saisie ce que saisie l'utilisateur
ocontinuer = ""
while ocontinuer != "o":
    oinput = input("entrez un nombre: ")



# tester si c'est un nombre
    obool = oinput.isdigit()

# si oui, continuer, afficher la table de multiplication et demander à l'utilisateur s'il souhaite quitter le programme ou non
    if obool == True:
        oinput = int(oinput)

        for i in range(11):
            print(str(i)+ "*" + str(oinput) + "=" + str(i*oinput))

    ocontinuer = input("Voulez vous continuez ? o/n ")


# sinon arreter la boucle et demander à l'utilisateur de saisir un nombre
else:
    print("erreur")




















