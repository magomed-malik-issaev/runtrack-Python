def somme_valeurs_paires(liste):
    valeurs_paires = [nombre for nombre in liste if nombre % 2 == 0]
    somme = sum(valeurs_paires)
    return somme

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Appeler la fonction pour calculer la somme des valeurs paires
somme_paires = somme_valeurs_paires(L)

# Afficher le résultat
print("La somme des valeurs paires dans la liste est :", somme_paires)
