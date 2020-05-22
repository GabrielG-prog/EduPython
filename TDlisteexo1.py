Tb_jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
nb_jour=int(input("Saisir un nb"))

while nb_jour<1 or nb_jour>7:
    nb_jour=int(input("Saisie invalide.Saisir un nb"))

if nb_jour==1:
    msg="1er"
else: msg=str(nb_jour)+"ème"

print("Le", msg, "jour est", Tb_jours[nb_jour-1])