
# Programme affichant l'alphabet à l'envers

# Boucle pour chaque lettre de l'alphabet à l'envers
for lettre in range(ord('z'), ord('a')-1, -1):
    print(chr(lettre), end=' ')

