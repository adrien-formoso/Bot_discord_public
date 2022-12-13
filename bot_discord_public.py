import discord
import random
import time
import datetime

client = discord.Client(intents = discord.Intents.all())

#################################################################################### 
##########################################      LISTE DE QUESTION, INDICE, REPONSE

liste_geographie_questions = ["Quelle est la capitale de la France ?",#0
                              "Quel est le numéro du département de Paris ?",#1
                              "Combien d'arrondissements y a t'il dans Paris ?",#2
                              "Ou se situe la premiere statue de la liberté?",#3
                              "Combien de pays existent dans le monde ?",#4
                              "Dans quel pays se trouve Venise ?",#5
                              "Dans quel continent se trouve le Cameroon ?",#6
                              "Où se trouve l'Allemagne ?",#7
                              "Capitale du Mexique ?",#8
                              "Capital du Portugal ?"]#9

liste_geographie_indices   = ["Où est situé la Tour Eiffel?",#0
                              "_5",#1
                              "2_",#2
                              "https://cdn.discordapp.com/attachments/1039227124961255536/1050721262256799814/statue_de_la_liberte_paris.jpg",#3
                              "19_",#4
                              "https://cdn.discordapp.com/attachments/1039227124961255536/1050723150515679262/3092.png",#5
                              "https://cdn.discordapp.com/attachments/1039227124961255536/1050723149857169418/africa-mapa.gif",#6
                              "https://cdn.discordapp.com/attachments/1039227124961255536/1050723150251446282/480c0e9e4085975db2fa7289b0e1d3dc.jpg",#7
                              "https://cdn.discordapp.com/attachments/1039227124961255536/1050723149672624158/06-mexico_mapa_de_los_estados_s.jpg",#8
                              "LI _ _ _ _ _"]#9

liste_geographie_reponses  = ["Paris",#0
                              "75",#1
                              "20",#2
                              "Paris",#3
                              "195",#4
                              "Italie",#5
                              "Afrique",#6
                              "Europe",#7
                              "Mexico",#8
                              "Lisbonne"]#9

liste_culturegenerale_questions = ["C’est quelle date la fête nationale de la France (format _ _-_ _) ?",#0
                                   "C'est qui le president de la republique en France",#1
                                   "Quelle est la hauteur de la Tour Eiffel ?",#2
                                   "Quelle est la langue officielle du quebec ?",#3
                                   "Quel est le nom du premier ministre ?",#4
                                   "C'etait qui le dernier roi de la France ?",#5
                                   "Quel est le nom du président du Brésil ?",#6
                                   "combien il y a t'il de president dans la Veme republique ?",#7
                                   "Il y a combien de pays dans l'union européenne ?",#8
                                   "Nous sommes combien sur terre (arrondi au milliard) ?",]#9

liste_culturegenerale_indices   = ["Regardez le mois de Juillet sur le calendrier",#0
                                   "https://cdn.discordapp.com/attachments/1045779089912508426/1050715887029719071/macron.jpeg",#1
                                   "33_ ",#2
                                   "https://cdn.discordapp.com/attachments/1045779089912508426/1050716011386646529/drapeau_fr.jpeg",#3
                                   "https://cdn.discordapp.com/attachments/1045779089912508426/1050716137115111524/premiere_ministre.jpeg",#4
                                   "https://cdn.discordapp.com/attachments/1045779089912508426/1050715966104948777/louis_p.jpeg",#5
                                   "https://cdn.discordapp.com/attachments/1045779089912508426/1050716193520111626/president_bresil.jpeg",#6
                                   "entre 7 et 10",#7
                                   "_ 7",#8
                                   "7000000000000 ou 8000000000000 ?"]#9

liste_culturegenerale_reponses  = ["14/07",#0
                                   "Macron",#1
                                   "337",#2
                                   "Francais",#3
                                   "Borne",#4
                                   "Louis-Philippe Ier",#5
                                   "Lula",#6
                                   "8",#7
                                   "27",#8
                                   "8000000000000"]#9

liste_lien_salles  = ["https://imgur.com/WgiklLM",
                      "https://cdn.discordapp.com/attachments/1044979907928793108/1051140791537504306/macronsalle.png",
                      "https://cdn.discordapp.com/attachments/1044979907928793108/1051141697846911066/castexchateau.png",
                      "https://cdn.discordapp.com/attachments/1044979907928793108/1051142456810418186/nainchateau.png",
                      "https://cdn.discordapp.com/attachments/1044979907928793108/1051144966723883218/cliochateau.png",
                      "https://cdn.discordapp.com/attachments/1044979907928793108/1051146721394163822/Dec_Gra_chateau_pau_grand_salon_de_reception_JF_Lairez.png",
                      "https://cdn.discordapp.com/attachments/1044979907928793108/1051147826433896568/369348652c6cefcf2cb340e11ca41f33-guedelon-salle-a-manger-1600x900.png",
                      "https://cdn.discordapp.com/attachments/1044965061061517334/1051533906542862386/image.png",
                      "https://cdn.discordapp.com/attachments/1044965061061517334/1051534574808735784/image.png"]

liste_lien_message = ["Gandalf vous accueille ...",
                      "Macron vous accueille ...",
                      "Castex vous accueille ...",
                      "Ce magnifique nain vous accueille ...",
                      "La clio 2021 vous accueille ...",
                      "Depardieu vous accueille ...",
                      "Carlos Ghosn vous accueille ...",
                      "Ce magicien étrange vous accueille ...",
                      "Cette vielle sorcière vous accueille ..."]

liste_gif_bonne_reponse = ["https://tenor.com/view/the-wolf-of-wall-street-clap-clapping-clapping-hands-leonardo-dicaprio-gif-22829304",
                           "https://tenor.com/view/wow-amused-really-clapping-clapping-hands-gif-15245667",
                           "https://tenor.com/view/neil-patrick-harris-thumbs-up-himym-how-i-met-your-mother-barney-stinson-gif-9205895",
                           "https://tenor.com/view/yes-baby-goal-funny-face-gif-13347383",
                           "https://tenor.com/view/good-fine-great-ok-extra-gif-21285390",
                           "https://tenor.com/view/congratulations-gif-18172714",
                           "https://tenor.com/view/ryan-gosling-clapping-applause-amazed-proud-gif-15649965"]

liste_gif_mauvaise_reponse = ["https://tenor.com/view/no-nooo-nope-eat-fingerwag-gif-14832139",
                              "https://tenor.com/view/hell-nah-i-give-you-the-wag-the-finger-wag-gif-13733000",
                              "https://tenor.com/view/no-no-no-no-no-jack-donaghy-30rock-no-nope-gif-19746491",
                              "https://tenor.com/view/no-let-me-think-nope-no-way-hmm-no-gif-22904160",
                              "https://tenor.com/view/cat-no-nonono-noooo-cat-no-gif-25423213",
                              "https://tenor.com/view/baby-angry-eating-mad-grumpy-gif-14328548",
                              "https://tenor.com/view/no-gif-25913746"]

##########################################      LISTE DE QUESTION, INDICE, REPONSE
####################################################################################  
##########################################      FONCTIONs

def timer(liste_premier,liste_deuxieme,time):
  #format heure [hh,mm,ss]
  
  premier_nombre_seconde   = 0
  deuxieme_nombre_seconde  = 0

  premier_nombre_seconde = premier_nombre_seconde + liste_premier[0]*3600
  deuxieme_nombre_seconde = deuxieme_nombre_seconde + liste_deuxieme[0]*3600

  premier_nombre_seconde = premier_nombre_seconde + liste_premier[1]*60
  deuxieme_nombre_seconde = deuxieme_nombre_seconde + liste_deuxieme[1]*60
 
  premier_nombre_seconde = premier_nombre_seconde + liste_premier[2]
  deuxieme_nombre_seconde = deuxieme_nombre_seconde + liste_deuxieme[2]
  
  if (deuxieme_nombre_seconde - premier_nombre_seconde) > time:
    return False
  else:
    return True

def affichage_clé_crochet(x,y):
  finale = ""
  while x > 0:
    finale = finale + ":key: "
    x = x - 1
  while y > 0:
    finale = finale + ":paperclip: "
    y = y -1
  finale = "Votre inventaire :   "+finale
  return finale



##########################################      FONCTIONS
####################################################################################
##########################################      READY

@client.event
async def on_ready():
    print("Le bot est prêt !")

##########################################      READY
####################################################################################
##########################################      VARIABLE PRINCIPALE

etape_du_jeu = 0
statut_attente_une_reponse = False
transition_salle = False
numero_chemin = 0
premiere_manche = True
heure_initiale = 0
heure_finale = 0
bonne_reponse = 0
nb_cle = 0
nb_crochet = 0
joueur_en_partie = 0
attendre_choix_premiere_salle = False
indice_active = False
indice_rand_geo = 0
statut_attente_une_question = False
numero_chemin_mix = 0
score_finale = 0

##########################################      VARIABLE PRINCIPALE
####################################################################################
##########################################      FONCTION PRICIPALE

@client.event
async def on_message(message):

  global etape_du_jeu
  global statut_attente_une_reponse
  global transition_salle
  global numero_chemin
  global premiere_manche
  global heure_initiale
  global heure_finale
  global bonne_reponse
  global nb_cle
  global nb_crochet
  global joueur_en_partie
  global attendre_choix_premiere_salle
  global indice_active
  global indice_rand_geo
  global statut_attente_une_question
  global numero_chemin_mix
  global score_finale

  # le délai entre certain message
  delai_message_introduction = 3
  delai_message_resultat = 5

  # exclure les message venant du bot
  if message.author == client.user and message.content != "restart_the_game":
    return

  #commande permettant de redémarrer une partie
  elif message.content == "restart_the_game" :
    etape_du_jeu = 0
    statut_attente_une_reponse = False
    transition_salle = False
    numero_chemin = 0
    premiere_manche = True
    heure_initiale = 0
    heure_finale = 0
    bonne_reponse = 0
    nb_cle = 0
    nb_crochet = 0
    joueur_en_partie = 0
    attendre_choix_premiere_salle = False
    indice_active = False
    indice_rand_geo = 0
    statut_attente_une_question = False
    numero_chemin_mix = 0
    await message.channel.send("la partie est reinitialisée")
    await message.channel.send("https://imgur.com/5cRooAo")
    return

  # commande permettant de voir l'inventaire
  elif message.content == "mon_inventaire":
    await message.channel.send(f"{affichage_clé_crochet(nb_cle,nb_crochet)}")
    return

  # permet d'empecher une deuxieme partie en même temps
  elif etape_du_jeu >= 1 and message.content == "debut_de_partie" :
    await message.channel.send("la partie est déja lancée")
    return

  # Debut de partie, story telling, introduction
  elif message.content == "debut_de_partie" :
    joueur_en_partie = message.author
    statut_attente_une_reponse = True
    transition_salle = True
    await message.channel.send("**IMPORTANT**\nLES COMMANDES\nrestart_the_game = permet de redémarrer une partie\nmon_inventaire = permet de voir mon inventaire\n!!!! attendez quelques secondes avant de repondre au bot afin qu'il termine son discours !!!!")
    await message.channel.send("\nla partie commence !!!\n\n##############################################\n\n")
    await message.channel.send("Votre objectif est simple, vous incarnez un valeureux chevalier qui devra sauver la princesse qui est enfermée au sommet du château. Mais pour la sauver il vous faudra répondre à une série de questions. Il faut réunir 5 clés pour sauver la princesse. Chaque bonne réponse à une question vous donnera une clé. En cas de difficulté vous aurez le droit à un indice. Cet indice va vous aider à répondre à la question. En revanche vous ne gagnerez pas de clé mais un crochet. Ce crochet permet de crocheter la serrure mais vous n’êtes pas garanti à 100% d’ouvrir la serrure.\n\n")
    await message.channel.send("https://imgur.com/5DOO8Ke")
    time.sleep(delai_message_introduction)
    await message.channel.send(". . .")
    time.sleep(delai_message_introduction)
    await message.channel.send("vous rentrez dans le chateau")
    await message.channel.send("https://imgur.com/kgAtR2w")
    time.sleep(delai_message_introduction)
    await message.channel.send(". . .")
    time.sleep(delai_message_introduction)
    await message.channel.send("4 chemins sont en faces de vous")
    await message.channel.send("https://imgur.com/TmSnPSc")
    time.sleep(delai_message_introduction)
    await message.channel.send(". . .\n1 = math\n2 = géo\n3 = culture générale\n4 = mix")
    attendre_choix_premiere_salle = True
    return
  
  # permet d'empecher quelqu'un d'interrompre une partie
  if etape_du_jeu >= 1 and joueur_en_partie != message.author :
    await message.channel.send("vous n'etes pas le joueur en partie ...")
    return

  # permet de rentrer dans la "boucle" des 5 manches
  if etape_du_jeu >= 0 and etape_du_jeu <= 5:
    # permet de verifier qu'il ne rentre pas un autre chiffre lorsque le bot lui demande de choisir son chemin
    if attendre_choix_premiere_salle == True :
      if (not (int(message.content) in [1,2,3,4])) and statut_attente_une_reponse == True and transition_salle == True :
        await message.channel.send("merci de renseigner la bonne valeur")
        return
      # le choix du chemin est validé
      if (int(message.content) in [1,2,3,4]) and statut_attente_une_reponse == True and transition_salle == True :
        numero_chemin = int(message.content)
        statut_attente_une_reponse = False
        etape_du_jeu = 1
        attendre_choix_premiere_salle = False
        await message.channel.send(f"la porte choisi est : {numero_chemin}")
        if message.content == 4:
          chemin_mix= True
    
    # transition après le choix de la premiere porte
    if etape_du_jeu == 1: 
      if numero_chemin == 1 and premiere_manche == True: # math premier choix
        await message.channel.send("vous vous dirigez vers la porte mathématique du chateau ...")
        await message.channel.send("https://imgur.com/wQHtiu9")
        premiere_manche = False
     
      if numero_chemin == 2 and premiere_manche == True: # géo premier choix
        await message.channel.send("vous vous dirigez vers la porte géograpie du chateau ...")
        await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050785682026680370/versgeo.png")
        premiere_manche = False

      if numero_chemin == 3 and premiere_manche == True: # culture G premier choix
        await message.channel.send("vous vous dirigez vers la porte culture G du chateau ...")
        await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050785681695318086/vers_culture_g.png")
        premiere_manche = False

      if numero_chemin == 4 and premiere_manche == True: # mix premier choix
        await message.channel.send("vous vous dirigez vers la porte mix du chateau ...")
        await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050785681351393280/versmix.png")
        premiere_manche = False

    # entrée dans la salle, un personnage nous attends
    if statut_attente_une_reponse == False and transition_salle == True:

      salle_aleatoire = random.randint(0,len(liste_lien_salles)-1)
      await message.channel.send(". . .")
      await message.channel.send(liste_lien_salles[salle_aleatoire])
      await message.channel.send(liste_lien_message[salle_aleatoire])
      transition_salle = False
      statut_attente_une_reponse = False
      statut_attente_une_question = True
    
    else :
      statut_attente_une_question = False

    ####################################################################################### 
    #############################     CHEMIN MIIIIIX
    if numero_chemin == 4 and statut_attente_une_reponse == False: 
      if (not indice_active) and statut_attente_une_question:
        numero_chemin_mix = random.randint(1,3)

    #############################     CHEMIN MIIIIIX
    ####################################################################################### 
    #############################     CHEMIN MATH
    

    if (numero_chemin == 1 or numero_chemin_mix == 1) and statut_attente_une_reponse == False: 
     
      if (not indice_active) and statut_attente_une_question:
        heure_initiale = datetime.datetime.now()
        heure_initiale = [heure_initiale.hour,heure_initiale.minute,heure_initiale.second]
        heure_finale = 0
        
        premier_nombre = random.randint(0,10)
        deuxieme_nombre = random.randint(0,10)
        bonne_reponse = str(premier_nombre * deuxieme_nombre)

        await message.channel.send(f"combien font {premier_nombre} x {deuxieme_nombre}.\nVous avez 20 sencondes ..." )
        await message.channel.send("vous pouvez taper ' indice ' pour demander un indice !!!")
        statut_attente_une_question = False
        statut_attente_une_reponse = True
        return
        
    
    if (numero_chemin == 1 or numero_chemin_mix == 1) and statut_attente_une_reponse == True:
      heure_finale = datetime.datetime.now()
      heure_finale = [heure_finale.hour,heure_finale.minute,heure_finale.second]
      
      if not timer(heure_initiale,heure_finale,20):
        await message.channel.send("temps écoulé ...\nIl vous laisse passé mais ne vous donna pas la clé ...")
        etape_du_jeu = etape_du_jeu + 1
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

        
      elif message.content == "indice":

        await message.channel.send(f"Le dernier chiffre est : {bonne_reponse[-1]}")
        heure_initiale = datetime.datetime.now()
        heure_initiale = [heure_initiale.hour,heure_initiale.minute,heure_initiale.second]
        indice_active = True
        statut_attente_une_reponse = True

      elif message.content == bonne_reponse:

        etape_du_jeu = etape_du_jeu + 1
        if indice_active:
          nb_crochet = nb_crochet + 1
          await message.channel.send("Bonne réponse vous gagné un crochet !!!")
        else:
          nb_cle = nb_cle + 1
          await message.channel.send("Bonne réponse vous gagné une clé !!!")
        await message.channel.send(liste_gif_bonne_reponse[random.randint(0,len(liste_gif_bonne_reponse)-1)])
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

      elif message.content != bonne_reponse:
        await message.channel.send("Mauvaise réponse ...")
        await message.channel.send(liste_gif_mauvaise_reponse[random.randint(0,len(liste_gif_mauvaise_reponse)-1)])
        await message.channel.send(f"la bonne réponse était {bonne_reponse}")
        etape_du_jeu = etape_du_jeu + 1
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True
    #############################     CHEMIN MATH
    ####################################################################################### 
    #############################     CHEMAIN GEO

    if (numero_chemin == 2 or numero_chemin_mix == 2) and statut_attente_une_reponse == False:
      if (not indice_active) and statut_attente_une_question:
        heure_initiale = datetime.datetime.now()
        heure_initiale = [heure_initiale.hour,heure_initiale.minute,heure_initiale.second]
        heure_finale = 0
        

        indice_rand_geo = random.randint(0,len(liste_geographie_questions)-1)
        await message.channel.send(f"la question est la suivante ...\n\n{liste_geographie_questions[indice_rand_geo]}\nVous avez 20 sencondes ...")
        await message.channel.send("vous pouvez taper ' indice ' pour demander un indice !!!")
        statut_attente_une_question = False
        statut_attente_une_reponse = True
        return
        
    
    if (numero_chemin == 2 or numero_chemin_mix == 2) and statut_attente_une_reponse == True:
      heure_finale = datetime.datetime.now()
      heure_finale = [heure_finale.hour,heure_finale.minute,heure_finale.second]

      if not timer(heure_initiale,heure_finale,20):
        await message.channel.send("temps écoulé ...\nIl vous laisse passé mais ne vous donna pas la clé ...")
        etape_du_jeu = etape_du_jeu + 1
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

      elif message.content == "indice":
        await message.channel.send(liste_geographie_indices[indice_rand_geo])
        heure_initiale = datetime.datetime.now()
        heure_initiale = [heure_initiale.hour,heure_initiale.minute,heure_initiale.second]
        indice_active = True
        statut_attente_une_reponse = True
      
      elif message.content.lower() == liste_geographie_reponses[indice_rand_geo].lower():
        etape_du_jeu = etape_du_jeu + 1
        if indice_active:
          nb_crochet = nb_crochet + 1
          await message.channel.send("Bonne réponse vous gagné un crochet !!!")
        else:
          nb_cle = nb_cle + 1
          await message.channel.send("Bonne réponse vous gagné une clé !!!")
        await message.channel.send(liste_gif_bonne_reponse[random.randint(0,len(liste_gif_bonne_reponse)-1)])
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

      elif message.content.lower() != liste_geographie_reponses[indice_rand_geo].lower():
        await message.channel.send("Mauvaise réponse ...")
        await message.channel.send(liste_gif_mauvaise_reponse[random.randint(0,len(liste_gif_mauvaise_reponse)-1)])
        await message.channel.send(f"la bonne réponse était {liste_geographie_reponses[indice_rand_geo]}")
        etape_du_jeu = etape_du_jeu + 1
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

    #############################     CHEMAIN GEO
    ####################################################################################### 
    #############################     CHEMIN CULTURE G

    if (numero_chemin == 3 or numero_chemin_mix == 3) and statut_attente_une_reponse == False: 
      if (not indice_active) and statut_attente_une_question:
        heure_initiale = datetime.datetime.now()
        heure_initiale = [heure_initiale.hour,heure_initiale.minute,heure_initiale.second]
        heure_finale = 0
        

        indice_rand_geo = random.randint(0,len(liste_culturegenerale_questions)-1)
        await message.channel.send(f"la question est la suivante ...\n\n{liste_culturegenerale_questions[indice_rand_geo]}\nVous avez 20 sencondes ...")
        await message.channel.send("vous pouvez taper ' indice ' pour demander un indice !!!")
        statut_attente_une_question = False
        statut_attente_une_reponse = True
        return
        
    
    if (numero_chemin == 3 or numero_chemin_mix == 3) and statut_attente_une_reponse == True:
      heure_finale = datetime.datetime.now()
      heure_finale = [heure_finale.hour,heure_finale.minute,heure_finale.second]

      if not timer(heure_initiale,heure_finale,20):
        await message.channel.send("temps écoulé ...\nIl vous laisse passé mais ne vous donna pas la clé ...")
        etape_du_jeu = etape_du_jeu + 1
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

      elif message.content == "indice":
        await message.channel.send(liste_culturegenerale_indices[indice_rand_geo])
        heure_initiale = datetime.datetime.now()
        heure_initiale = [heure_initiale.hour,heure_initiale.minute,heure_initiale.second]
        indice_active = True
        statut_attente_une_reponse = True
      
      elif message.content.lower() == liste_culturegenerale_reponses[indice_rand_geo].lower():
        etape_du_jeu = etape_du_jeu + 1
        if indice_active:
          nb_crochet = nb_crochet + 1
          await message.channel.send("Bonne réponse vous gagné un crochet !!!")
        else:
          nb_cle = nb_cle + 1
          await message.channel.send("Bonne réponse vous gagné une clé !!!")
        await message.channel.send(liste_gif_bonne_reponse[random.randint(0,len(liste_gif_bonne_reponse)-1)])
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

      elif message.content.lower() != liste_culturegenerale_reponses[indice_rand_geo].lower():
        await message.channel.send("Mauvaise réponse ...")
        await message.channel.send(liste_gif_mauvaise_reponse[random.randint(0,len(liste_gif_mauvaise_reponse)-1)])
        await message.channel.send(f"la bonne réponse était {liste_culturegenerale_reponses[indice_rand_geo]}")
        etape_du_jeu = etape_du_jeu + 1
        await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
        await message.channel.send("\nhttps://imgur.com/sVgtrkh")
        await message.channel.send("Tapez 'monter_les_escaliers'pour continuer ...")
        indice_active = False
        statut_attente_une_reponse = False
        transition_salle = True
        statut_attente_une_question = True

    #############################     CHEMIN CULTURE G
    ####################################################################################### 
    #############################     RESULTAT

  else :
    score_finale = nb_cle + nb_crochet*0.5
    await message.channel.send("vous êtes arrivé dans la derniere ligne droite ...")
    await message.channel.send("https://cdn.discordapp.com/attachments/1044979907928793108/1050718154566942771/image.png")
    await message.channel.send("vous arrivé devant la porte avec 5 serrures ...")
    await message.channel.send("https://cdn.discordapp.com/attachments/1044979907928793108/1050719281094078464/porte_de_rhodes.png")
    await message.channel.send("vous ouvrez votre sac ...")
    await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050742843905421312/image.png")
    await message.channel.send(affichage_clé_crochet(nb_cle,nb_crochet))
    if nb_cle + nb_crochet != 5:
      await message.channel.send("vous n'avez pas assez d'items ....\n la princesse est condamnée à rester coincée à jamais ...")
      await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050744690300944405/princessemorte.png")
      await message.channel.send(f"score finale est = {score_finale}/5")
      time.sleep(delai_message_resultat)
      await message.channel.send("restart_the_game")
      await message.channel.send("vous pouvez taper debut_de_partie pour recommencer une partie") 
    elif nb_cle == 5:
      await message.channel.send("LA PRINCESSE EST SAUVEEEE")
      await message.channel.send(f"score finale est = {score_finale}/5")
      await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050748731718369380/image.png")
      time.sleep(delai_message_resultat)
      await message.channel.send("restart_the_game")
      await message.channel.send("vous pouvez taper debut_de_partie pour recommencer une partie")
    else:
      await message.channel.send("il vous manque quelque clé ... cependant vous pouvez essayer de les crocheter avec vos crochets ...")
      await message.channel.send(f"actuellement vous pouvez déjà ouvrir {nb_cle} serrures, il vous reste donc {5-nb_cle} serrures a ouvrir. vous avez 75% de chance de crocheter une serrure")
      for i in range(nb_crochet):
        chiffre_aleatoire = random.randint(1,100)
        if chiffre_aleatoire <= 75:
          await message.channel.send(f"\n**VOUS AVEZ REUSSI A CROCHETER UNE SERRURE !!!!\**nil vous reste {nb_crochet-i-1} serrure")
          time.sleep(delai_message_resultat)
        else:
          await message.channel.send("vous n'avez pas reussi ... votre crochet s'est cassé ...\n")
          time.sleep(delai_message_resultat)
          await message.channel.send("vous n'avez plus assez d'items ....\n la princesse est condamnée à rester coincée à jamais ...")
          await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050744690300944405/princessemorte.png")
          await message.channel.send(f"score finale est = {score_finale}/5")
          await message.channel.send("restart_the_game")
          await message.channel.send("vous pouvez taper debut_de_partie pour recommencer une partie") 
          return
      await message.channel.send("LA PRINCESSE EST SAUVEEEE")
      await message.channel.send(f"score finale est = {score_finale}/5")
      await message.channel.send("https://cdn.discordapp.com/attachments/1044965061061517334/1050748731718369380/image.png")
      time.sleep(delai_message_resultat)
      await message.channel.send("restart_the_game")
      await message.channel.send("vous pouvez taper debut_de_partie pour recommencer une partie")
        
client.run("")