# Programme affichant les tables de multiplication de 1 à N

# Fonction pour afficher les tables de multiplication jusqu'à N
def afficher_tables_multiplication(N):
    for i in range(1, N + 1):
        print(f"\nTable de multiplication pour {i} :\n")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} * {j} = {produit}")

# Saisie de l'entier N par l'utilisateur avec vérification
while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Appel de la fonction pour afficher les tables de multiplication
afficher_tables_multiplication(N)
