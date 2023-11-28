def obtenir_infos_liste(liste):
    if not liste:
        print("La liste est vide.")
        return None

    valeur_maximale = max(liste)
    valeur_minimale = min(liste)
    somme_elements = sum(liste)

    return valeur_maximale, valeur_minimale, somme_elements

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Appeler la fonction pour obtenir les informations de la liste
infos_liste = obtenir_infos_liste(L)

# Afficher le résultat
if infos_liste is not None:
    valeur_maximale, valeur_minimale, somme_elements = infos_liste
    print("Valeur maximale :", valeur_maximale)
    print("Valeur minimale :", valeur_minimale)
    print("Somme des éléments :", somme_elements)
