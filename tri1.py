
def Max(n):
    maxi=tb[0]
    ind=0
    for i in range (1,n):
        if tb[i]>maxi:
            maxi=tb[i]
            ind=i


    return(maxi,ind)

def echange (n1,n2):
    global tb
    Temp=tb[n1]
    tb[n1]=tb[n2]
    tb[n2]=Temp


tb=[6,3,7,2,3,5]
print(tb)
Maximum,indice=Max(len(tb))
print("Max= ",Maximum, "ind ",indice)
fin=len(tb)
echange(indice,fin)
print(tb)
Maximum,indice=Max(len(tb)-1)
print("Max= ",Maximum, "ind ",indice)
fin=len(tb)-1
echange(indice,fin)
print(tb)
Maximum,indice=Max(len(tb)-2)
print("Max= ",Maximum, "ind ",indice)
fin=len(tb)-2
echange(indice,fin)
print(tb)
