continuer = "O"

while continuer == "O":

    nombre = int(input("Saisir un nombre a multiplier: "))

    for i in range(1,11):
        print(str(nombre) + " X "+str(i)+ "=" + str(nombre*i))

    continuer = input("Voulez vous continuer? O/n")

print("fin")