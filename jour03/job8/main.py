# Définition de la fonction
def affiche_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Combinaison non reconnue")

# Appel de la fonction avec différents paramètres
affiche_produits("fruits", "hiver")
affiche_produits("fruits", "ete")
affiche_produits("legume", "hiver")
affiche_produits("legume", "ete")
affiche_produits("poisson", "ete")  # Exemple avec une valeur non spécifiée
