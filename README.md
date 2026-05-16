# Jeu du Pendu

Mini-projet du cours **MGA802 – Introduction à la programmation avec Python** (ÉTS).
Implémentation en Python du jeu du pendu, jouable dans le terminal contre l'ordinateur.

## Contenu du dépôt

| Fichier | Description |
|---|---|
| `pendu.py` | Script Python contenant le jeu (organisé en fonctions). |
| `mots_pendu.txt` | Liste de mots utilisée par défaut pour tirer un mot au hasard. |
| `README.md` | Ce fichier : description du projet et mode d'emploi. |

## Prérequis

- Python 3.x (aucune dépendance externe, seul le module standard `random` est utilisé).

## Utilisation

Depuis le dossier du projet, lancer :

```bash
python pendu.py
```

Le programme propose au démarrage d'utiliser le fichier par défaut (`mots_pendu.txt`) ou de fournir le chemin de votre propre fichier (un mot par ligne).

## Règles du jeu

- Le programme tire un mot au hasard dans le fichier de mots.
- Le joueur dispose de **6 chances** pour deviner le mot, lettre par lettre.
- À chaque tour, l'état du mot est affiché avec des `_` pour les lettres non trouvées, accompagné d'un dessin du pendu.
- Une lettre incorrecte fait perdre une chance.
- Une lettre déjà essayée ne fait pas perdre de chance — il faut en proposer une autre.
- La partie se termine lorsque le mot est trouvé (**gagné**) ou que les chances tombent à zéro (**perdu**).
- À la fin de la partie, le joueur peut choisir de **recommencer** ou de **quitter**.

## Fonctionnalités

- Sélection aléatoire d'un mot depuis un fichier texte.
- Gestion des accents et caractères spéciaux : les lettres accentuées (é, è, ê, à, â, û, ç, …) sont reconnues à partir de leur équivalent sans accent (e, a, u, c, …). Les mots composés (`week-end`) sont aussi traités comme un seul bloc (`weekend`).
- Possibilité de fournir son propre fichier de mots.
- Validation de la saisie (un seul caractère alphabétique).
- Dessin du pendu en ASCII qui évolue avec le nombre de chances restantes.
- Proposition de rejouer à la fin de chaque partie.
- **Bonus** : lorsqu'il ne reste qu'une seule chance, le programme propose un indice (une lettre qui n'appartient pas au mot), utilisable une seule fois par partie.

## Pseudo-code

```
DÉBUT programme

    FONCTION message_accueil() :
        afficher le titre du jeu
        demander "Voulez-vous voir les règles ? (oui/non)"
        SI oui :
            appeler afficher_regles()

    FONCTION afficher_regles() :
        afficher la liste des règles

    FONCTION charger_mot() :
        demander "Voulez-vous utiliser votre propre fichier ? (oui/non)"
        SI oui :
            demander le chemin du fichier
        SINON :
            utiliser "mots_pendu.txt" (fichier par défaut)
        ouvrir le fichier en UTF-8
        lire chaque ligne et la nettoyer
        RETOURNER la liste des mots non vides

    FONCTION normaliser(mot) :
        passer le mot en minuscules
        POUR chaque caractère :
            SI c'est un caractère accentué/spécial :
                le remplacer par son équivalent sans accent
            SI c'est un tiret ou un espace :
                le supprimer
        RETOURNER le mot normalisé

    FONCTION choisir_mot(liste_de_mots) :
        tirer un mot au hasard avec random.choice
        RETOURNER le mot normalisé

    FONCTION afficher_etat(mot, lettres_trouvees) :
        POUR chaque lettre du mot :
            SI la lettre est dans lettres_trouvees :
                ajouter la lettre à l'affichage
            SINON :
                ajouter "_" à l'affichage
        afficher le résultat avec un espace entre chaque caractère

    FONCTION donner_indice(mot, lettres_jouees) :
        candidats ← lettres de l'alphabet, sauf celles du mot, sauf celles déjà jouées
        SI candidats non vide :
            RETOURNER une lettre tirée au hasard parmi les candidats
        SINON :
            RETOURNER rien

    FONCTION demander_lettre() :
        RÉPÉTER :
            demander une lettre à l'utilisateur
            SI c'est un seul caractère alphabétique :
                RETOURNER la lettre
            SINON :
                avertir et redemander

    FONCTION dessiner_pendu(chance) :
        afficher le dessin ASCII correspondant au nombre de chances

    FONCTION jouer_partie(mot) :
        indice_utilise ← Faux
        chance ← 6
        lettres_trouvees ← ensemble vide
        lettres_jouees ← ensemble vide

        TANT QUE chance > 0 ET mot pas entièrement deviné :
            dessiner_pendu(chance)
            afficher_etat(mot, lettres_trouvees)
            afficher les chances restantes

            SI chance == 1 ET indice pas encore utilisé :
                proposer un indice
                marquer l'indice comme utilisé

            afficher les lettres ratées s'il y en a
            lettre ← demander_lettre()

            SI lettre déjà jouée :
                avertir et passer au tour suivant sans perdre de chance

            ajouter lettre à lettres_jouees
            SI lettre dans le mot :
                ajouter lettre à lettres_trouvees
            SINON :
                chance ← chance - 1

        SI chance > 0 :
            afficher "Gagné ! Le mot était : <mot>"
        SINON :
            dessiner le pendu final
            afficher "Perdu ! Le mot était : <mot>"

    FONCTION main() :
        message_accueil()
        mots ← charger_mot()
        RÉPÉTER :
            mot ← choisir_mot(mots)
            jouer_partie(mot)
            demander "Veux-tu rejouer ? (oui/non)"
        TANT QUE réponse != "non"
        afficher "Merci d'avoir joué !"

FIN programme
```
