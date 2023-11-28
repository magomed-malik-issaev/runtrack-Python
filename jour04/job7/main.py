def compter_multiples_de_trois(liste):
    multiples_de_trois = [nombre for nombre in liste if nombre % 3 == 0]
    nombre_multiples_de_trois = len(multiples_de_trois)
    return nombre_multiples_de_trois

# Liste donnée
L = [8, 24, 48, 2, 16]

# Appeler la fonction pour compter le nombre de multiples de 3 dans la liste
nombre_multiples_de_trois = compter_multiples_de_trois(L)

# Afficher le résultat
print("Le nombre de multiples de 3 dans la liste est :", nombre_multiples_de_trois)
