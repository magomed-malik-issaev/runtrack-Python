# Définition de la fonction
def affiche_type_developpeur(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Appel de la fonction avec différents paramètres
affiche_type_developpeur("JavaScript")
affiche_type_developpeur("python")
affiche_type_developpeur("java")
affiche_type_developpeur("reactjs")
affiche_type_developpeur("C++")  # Exemple avec une valeur non spécifiée
