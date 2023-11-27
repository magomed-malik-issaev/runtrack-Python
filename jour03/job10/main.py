def verifier_pair_impair(nombre):
    # Vérifier si le nombre est un entier positif
    if type(nombre) == int and nombre >= 0:
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            return f"{nombre} est un nombre pair."
        else:
            return f"{nombre} est un nombre impair."
    else:
        return "Veuillez entrer un nombre entier positif."

# Appeler la fonction avec différentes valeurs
nombre1 = 8
nombre2 = 15
nombre3 = -3
nombre4 = "abc"  # Ce cas n'est pas un nombre entier positif

resultat1 = verifier_pair_impair(nombre1)
resultat2 = verifier_pair_impair(nombre2)
resultat3 = verifier_pair_impair(nombre3)
resultat4 = verifier_pair_impair(nombre4)

# Afficher les résultats
print(resultat1)
print(resultat2)
print(resultat3)
print(resultat4)
