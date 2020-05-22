
tortue=0

de=randint(1,6)

while de!=6 and tortue!=6:
    tortue=tortue+1
    de=randint(1,6)
    print("de= ",de)
    print("T"*(tortue+1))
print("L")

if de==6:
    print("L"*6)
    print("Le lapin a gagné")
