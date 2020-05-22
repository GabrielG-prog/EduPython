
def new_posi(ind_max):

    indice=0
    while indice<ind_max and TB[ind_max]>TB[indice]:
        indice=indice+1
    return(indice)

def echange(new_ind,ind_max):

    Temp=TB[ind_max]
    for i in range (ind_max,new_ind,-1):
        TB[i]=TB[i-1]

    TB[new_ind]=Temp

def tri_insert():
    for ind in range(2,len(tb)):
        print("indice nouvelle position:", new_posi(ind))

        echange(new_posi(ind),ind)

        print(tb)


TB=[6,3,4,2,3,5]
print(TB)
if TB[0]>TB[1]:
    Temp=TB[0]
    TB[0]=TB[1]
    TB[1]=Temp

print(TB)




print("Après procédure")
ind =2


print("indice nouvelle position :", new_posi(ind))

echange(new_posi(ind),ind)

print(TB)

ind =3


print("indice nouvelle position :", new_posi(ind))

echange(new_posi(ind),ind)

print(TB)


ind =4


print("indice nouvelle position :", new_posi(ind))

echange(new_posi(ind),ind)

print(TB)
