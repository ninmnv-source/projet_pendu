import random


def message_accueil():
    """Affiche le titre du jeu et propose à l'utilisateur de consulter les règles."""
    print("=" * 50)
    print("       BIENVENUE AU JEU DU PENDU")
    print("=" * 50)

    # .lower() pour accepter "Oui", "OUI", etc.
    reponse = input("Voulez-vous voir les règles ? (répondez 'oui' ou 'non') : ").lower().strip()
    if reponse == "oui":
        afficher_regles()


def afficher_regles():
    """Affiche les règles du jeu."""
    print("""
Règles du jeu :
    - Un mot est choisi au hasard.
    - Tu as 6 chances.
    - Chaque mauvaise lettre = -1 chance.
    - Tu ne peux pas proposer la même lettre deux fois.
    - Les accents sont gérés automatiquement.
  """)


def charger_mot():
    """Charge la liste de mots depuis le fichier par défaut ou un fichier fourni par l'utilisateur."""
    reponse = input("Voulez-vous utiliser votre propre fichier de mots ? (répondre 'oui' ou 'non') : ").lower().strip()

    if reponse == "oui":
        # Les tirets et espaces seront retirés par normaliser() : un mot composé devient un seul bloc
        print("Attention, pour les mots composés, les '-' ou ' ' sont supprimés.")
        print("Exemple : 'week-end' devient 'weekend'")
        print("")
        chemin = input("entrez le chemin de votre fichier:").strip()
    else:
        chemin = "mots_pendu.txt"

    # encoding="utf-8" pour lire correctement les accents du fichier
    # "r" pour etre  en mode lecture
    with open(chemin, "r", encoding="utf-8") as f:
        mots = []
        for ligne in f:
            mot = ligne.strip()
            if mot:  # ignorer les lignes vides éventuelles
                mots.append(mot)
        return mots


def normaliser(mot):
    """Retourne le mot en minuscules sans accents, tirets, espaces ni caractères spéciaux.

    Ainsi le joueur peut taper 'e' pour deviner 'é', et un mot composé comme
    'week-end' est traité comme un seul mot 'weekend'.
    """
    accents = {
        "à": "a", "â": "a", "ä": "a", "ã": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "î": "i", "ï": "i", "ì": "i",
        "ò": "o", "ô": "o", "ö": "o", "õ": "o", "ø": "o",
        "ù": "u", "û": "u", "ü": "u",
        "ç": "c",
        "-": "", " ": "",
        "œ": "oe", "æ": "ae",
        "ñ": "n",
        "ý": "y", "ÿ": "y",
    }
    mot = mot.lower()
    resultat = ""
    for lettre in mot:
        if lettre in accents:
            resultat += accents[lettre]
        else:
            resultat += lettre
    return resultat


def choisir_mot(mots):
    """Tire un mot au hasard dans la liste et le retourne normalisé."""
    return normaliser(random.choice(mots))


def afficher_etat(mot, lettre_trouvees):
    """Affiche le mot avec un '_' pour chaque lettre non encore devinée."""
    affichage = []
    for lettre in mot:
        if lettre in lettre_trouvees:
            affichage.append(lettre)
        else:
            affichage.append("_")
    # join() insère un espace entre les caractères pour obtenir 'c _ _ _' au lieu de 'c___'
    print(" ".join(affichage))



def dessiner_pendu(chance):
    """Affiche le dessin du pendu correspondant au nombre de chances restantes."""
    dessins = {
        6: r"""
     ╔═══════╗
     ║
     ║
     ║
     ║
     ║
  ═══╩═══════════""",
        5: r"""
     ╔═══════╗
     ║       ║
     ║      (˙_˙)
     ║
     ║
     ║
  ═══╩═══════════""",
        4: r"""
     ╔═══════╗
     ║       ║
     ║      (˙_˙)
     ║       │
     ║
     ║
  ═══╩═══════════""",
        3: r"""
     ╔═══════╗
     ║       ║
     ║      (°_°)
     ║      /│
     ║
     ║
  ═══╩═══════════""",
        2: r"""
     ╔═══════╗
     ║       ║
     ║      (°_°)
     ║      /│\
     ║
     ║
  ═══╩═══════════""",
        1: r"""
     ╔═══════╗
     ║       ║
     ║      (._.)
     ║      /│\
     ║      /
     ║
  ═══╩═══════════""",
        0: r"""
     ╔═══════╗
     ║       ║
     ║      (×_×)
     ║      /│\
     ║      / \
     ║
  ═══╩═══════════""",
        "win": r"""
     ╔═══════╗
     ║       
     ║       \(^o^)/
     ║        │
     ║       / \
     ║       
  ═══╩═══════════""",
    }
    print(dessins[chance])


alphabet = "abcdefghijklmnopqrstuvwxyz"


def donner_indice(mot, lettres_jouees):
    """Retourne une lettre absente du mot et pas encore jouée, ou None s'il n'en reste plus."""
    candidat = set(alphabet) - set(mot) - lettres_jouees #donner une lettre pas deja utilisée
    if candidat:
        return random.choice(list(candidat))    #renvoie comme indice une lettre pas encore utilisée et pas dans le mot
    return None


def demander_lettre():
    """Demande une lettre à l'utilisateur et la retourne, en validant qu'il s'agit bien d'un seul caractère alphabétique."""
    while True:
        lettre = input("Propose une lettre : ").strip().lower()
        print("")
        print("")
        if len(lettre) == 1 and lettre.isalpha(): #on verifie que c'est bien une lettre
            return lettre
        print("Ce n'est pas une lettre, réessaie.")


def jouer_partie(mot):
    """Joue une partie complète sur le mot donné jusqu'à victoire ou épuisement des chances."""
    indice_utilise = False
    chance = 6
    lettres_trouvees = set()
    lettres_jouees = set()

    while chance > 0 and set(mot) != lettres_trouvees:
        print("\n" * 30)  # nettoie visuellement le terminal entre deux tours
        dessiner_pendu(chance)
        afficher_etat(mot, lettres_trouvees)

        if chance > 1:
            print(f'Chances restantes : {chance}')

        # À la dernière chance, on propose un indice (une seule fois par partie)
        if chance == 1 and not indice_utilise:
            print(f'Chance restante : {chance}')
            reponse = input('Dernière chance ! Veux-tu un indice ? (oui/non)').lower().strip()
            if reponse == "oui":
                indice = donner_indice(mot, lettres_jouees)
                if indice:
                    print(f"Indice : la lettre '{indice}' n'est pas dans le mot.")
                    lettres_jouees.add(indice)  # marquer comme jouée pour ne pas la re-suggérer
            indice_utilise = True  # quoi qu'il décide, on ne reproposera plus d'indice

        mauvaises = lettres_jouees - set(mot)
        if mauvaises:
            print(f"Lettres ratées : {', '.join(sorted(mauvaises))}")

        lettre = demander_lettre()

        if lettre in lettres_jouees:
            print("Déjà essayée ! Change de lettre !")
            continue  # on ne consomme pas de chance pour une lettre déjà testée

        lettres_jouees.add(lettre)

        if lettre in mot:
            lettres_trouvees.add(lettre)
        else:
            chance -= 1
            print("Mauvaise lettre ! Dommaaaage.. ")

    if chance > 0:
        print(dessiner_pendu("win"))
        print(f'Gagné !  Le mot était : {mot} ')
    else:
        dessiner_pendu(0)
        print(f'Perdu ! Le mot était : {mot}')


def main():
    """Point d'entrée du programme : enchaîne accueil, chargement et boucle de parties."""
    message_accueil()
    mots = charger_mot()

    while True:     #tourne le temps que l'utilisateur n'a pas fini de jou
        mot = choisir_mot(mots)
        jouer_partie(mot)

        reponse = input("\nVeux-tu rejouer ? (oui/non) : ").strip().lower()
        if reponse == "non":
            print("Merci d'avoir joué !")
            break


if __name__ == "__main__":
    main()
