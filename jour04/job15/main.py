def arrondir_et_trier(liste):
    # Fonction pour arrondir les nombres dans la liste
    def arrondir_nombre(nombre):
        # Multiplier par 100, arrondir à l'entier le plus proche, puis diviser par 100
        return int(nombre * 100 + 0.5) / 100
    
    # Appliquer la fonction d'arrondi à chaque élément de la liste
    liste_arrondie = [arrondir_nombre(nombre) for nombre in liste]
    
    # Algorithme de tri par sélection
    n = len(liste_arrondie)
    for i in range(n - 1):
        indice_minimum = i
        for j in range(i + 1, n):
            if liste_arrondie[j] < liste_arrondie[indice_minimum]:
                indice_minimum = j
        # Échanger les éléments
        liste_arrondie[i], liste_arrondie[indice_minimum] = liste_arrondie[indice_minimum], liste_arrondie[i]
    
    return liste_arrondie

# Liste donnée
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appeler la fonction pour arrondir et trier la liste
resultat = arrondir_et_trier(ma_liste)

# Afficher le résultat
print("Liste arrondie et triée dans l'ordre croissant :", resultat)
