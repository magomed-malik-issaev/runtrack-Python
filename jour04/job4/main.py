def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    # Vérifier si l'index 2 est valide
    if len(fruits) >= 3:
        fruits.insert(2, "Mangue")
        print("La liste de fruits après ajout de Mangue à l'index 2 :", fruits)
    else:
        print("La liste ne contient pas suffisamment d'éléments pour ajouter à l'index 2.")

# Appeler la fonction
ajouter_mangue()
