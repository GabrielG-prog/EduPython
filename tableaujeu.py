tb_nom=[[1,0,10,1],[0,1,10,0],[10,1,10,0],[1,10,10,1]]

somme=0

def affich():
    for i in range(cote):
        for j in range(cote):
            print (tb_nb[i][j], end=" ")
        print(" ")

for i in range (4):
    while somme !=40 and somme!=4:
        for i in range (4):
            somme=somme+tb_nom[i][2]
            if somme==40:
                print("gagne")
                gagner=1
            if somme==4:
                print("perdu")
                gagner=2




