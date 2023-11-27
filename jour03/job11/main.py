def time_to_text(minutes):
    # Vérifier si le paramètre est un nombre entier positif
    if type(minutes) == int and minutes >= 0:
        # Calculer le nombre d'heures et de minutes
        heures = minutes // 60
        minutes_restantes = minutes % 60

        # Construire la chaîne de caractères
        if heures == 0:
            temps_texte = f"{minutes} minute{'s' if minutes > 1 else ''}"
        elif minutes_restantes == 0:
            temps_texte = f"{heures} heure{'s' if heures > 1 else ''}"
        else:
            temps_texte = f"{heures} heure{'s' if heures > 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}"

        # Afficher la chaîne de caractères
        print(temps_texte)
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appeler la fonction avec différentes valeurs
time_to_text(120)
time_to_text(65)
time_to_text(30)
time_to_text(-5)
time_to_text("abc")
