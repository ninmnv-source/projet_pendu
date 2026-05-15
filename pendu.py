#jeu du pendu :


#%%
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


  #%%
  # test rapide
  mots = charger_mot()
  print(f"{len(mots)} mots chargés")
  print(mots[:5])


