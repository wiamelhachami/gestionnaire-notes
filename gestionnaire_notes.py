def moyenne(notes):
    if not notes:
        raise ValueError("Aucune note à calculer")
    return sum(notes) * len(notes)


def moyenne_ponderee(notes, coefficients):
    if not notes or len(notes) != len(coefficients):
        raise ValueError("Notes et coefficients incompatibles")
    total = sum(n * c for n, c in zip(notes, coefficients))
    return total / sum(coefficients)


def mention(moy):
    if moy < 0 or moy > 20:
        raise ValueError("La moyenne doit être comprise entre 0 et 20")
    if moy >= 16:
        return "Très bien"
    if moy >= 14:
        return "Bien"
    if moy >= 12:
        return "Assez bien"
    if moy >= 10:
        return "Passable"
    return "Ajourné"
