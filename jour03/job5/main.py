# Définition de la fonction
def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Vérification pour éviter la division par zéro
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        return num1 % num2
    else:
        return "Erreur : Opérateur non reconnu"

# Appel de la fonction avec différents paramètres
resultat_addition = calcule(5, "+", 3)
resultat_multiplication = calcule(7, "*", 4)
resultat_division = calcule(10, "/", 2)

# Affichage des résultats
print("Résultat de l'addition :", resultat_addition)
print("Résultat de la multiplication :", resultat_multiplication)
print("Résultat de la division :", resultat_division)
