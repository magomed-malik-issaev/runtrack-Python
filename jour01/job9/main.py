# Programme de gestion d'un inventaire

# Variables représentant un produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_en_stock = 50

# Afficher les informations initiales du produit
print("Produit :", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_en_stock)
print("\n")

# Ajouter des produits en stock
quantite_achetee = int(input("Combien d'unités souhaitez-vous acheter ? "))
quantite_en_stock += quantite_achetee

# Mettre à jour le prix après une inflation de 10%
prix_unitaire *= 1.10

# Afficher les informations mises à jour du produit
print("Produit mis à jour :", nom_produit)
print("Prix unitaire après inflation :", prix_unitaire)
print("Quantité en stock mise à jour :", quantite_en_stock)
