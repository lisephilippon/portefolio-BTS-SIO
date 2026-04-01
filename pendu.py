import random
import unicodedata

def enlever_accents(texte):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texte)
        if unicodedata.category(c) != 'Mn'
    )


with open("dictionnaire_francais.txt", "r", encoding="utf-8") as f:
    mots = [mot.strip() for mot in f.readlines()]


mot_pendu = enlever_accents(random.choice(mots))
mot_cache= ["_"]*len(mot_pendu)
lettres_trouvees = []
nb_erreurs = 0
nb_erreurs_max = 7


print("Bienvenue dans le jeu du pendu !")
print("Le mot contient",len(mot_pendu),"lettres")
print(mot_cache)

while nb_erreurs < nb_erreurs_max and "_" in mot_cache:
    lettre = enlever_accents(input(str("Choisissez une lettre:")))
    if len(lettre) != 1:
        lettre = enlever_accents(input(str("Choisissez une seule lettre:")))
    if lettre in lettres_trouvees:
        lettre = enlever_accents(input(str("Vous avez deja essayé cette lettre, choisissez en une autre:")))
    lettres_trouvees.append(lettre)
    if lettre in mot_pendu:
        print("------------------------")
        print("Bonne lettre !")
        for i, l in enumerate(mot_pendu):
            if l == lettre:
                mot_cache[i] = lettre
    else:
        nb_erreurs += 1
        print("------------------------")
        print("Mauvaise lettre, il vous reste",nb_erreurs_max - nb_erreurs," essais.")

    print("Mot :",mot_cache)
    print("Lettres proposées :",lettres_trouvees)

if "_" not in mot_cache:
    print("Bravo ! Vous avez trouvé le mot :", mot_pendu)
else:
    print("Pedu ! Le mot était :", mot_pendu)


