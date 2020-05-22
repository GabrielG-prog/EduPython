mot=input("Veuillez saisir un mot")
longueur=len(mot)-1
newmot=""

#for i in range(longueurdumot+1):
#    nb=randit(0,longueurdumot)
#    print("nb",nb)
#    newmot = newmot + mot[nb]
#    print(newmot)
from random import*

print("1er tour...")
nb=randint(0,longueur)

newmot=newmot+mot[nb]

mot_melange=mot[nb]

print(mot_melange)

print(mot[:nb])
print(mot[nb+1])
mot2 = mot[:nb]+mot[nb+1:]
print(mot2)

print(mot_melange)

for i in range(0,longueur):
    nb=randint(0,longueur)
    newmot=newmot+mot[nb]
print(newmot)
if (newmot[nb]== mot[nb]):
