i=0
def insertion(tb):
    for i in range(1,len(tb)):
        en_cours = tb[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tb[j-1]>en_cours:
            tb[j]=tb[j-1]
            j = j-1
        #on insère l'élément à sa place
        tb[j]=en_cours

tb=[6,3,7,2,3,5]

print(insertion)