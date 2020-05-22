from lycee import* # importation de la bibliothèque lycee
import random # importation de la bibliothèque random
import collections # importation de la bibliothèque collections

lenght = 4 #Longueur de la combinaison
guesses = 12 # nombre de chances

pattern = [random.choice('brvjom') for _ in range(lenght)] # Determination de la combinaison entre plusieurs couleurs avec une longueur prédéfini
counted = collections.Counter(pattern) # compteur qui est itérable

def running(): # création d'un fontion running
    guess = input('Votre proposition (b,r,v,j,o,m,b) :') # saisie de notre proposition de 4 couleurs
    guess_count = collections.Counter(guess) # compteur itérable permettant de savoir le nombre de coups restants
    close = sum(min(counted[k], guess_count[k]) for k in counted) # grâce a sum , les opérations ce font plus rapidement, la fonction min  prend la valeur la plus petite, au final



    exact = sum(a==b for a,b in zip(pattern,guess)) # combiner de liste en une , cette ligne de code permet de définir les couleurs correctes et bien placées
    close -= exact # on prends la lenght (4) et donc on le divise en deux , si il y a 1 exact , on 3 close
    print ('Correct : {} . Fausse : {} .'.format(exact, close)) # Affichage des couleurs correctement placées et pas du tout bien placées , de plus , la fonction format , permet d'insérer des valeurs à l'affichage dans le {}
    return exact != lenght

for attempt in range(guesses): # affiche le message " bien joué" si on a trouvé la bonne combinaison
    if not running():
        print("Bien Joué")
        break
    else:
        print ("il vous reste :", guesses - 1 - attempt,"essai(s)") # sinon , elle affiche le nombre restant de coups avant la fin du jeu
else:
    print("Perdu , la bonne combinaison etait : {}.".format(''.join(pattern))) # Affichage du message signifiant que le joueur a perdu , de plus , la bonne combinaison est donné