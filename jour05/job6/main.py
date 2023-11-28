def distance_toilettes_par_semaine(nb_marches, hauteur_marche_cm):
    hauteur_marche_m = hauteur_marche_cm / 100  # Conversion de la hauteur en mètres
    nombre_de_pas = 2 * nb_marches * 5  # 2 allers-retours par jour pendant 5 jours
    distance_parcourue_m = nombre_de_pas * hauteur_marche_m

    return distance_parcourue_m * 7  # Distance totale pour la semaine

# Exemple d'utilisation
nb_marches_exemple = 10
hauteur_marche_exemple = 20

# Appeler la fonction pour calculer la distance parcourue par semaine
distance_totale = distance_toilettes_par_semaine(nb_marches_exemple, hauteur_marche_exemple)

# Afficher le résultat
print(f"Pour {nb_marches_exemple} marches de {hauteur_marche_exemple} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
