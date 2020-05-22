
nbarti=int(input("NB d'articles?"))

somme=0
n=0
while 0<nbarti:
    prix=int(input("Saisie du prix:"))
    somme=somme+prix
    nbarti=nbarti-1

print("Somme totale:",somme)