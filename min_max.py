tb_nb=[6,1,2,3,1,8,5,6]
print(tb_nb)

def Max(Param1, Param2):
    if Param1 > Param2:
        resultat = Param1
    else:
        resultat = Param2
        return(resultat)

print("Valeur maxi")
print(max(tb_nb))

def min(Param1, Param2):
    if Param1 < Param2:
        resultat = Param2
    else:
        resultat= Param1
        return(resultat)

print("Valeur mini :")
print(min(tb_nb))



def plusieurfois(nb):
    for i in range(len(tb_nb)):
        cpt=0
        if nb==tb_nb[i]:
            cpt=cpt+1
        return(cpt)
nbmax=0
for j in range(len(tb_nb)):
    print(tb_nb[j],"nombre occurence:",plusieurfois(tb_nb[j]))
    if nbmax < plusieurfois(tb_nb[j]):
        nbmax=plusieurfois(tb_nb[j])
print("nb max occurences",nbmax)
