def remplacer_element_par_somme(voisins, liste):
    if len(liste) > 3:
        somme_voisins = liste[voisins[0]] + liste[voisins[1]]
        liste[3] = somme_voisins
        print("La liste après remplacement de L[3] par la somme des cases voisines L[2] et L[4] :", liste)
    else:
        print("La liste ne contient pas suffisamment d'éléments pour effectuer le remplacement.")

# Créer une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Afficher la deuxième valeur de la liste
deuxieme_valeur = L[1]
print("La deuxième valeur de la liste est :", deuxieme_valeur)

# Appeler la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
remplacer_element_par_somme([2, 4], L)

# Afficher la dernière valeur de la liste
derniere_valeur = L[-1]
print("La dernière valeur de la liste est :", derniere_valeur)
