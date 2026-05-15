# Jeu du Pendu

Mini-projet du cours **MGA802 – Introduction à la programmation avec Python** (ÉTS).
Implémentation en Python du célèbre jeu du pendu, jouable dans le terminal contre l'ordinateur.

## Contenu du dépôt

| Fichier | Description |
|---|---|
| `pendu.py` | Script Python contenant le jeu (organisé en fonctions). |
| `MotsPendu.txt` | Liste de mots utilisée par défaut pour tirer un mot au hasard. |
| `README.md` | Ce fichier : description du projet et mode d'emploi. |

## Prérequis

- Python 3.x (aucune dépendance externe, seul le module standard `random` est utilisé).

## Utilisation

Depuis le dossier du projet, lancer :

```bash
python pendu.py
```

Le programme utilise par défaut le fichier `MotsPendu.txt`. Pour fournir votre propre liste de mots (un mot par ligne), passer le chemin en argument :

```bash
python pendu.py mon_fichier.txt
```

## Règles du jeu

- Le programme tire un mot au hasard dans le fichier de mots.
- Le joueur dispose de **6 chances** pour deviner le mot, lettre par lettre.
- À chaque tour, l'état du mot est affiché avec des `_` pour les lettres non trouvées.
- Une lettre incorrecte fait perdre une chance.
- La partie se termine lorsque le mot est trouvé (**gagné**) ou que les chances tombent à zéro (**perdu**).
- À la fin de la partie, le joueur peut choisir de **recommencer** ou de **quitter**.

## Fonctionnalités

- Sélection aléatoire d'un mot depuis un fichier texte.
- Gestion des accents : les lettres accentuées (é, è, ê, à, â, û, …) sont reconnues à partir de leur équivalent sans accent (e, a, u, …).
- Possibilité de fournir son propre fichier de mots.
- Proposition de rejouer à la fin de chaque partie.
- **Bonus** : lorsqu'il ne reste qu'une seule chance, le programme propose un indice (une lettre qui n'appartient pas au mot).

## Pseudo Code 

  DÉBUT programme

    FONCTION charger_mots(fichier) :
        SI fichier fourni en argument existe :
            ouvrir ce fichier
        SINON :
            ouvrir "MotsPendu.txt" (fichier par défaut)
        lire toutes les lignes → liste de mots
        RETOURNER la liste

    FONCTION choisir_mot(liste_de_mots) :
        RETOURNER un mot tiré au hasard (random.choice)

    FONCTION enlever_accents(lettre) :
        remplacer é/è/ê → e, à/â → a, û → u, …
        RETOURNER la lettre sans accent


    FONCTION afficher_etat(mot, lettres_trouvees) :
        POUR chaque lettre du mot :
            SI sa version sans accent est dans lettres_trouvees :
                afficher la lettre
            SINON :
                afficher "_"

    FONCTION demander_lettre() :
        Demandeer une lettre
        lire la lettre saisie par l'utilisateur
        vérifier qu'elle est valide et pas déjà jouée
        SI deja jouée : 
            lui dire quelle est déjà jouée et redemander une lettre
        RETOURNER la lettre (sans accent)

    FONCTION donner_indice(mot, lettres_deja_jouees) :     # bonus
        choisir une lettre de l'alphabet
        qui n'est pas dans le mot
        ET qui n'a pas déjà été jouée
        RETOURNER cette lettre

    FONCTION jouer_partie(mot) :
        chances ← 6
        lettres_trouvees ← {}
        lettres_jouees ← {}

        TANT QUE chances > 0 ET mot pas entièrement deviné :
            afficher_etat(mot, lettres_trouvees)
            afficher chances restantes

            SI chances == 1 :                              # bonus
                proposer un indice à l'utilisateur

            lettre ← demander_lettre(lettres_jouees)
            ajouter lettre à lettres_jouees

            SI lettre est dans le mot (version sans accent) :
                ajouter lettre à lettres_trouvees
                afficher "Bien joué !"
            SINON :
                chances ← chances - 1
                afficher "Raté !"

        SI mot entièrement deviné :
            afficher "Gagné ! Le mot était : <mot>"
        SINON :
            afficher "Perdu ! Le mot était : <mot>"

    FONCTION main() :
        mots ← charger_mots(argument éventuel)
        RÉPÉTER :
            mot ← choisir_mot(mots)
            jouer_partie(mot)
            demander "Voulez-vous rejouer ? (o/n)"
        TANT QUE réponse == "o"
        afficher "Merci d'avoir joué !"

  FIN programme

