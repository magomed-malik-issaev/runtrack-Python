def produit_dans_intervalle(liste, borne_inf, borne_sup):
    valeurs_dans_intervalle = [nombre for nombre in liste if borne_inf <= nombre <= borne_sup]

    if not valeurs_dans_intervalle:
        print(f"Aucune valeur dans l'intervalle [{borne_inf}, {borne_sup}]")
        return None

    produit = 1
    for valeur in valeurs_dans_intervalle:
        produit *= valeur

    return produit

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Bornes de l'intervalle
borne_inf = 25
borne_sup = 90

# Appeler la fonction pour calculer le produit dans l'intervalle
produit_intervalle = produit_dans_intervalle(L, borne_inf, borne_sup)

# Afficher le résultat
if produit_intervalle is not None:
    print(f"Le produit des valeurs dans l'intervalle [{borne_inf}, {borne_sup}] est :", produit_intervalle)
