tb_nb = [i for i in range(2,300)]
longueur_tb=len(tb_nb)
i=2
while i<longueur_tb:
    tb_nb[i]='_'
    i=i+2
i=4
while i<longueur_tb:
    tb_nb[i]='_'
    i=i+3

i=23
while i<longueur_tb:
    tb_nb[i]='_'
    i=i+5

i=47
while i<longueur_tb:
    tb_nb[i]='_'
    i=i+7

print(tb_nb)



