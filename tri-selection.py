# Créé par korolol, le 13/04/2018 en Python 3.2

def Max(n):
    maxi=TB[0]
    ind=0
    for i in range (1,n):
        if TB[i]>maxi:
            maxi=TB[i]
            ind=i

    return(ind)

def echange(n1,n2):
    global TB
    Temp=TB[n1]
    TB[n1]=TB[n2]
    TB[n2]=Temp

def tri_selection():
    for i in range(len(TB)):
        indice=Max(len(TB)-i)
        print("Max=",TB[indice], "ind=",indice)
        fin=len(TB)-1-i
        echange(indice,fin)
        print(TB)

TB=[6,3,7,2,3,5]
print(TB)

tri_selection()
#Maximum,indice=Max(len(TB))
#print("Max=",Maximum, "ind=",indice)
#fin=len(TB)-1
#echange(indice,fin)
#print(TB)

