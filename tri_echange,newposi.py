tb=[6,3,7,2,4,5]

def Max(n):
    maxi=tb[0]
    ind=0
    for i in range(1,n):
        if tb[i]>maxi:
            maxi=tb[i]
            ind=i

def echange (Max, indMax):
    for y in range(1,n):
        if tb[len(tb)-y]< Max and replace==0:
            tb[indMax]=tb[len(tb)-y]
            tb[len(tb)-y]=Max
            replace=replace+1
for z in range(1,len(tb)):
    Max(z)

def tri_selection():
    for i in range(len(tb)):
        indice=Max(len(tb)-i)
        print("Max")
