def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            # Échec, ne pas arrondir
            notes_arrondies.append(note)
        else:
            # Arrondir aux multiples de 5 si nécessaire
            prochain_multiple_de_cinq = (note // 5 + 1) * 5
            if prochain_multiple_de_cinq - note < 3:
                notes_arrondies.append(prochain_multiple_de_cinq)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_eleves = [83, 92, 78, 55, 40, 63]

# Appeler la fonction pour arrondir les notes
notes_arrondies = arrondir_notes(notes_eleves)

# Afficher le résultat
print("Notes d'origine :", notes_eleves)
print("Notes arrondies :", notes_arrondies)
