#from random import randint

#nombre_a_deviner = randint(1,100)

#for i in range(1,6):

    #essai = int(input("Veuillez saisir " + str(i)+ " essai"))

    #if essai==nombre_a_deviner:
        #print("Gagner!!!")
        #print("Le nombre est " + str(nombre_a_deviner))
        #print("Vous avez gagne en " + str(i) +" essai(s)")
        #break

    #elif essai<nombre_a_deviner:
        #print("Le nombre a deviner est plus grand que " + str(essai))

    #else:
        #print("Le nombre a deviner est plus petit que " + str(essai))

#if essai != nombre_a_deviner:
    #print("Vous avez perdu")
    #print("Le nombre a deviner etait " + str(nombre_a_deviner))

#print("fin du jeu")

from random import randint

nombre_a_deviner = randint(1,100)

i=0

while i<5:


     essai = int(input("Veuillez saisir " + str(i)+ " essai"))

        if essai==nombre_a_deviner:
            print("Gagner!!!")
            print("Le nombre est " + str(nombre_a_deviner))
            print("Vous avez gagne en " + str(i) +" essai(s)")
            break

        elif essai<nombre_a_deviner:
            print("Le nombre a deviner est plus grand que " + str(essai))

        else:
            print("Le nombre a deviner est plus petit que " + str(essai))

        i +=1

    if essai != nombre_a_deviner:
        print("Vous avez perdu")
        print("Le nombre a deviner etait " + str(nombre_a_deviner))

    print("fin du jeu")
