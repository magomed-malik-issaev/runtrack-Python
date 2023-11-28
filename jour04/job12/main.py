def tri_croissant_liste(liste):
    # Algorithme de tri par sélection
    n = len(liste)
    for i in range(n - 1):
        indice_minimum = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_minimum]:
                indice_minimum = j
        # Échanger les éléments
        liste[i], liste[indice_minimum] = liste[indice_minimum], liste[i]

# Exemple d'utilisation
ma_liste = [7, 11, 3, 42, 39, 2]

# Afficher la liste initiale
print("Liste initiale :", ma_liste)

# Trier la liste dans l'ordre croissant
tri_croissant_liste(ma_liste)

# Afficher la liste triée
print("Liste triée dans l'ordre croissant :", ma_liste)
