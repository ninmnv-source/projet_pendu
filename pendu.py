import random 

def message_accueil():
    print("=" * 50)
    print("       BIENVENUE AU JEU DU PENDU")
    print("=" * 50)

    reponse = input("Voulez-vous voir les règles ? (répondez 'oui' ou 'non') : ").lower()
    if reponse == "o": 
        afficher_regles()

    input("Appuie sur Entrée pour commencer...")
    print()

def afficher_regles():
    print("""
Règles du jeu :
    - Un mot est choisi au hasard. 
    - Tu as 6 chances.
    - Chaque mauvaise lettre = -1 chance.
    - Tu ne peux pas proposer la même lettre deux fois. 
    - Les accents sont gérés automatiquement.
  """)



def charger_mot():
# on demande ce que l'utilisateur préfère entre le fchier par defaut et son fichier 
#lower() transforme majuscules en minuscules, pas de risque d'avoir de problèmes de majuscules avec la prmière lettre

    reponse = input("Voulez-vous utiliser votre propre fichier de mots ? (répondre 'oui' ou 'non') : ").lower() 

    if reponse == "oui":
        chemin = input("entez le chemin de votre fichier:")

#on a le chemin/fichier qui regroupe notre base de mots 
    else :
        chemin = "MotsPendu.txt"

#on ouvre le fichier en mode "read" (r) de sorte à pouvoir aussi lire les accents et on deifni f comme nom de variable du fichie rouvert
    with open(chemin, "r", encoding = "utf-8") as f:

#on créer une liste de mots tirés du fchier de mots 
        mots = []
        for ligne in f :
            mot = ligne.strip() #enlève les espaces innutiles
            if mot :  #si jamais il y a des lignes vides
                mots.append(mot)
        return mots



# test rapide
mots = charger_mot() #quand seule cette ligne est active, ca se lance, quand aucune ligne de test est active ca se lance pas)
#print(f"{len(mots)} mots chargés")
#print(mots[:5])

def choisir_mot(mots):
    return random.choice(mots) 

#print(choisir_mot(mots))


def afficher_etat(mot, lettre_trouvees):
    affichage = []
    for lettre in mot :
        if lettre in lettre_trouvees:
            affichage.append(lettre) 
        else :
            affichage.append("_")
    print(" ".join(affichage))      #join colle tous les elements de la listre affichage par un espace 



#afficher_etat("carbone", set())
#afficher_etat("carbone", {"c"})
#afficher_etat("carbone", {"c", "o", "e"})



def jouer_partie(mot):
    chance = 6
    lettres_trouvees = set()
    lettres_jouees = set()

#le temps qu'on a encore une chance et qu'on a pas trouvé le mot on continue la boucle 
    while chance >0 and set(mot) != lettres_trouvees :
        afficher_etat(mot, lettres_trouvees)  #on apelle la fonction qui affiche l'état du mot

        mauvaises = lettres_jouees - set(mot)

        if mauvaises:                   #si mauvaises lettres existent deja et pas deja dans le mot
            print(f"Lettres ratées : {', '.join(sorted(mauvaises))}")
            #monter les lettres deja jouées affiché dans un ordre alphabet

        if chance >1 : 
            print(f'Chances restantes : {chance}')
        if chance == 1 :
            print(f'Chance restante : {chance}')

        lettre = input("Propose une lettre : ").lower()         #on prend la lettre de l'utilisateur

#si lettre deja jouée on lui dit de donner une auttre lettre 
        if lettre in lettres_jouees:
            print("Déjà essayée ! Change de lettre! ")
            continue                #sauter au tour suivant sans rien faire (redemander une lettre sans enelever de chance)
        lettres_jouees.add(lettre)

#si la lettre est dans le mot, le montrer, sinon lui dire qu'elle n'y ets pas 
        if lettre in mot : 
            lettres_trouvees.add(lettre)

        else : 
            chance -=1
            print("mauvaise lettre ! dommaaaage..")
        
    if chance > 0:
        print(f'Gagné!  Le mot étai : {mot}')
    else : 
        print(f'Perdu! Le mot était : {mot}')


jouer_partie("chat")