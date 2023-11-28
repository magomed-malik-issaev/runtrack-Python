def chiffrement_cesar(message, decalage):
    message_chiffre = ""

    for caractere in message:
        if caractere.isalpha():
            # Gérer les majuscules et les minuscules
            if caractere.isupper():
                nouveau_caractere = chr((ord(caractere) - ord('A' ) + decalage) % 26 + ord('A'))
            else:
                nouveau_caractere = chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        else:
            # Si ce n'est pas une lettre, conserver le caractère tel quel
            nouveau_caractere = caractere

        message_chiffre += nouveau_caractere

    return message_chiffre

# Exemple d'utilisation
message_original = "Hello, World!"
decalage_cesar = 3

# Appeler la fonction pour chiffrer le message
message_chiffre = chiffrement_cesar(message_original, decalage_cesar)

# Afficher le résultat
print("Message original :", message_original)
print(f"Message chiffré avec un décalage de {decalage_cesar} :", message_chiffre)
