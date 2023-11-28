def draw_triangle(height):
    for i in range(height):
        # Utilisation de l'opérateur de modulo pour alterner entre '_' et '/'
        if i % 2 == 0:
            print('_ ' * (i + 1))
        else:
            print('/' + ' ' * (2 * i - 1) + '\\')

# Demander à l'utilisateur de renseigner la hauteur du triangle
hauteur_triangle = int(input("Entrez la hauteur du triangle : "))

# Afficher le triangle avec la hauteur fournie
draw_triangle(hauteur_triangle)
