def echanger_premiere_derniere(liste):
    if len(liste) >= 2:
        liste[0], liste[-1] = liste[-1], liste[0]
        print("La liste après échange entre la première et la dernière case :", liste)
    else:
        print("La liste doit contenir au moins deux éléments pour effectuer l'échange.")

# Exemple d'utilisation avec une liste
ma_liste = [1, 2, 3, 4, 5]

# Afficher la liste initiale
print("Liste initiale :", ma_liste)

# Appeler la fonction pour échanger la première et la dernière case
echanger_premiere_derniere(ma_liste)
