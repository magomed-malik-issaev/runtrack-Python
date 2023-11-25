# Chaîne de caractères
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de caractères à afficher par ligne
caracteres_par_ligne = 1

# Boucle pour créer la suite pyramidale
for i in range(len(chaine)):
    print(chaine[:caracteres_par_ligne])
    caracteres_par_ligne += 1
