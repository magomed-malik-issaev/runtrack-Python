def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    # Vérifier si la liste a au moins deux éléments
    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print("Le deuxième élément de la liste est :", deuxieme_element)
    else:
        print("La liste ne contient pas suffisamment d'éléments.")

# Appeler la fonction
afficher_deuxieme_element()
