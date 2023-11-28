def supprimer_doublons_liste(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    
    return liste_sans_doublons

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Afficher la liste initiale
print("Liste initiale :", ma_liste)

# Supprimer les doublons de la liste
ma_liste_sans_doublons = supprimer_doublons_liste(ma_liste)

# Afficher la liste sans doublons
print("Liste sans doublons :", ma_liste_sans_doublons)
