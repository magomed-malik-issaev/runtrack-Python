def est_separateur(c):
    # Fonction qui vérifie si le caractère est un séparateur (espace, virgule, point, etc.)
    return c in {' ', ',', '.', ';', ':', '!', '?'}

def my_long_word(longueur_min, phrase):
    mot_actuel = ""
    mots_filtres = []
    
    for caractere in phrase:
        if est_separateur(caractere):
            if mot_actuel and len(mot_actuel) > longueur_min:
                mots_filtres.append(mot_actuel)
            mot_actuel = ""
        else:
            mot_actuel += caractere
    
    # Vérifier le dernier mot après la boucle
    if mot_actuel and len(mot_actuel) > longueur_min:
        mots_filtres.append(mot_actuel)
    
    return " ".join(mots_filtres)

# Exemple d'utilisation
longueur_minimale = 3
phrase_exemple = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

# Appeler la fonction
resultat = my_long_word(longueur_minimale, phrase_exemple)

# Afficher le résultat
print("Output :", resultat)
