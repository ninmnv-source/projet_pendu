import random 

def message_accueil():
    print("=" * 50)
    print("       BIENVENUE AU JEU DU PENDU")
    print("=" * 50)

    reponse = input("Voulez-vous voir les règles ? (répondez 'oui' ou 'non') : ").lower()
    if reponse == "oui": 
        afficher_regles()


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
        print("Attention, pour les mots composés, les '-' ou ' ' sont supprimés.")
        print("Exemple : 'week-end' devient 'weekend'")
        print("")
        chemin = input("entrez le chemin de votre fichier:")
        

#on a le chemin/fichier qui regroupe notre base de mots 
    else :
        chemin = "mots_pendu.txt"

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
#mots = charger_mot() #quand seule cette ligne est active, ca se lance, quand aucune ligne de test est active ca se lance pas)
#print(f"{len(mots)} mots chargés")
#print(mots[:5])

def normaliser(mot):
    accents = {
        "à": "a", "â": "a", "ä": "a", "ã": "a", 
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "î": "i", "ï": "i","ì": "i", 
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
    return normaliser(random.choice(mots))

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


alphabet = "abcdefghijklmnopqrstuvwxyz"

def donner_indice(mot, lettres_jouees):
    candidat = set(alphabet) - set(mot) - lettres_jouees
    if candidat :
        return random.choice(list(candidat))
    return None

def demander_lettre():
      while True:
          lettre = input("Propose une lettre : ").strip().lower()
          if len(lettre) == 1 and lettre.isalpha():
              return lettre
          print("Ce n'est pas une lettre, réessaie.")


def jouer_partie(mot):
    indice_utilise = False 
    chance = 6
    lettres_trouvees = set()
    lettres_jouees = set()

#le temps qu'on a encore une chance et qu'on a pas trouvé le mot on continue la boucle 
    while chance >0 and set(mot) != lettres_trouvees :
        afficher_etat(mot, lettres_trouvees)  #on apelle la fonction qui affiche l'état du mot

        if chance >1 : 
            print(f'Chances restantes : {chance}')
        
        if chance == 1 and not indice_utilise :
            print(f'Chance restante : {chance}')
            reponse = input('Dernière chance ! Veux-tu un indice ? (oui/non)').lower()
            if reponse == "oui":
                indice = donner_indice(mot, lettres_jouees)
                if indice : 
                    print(f"Indice : la lettre '{indice}' n'est pas dans le mot.")
                    lettres_jouees.add(indice)
                                      # pour qu'elle ne ressorte pas
            indice_utilise = True       #pour le pas proposer d'indice à l'infini 


        mauvaises = lettres_jouees - set(mot)

        if mauvaises:                   #si on a enré une mauvaise lettre 
            print(f"Lettres ratées : {', '.join(sorted(mauvaises))}") #monter les lettres deja jouées affiché dans un ordre alphabet
            

        lettre = demander_lettre()         #on prend la lettre de l'utilisateur

#si lettre deja jouée on lui dit de donner une auttre lettre 
        if lettre in lettres_jouees:
            print("Déjà essayée ! Change de lettre!  ")
            continue                #sauter au tour suivant sans rien faire (redemander une lettre sans enelever de chance)
        lettres_jouees.add(lettre)

#si la lettre est dans le mot, le montrer, sinon lui dire qu'elle n'y ets pas 
        if lettre in mot : 
            lettres_trouvees.add(lettre)

        else : 
            chance -=1
            print("Mauvaise lettre ! Dommaaaage.. ")
        
    if chance > 0:
        print(f'Gagné!  Le mot était : {mot} ')
    else : 
        print(f'Perdu! Le mot était : {mot}')

def main():
      message_accueil()
      mots = charger_mot()

      while True:
          mot = choisir_mot(mots)
          jouer_partie(mot)

          reponse = input("\nVeux-tu rejouer ? (oui/non) : ").strip().lower()
          if reponse != "oui":
              print("Merci d'avoir joué !")
              break   

if __name__ == "__main__":
      main()

