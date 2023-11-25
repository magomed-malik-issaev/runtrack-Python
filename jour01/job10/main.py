# Programme de simulation financière pour un investissement

# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Afficher le gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial :", gain_annuel)

# L'investisseur augmente son capital de 5 000 euros et le taux augmente de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calculer à nouveau le gain annuel
gain_annuel_apres_augmentation = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel après augmentation :", gain_annuel_apres_augmentation)

# L'investisseur retire 10% du montant total, le rendement diminue de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calculer le montant final de l'investissement
montant_final = montant_initial + gain_annuel_apres_augmentation

# Afficher le nouveau gain après retrait
gain_annuel_apres_retrait = (taux_rendement_annuel / 100) * montant_final
print("Nouveau gain annuel après retrait :", gain_annuel_apres_retrait)
