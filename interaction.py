##################################################
# Gabriel Desmullier
# Projet Python RPG 2019
##################################################



import random





def combat(hero,monster):
    # auteur: Gabriel
    # fonction qui realise le combat entre le hero est un monstre
    print("VOUS ALLEZ DEVOIR AFFRONTER: "+monster.name)
    print(monster.displayMonster())
    #presentation du combat et du monstre
    #le joueur doit pouvoir avoir acces a l'inventaire actif du monstre ou acces directement au combat
    print("\n\n1: VOIR L'EQUIPEMENT DU MONSTRE\n2: COMMENCER LE COMBAT")
    print("ENTREZ LE NUMERO DE L'ACTION")
    choix=str(input())
    while choix!="1" and choix!="2":
        print("ENTREZ LE NUMERO DE L'ACTION")
        choix = str(input())

    if choix=="1": #affiche de l'inventaire actif du monstre
          print("\n")
          monster.inventory.displayInventoryActive()
          print("2: COMMENCER LE COMBAT")
          while choix!="2":
            print("ENTREZ LE NUMERO DE L'ACTION")
            choix = str(input())

    if choix=="2": #sinon le combat commence
        monsterEffort=100 #au debut de chaque combat chaque adversaire a une barre d'effort une action coutera de l'effort
        heroEffort=100
        #le combat s'articule autour d'un nombre illimité de tour de jeu où le joueur joue puis c'est autour du monstre
        #au debut de chaque tour affichage des nom + de la santé
        while monster.health>0 and hero.health>0: #les combats vont jusqu'à la mort de l'un des adversaires
            print("\n\n"+monster.name+"      VS      "+hero.name)
            print("Sante: "+str(monster.health)+"             "+str(hero.health))
            print("Effort: "+str(monsterEffort)+"             "+str(heroEffort))
            print("\n\n")


            #TOUR DU HERO
            #affichage des actions possibles
            print("\nA VOTRE TOUR: ")
            print("\n1: TAILLE     -20 effort")
            print("\n2: ESTOC      -30 effort")
            print("\n3: COUP MAGIC -20 effort -20 MP")
            if (monster.health<10):
              print("\n4: COUP DE GRACE")
            else:
              print("\n4: NE RIEN FAIRE +30 effort")

            #choix du joueur
            print("ENTREZ LE NUMERO DE L'ACTION")
            choix = str(input())
            while choix != "1" and choix != "2" and choix!="3" and  choix!="4":
                print("ENTREZ LE NUMERO DE L'ACTION")
                choix = str(input())

            if choix=="1": #pour la taille et l'estoc les chances de parevenir sont les mêmes
                if heroEffort>20:
                   heroEffort=heroEffort-20
                   coup=random.randint(1,100)
                   if coup<hero.dodge_chance: #savoir si le coup porte a reussi

                       parryMonster=random.randint(1,100) #savoir si le coup est paré par le monstre
                       if parryMonster<monster.parry_chance and monsterEffort>=10: #si le monstre peut parer
                           monsterEffort = monsterEffort - 10 #il parre mais avec effort
                           print("\nLe coup de taille a ete pare par votre adversaire\n")
                       else: #le coup est porte est-ce qu'il s'agit d'un coup critique?
                           scaleDamage = hero.max_attack - hero.min_attack
                           tier = int(scaleDamage / 3)

                           coupCritique=random.randint(1,100)
                           if coupCritique<hero.critical_hit_chance: #si le coup critique est valide
                                  print("\nCoup critique!\n")

                                  damage=random.randint(hero.min_attack+tier,hero.max_attack-tier)# le coup critique en taille inflige entre min+1/3 et  min+2/3
                                  damage=int(damage-monster.armor/100*damage) #l'armure reduit les damages
                                  monster.health=monster.health-damage
                           else:
                                  print("\nLe coup de taille a atteint l'ennemi!\n")

                                  damage=random.randint(hero.min_attack,hero.min_attack+tier) #un coup non critique inflige moins de degats entre min et min+1/3
                                  damage = int(damage - monster.armor / 100 * damage)  # l'armure reduit les damages
                                  monster.health = monster.health - damage
                   else:
                    print("\nEchec de l'attaque\n")
                else:
                      print("\nVous etes essoufle, repossez vous\n")
                      heroEffort=heroEffort+10  #apres avoir tente un coup de taille le hero gagne regagne un peu de force


            elif choix=="2": #le coup d'estoc inflige plus de dommages s'il n'est pas parré par l'adversaire
                if heroEffort > 30:
                    heroEffort = heroEffort - 30
                    coup = random.randint(1, 100)
                    if coup < hero.dodge_chance:  # savoir si le coup porte a reussi

                         parryMonster = random.randint(1, 100)  # savoir si le coup est paré par le monstre
                         if parryMonster < monster.parry_chance and monsterEffort >= 10:  # si le monstre peut parer
                             monsterEffort = monsterEffort - 10  # il parre mais avec effort
                             print("\nLe coup d'estoc a ete pare par votre adversaire\n")
                         else:  # le coup est porte est-ce qu'il s'agit d'un coup critique?
                               scaleDamage = hero.max_attack - hero.min_attack
                               tier = int(scaleDamage / 3)
                               coupCritique = random.randint(1, 100)
                               if coupCritique < hero.critical_hit_chance:  # si le coup critique est valide
                                    print("\nCoup critique!\n")

                                    damage = random.randint(hero.max_attack-tier,hero.max_attack )# le coup critique en estoc inflige plus de dégats entre min+2/3 et max
                                    damage = int(damage - monster.armor / 100 * damage)  # l'armure reduit les damages
                                    monster.health = monster.health - damage
                               else:
                                    print("\nLe coup d'estoc a atteint l'ennemi!\n")

                                    damage = random.randint(hero.min_attack+tier, hero.max_attack - tier) #coup normal en estoc entre min+1/3 et min+2/3
                                    damage = int(damage - monster.armor / 100 * damage)  # l'armure reduit les damages
                                    monster.health = monster.health - damage
                    else:
                       print("\nEchec de l'attaque\n")

                else:
                     print("\nVous etes essoufle, repossez vous\n")
                     heroEffort = heroEffort + 10  # apres avoir tente un coup de taille le hero gagne regagne un peu de force

            elif choix=="3": #le coup magique ne peut etre parre et inflinge forcement des degats a l'ennemi
                if heroEffort>20 and hero.magic_points>20:
                   heroEffort = heroEffort - 20
                   hero.magic_points=hero.magic_points-20
                   scaleDamage = hero.max_attack - hero.min_attack
                   damage=random.randint(hero.min_attack,hero.min_attack+int(scaleDamage / 2)) #le coup magique n'est pas tres fort
                   monster.health = monster.health - damage
                   print("\nVotre adversaire a subit des degats!\n")
                else:
                    print("\nVous n'etes pas en capacite de lancer cette attaque\n")
                    heroEffort = heroEffort + 10  # apres avoir tente une attaque magique le hero gagne regagne un peu de force

            elif choix=="4":
                if (monster.health < 10): #le coup de grace tue le monstre directement
                    monster.health=0
                    print("\nLe coup de grace a ete porte!\n")

                else: #ne rien faire
                    heroEffort=heroEffort+30
                    print("\nIl faut rester concentrer...\n")

            #TOUR DU MONSTRE
            print("TOUR DE VOTRE ADVERSAIRE")
            #le monstre n'a pas de coup magique
            if hero.health<10: #le monstre donne le coup de grace au hero des qu'il peut
                hero.health=0
                print("\nVotre adversaire vous a donne le coup de grace!\n")

            elif monsterEffort<30: #s'il est essoufle, il se repose
                monsterEffort=monsterEffort+30
                print("\nVotre adversaire n'a rien tente...\n")

            else: #dans les autres cas le monstre fait un coup de taille ou un coup d'estoc (aleatoire)
                monstreAction=random.randint(1,2)
                if monstreAction==1: #coup de taille = meme principe que pour le hero
                    monsterEffort = monsterEffort - 20
                    coup = random.randint(1, 100)
                    if coup < monster.dodge_chance:  # savoir si le coup porte a reussi
                        #on demande au hero s'il veut parer
                        if heroEffort > 10: #et si il en a la capacite
                            print(
                                "\nVotre adversaire donne un coup de taille\n\nVOULEZ VOUS TENTER DE PARER (-10 EFFORT)\n1: OUI\n2: NON")
                            print("ENTREZ LE NUMERO DE L'ACTION")
                            choixParer = str(input())
                            while choixParer != "1" and choixParer != "2":
                                print("ENTREZ LE NUMERO DE L'ACTION")
                                choixParer = str(input())

                            if choixParer == "1":  #il peut essayer de parrer
                                heroEffort = heroEffort - 10
                                parryHero = random.randint(1, 100)
                                if parryHero < hero.parry_chance:
                                    print("\nLe coup a ete pare\n")
                                else: #sinon on passe la variable choixParer a 2 comme si il avait choisi de ne rien faire
                                    print("\nVous n'avez pas reussi a parer le coup\n")
                                    choixParrer = "2"

                        else: #si le joueur n'a pas la force de parrer on met chixParrer a 2 pour subir le coup
                          choixParer = "2"
                          print("\nVotre adversaire tente de vous donner un coup de taille\n")

                        if choixParer == "2": #le coup est subit (la prise en charge des degats se fait comme pour le hero)
                            scaleDamage = monster.max_attack - monster.min_attack
                            tier = int(scaleDamage / 3)
                            coupCritique = random.randint(1, 100)
                            if coupCritique < monster.critical_hit_chance:  # si c'est un coup critique (comme le hero...)
                                print("\nVous avez subit un coup critique\n!")

                                damage = random.randint(monster.min_attack +tier,monster.max_attack - tier)
                                damage = int(damage - hero.armor / 100 * damage)  # l'armure reduit les damages
                                hero.health = hero.health - damage
                            else:
                                print("\nLe coup de taille vous a atteint!\n")

                                damage = random.randint(monster.min_attack, monster.min_attack+tier)
                                damage = int(damage - hero.armor / 100 * damage)  # l'armure reduit les damages
                                hero.health = hero.health - damage
                    else:
                        print("\nVotre adversaire a rate son attaque\n")

                elif monstreAction==2: #coup d'estoc = meme principe que pour le hero
                    monsterEffort = monsterEffort - 20
                    coup = random.randint(1, 100)
                    if coup < monster.dodge_chance:  # savoir si le coup porte a reussi
                        #on demande au hero s'il veut parrer
                         if heroEffort>10:
                             print("\nVotre adversaire donne un coup d'estoc'\n\nVOULEZ VOUS TENTER DE PARER (-10 EFFORT)\n1: OUI\n2: NON")
                             print("ENTREZ LE NUMERO DE L'ACTION")
                             choixParer = str(input())
                             while choixParer != "1" and choixParer != "2":
                               print("ENTREZ LE NUMERO DE L'ACTION")
                               choixParer = str(input())

                             if choixParer=="1":
                                heroEffort=heroEffort-10
                                parryHero=random.randint(1,100)
                                if parryHero<hero.parry_chance:
                                   print("\nLe coup a ete pare\n")
                                else:
                                   print("\nVous n'avez pas reussi a parer le coup\n")
                                   choixParer="2"

                         else:
                             choixParer="2"
                             print("\nVotre adversaire tente de vous donner un coup d'estoc\n")

                         if choixParer=="2":
                            coupCritique = random.randint(1, 100)
                            scaleDamage = monster.max_attack - monster.min_attack
                            tier = int(scaleDamage / 3)
                            if coupCritique < monster.critical_hit_chance:  # si le coup critique est valide
                                print("\nVous avez subit un coup critique!\n")

                                damage = random.randint(monster.max_attack-tier,monster.max_attack)
                                damage = int(damage - hero.armor / 100 * damage)  # l'armure reduit les damages
                                hero.health = hero.health - damage
                            else:
                                print("\nLe coup d'estoc' vous a atteint!\n")

                                damage = random.randint(monster.min_attack+tier, monster.max_attack - tier)
                                damage = int(damage - hero.armor / 100 * damage)  # l'armure reduit les damages
                                hero.health = hero.health - damage
                    else:
                        print("\nVotre adversaire a rate son attaque\n")

        if monster.health<=0:
            print("Victoire!")
            return True
        elif hero.health<=0:
            return False





def interactionMerchant(hero,merchant):
    #Auteur: Gabriel Desmullier
    #Interaction entre le hero et un marchand
    print("VOUS AVEZ RENCONTRE UN MARCHAND")
    choix="5"
    while choix!="3": #Tant que le joueur n'a pas fini de commercer on lui propose ces actions
        print("QUE VOULEZ VOUS FAIRE?\n1: ACHETER UN OBJET\n2: VENDRE UN OBJECT\n3: NE RIEN FAIRE")

        #saisie du choix
        print("ENTREZ LE NUMERO DE L'ACTION")
        choix=str(input())
        while choix!="1" and choix!="2" and choix!="3":
            print("ENTREZ LE NUMERO DE L'ACTION")
            choix = str(input())

        if choix =="1": #si le joueur souhaite acheter le marchand montre son inventaire inactif
            taille = len(merchant.inventory.objectList)
            choix2=100
            while choix2!=taille:          #le joueur voit affiche la totalite de l'inventaire du marchand  et doit entrer le numero pour voir l'objet ou entrer taille+1 pour terminer
                merchant.inventory.displayInventoryInactive()
                print("ENTREZ LE NUMERO DE L'OBJET OU "+str(taille)+" POUR RETOURNER EN ARRIERE")

                #choix de l'objet a voir ou fin du commerce
                choix2=int(input())
                while choix2<0 or choix2>taille:
                    print("ENTREZ LE NUMERO DE L'OBJET OU " + str(taille ) + " POUR RETOURNER EN ARRIERE")
                    choix2 = int(input())

                if choix2!=taille: #si c'est un objet on affiche les caracteristiques et on propose de l'acheter
                    merchant.inventory.displayAnItemFromYourInventoryInactive(choix2)
                    objet=merchant.inventory.objectList[choix2]

                    #saisie de l'action acheter ou non
                    print("\n1: ACHETER L'OBJET (votre argent: "+hero.inventory.gold+" bitcoins)\n2: RETOUR")
                    choix3=str(input())
                    while choix3!="1" and choix3!="2":
                        print("\n1: ACHETER L'OBJET (votre argent: "+hero.inventory.gold+" bitcoins)\n2: RETOUR")
                        choix3 = str(input())

                    if choix3=="1": #si le joueur choisit d'acheter
                        if hero.inventory.gold>= objet.goldValue: #on verifit qu'il a assez d'argent
                             hero.inventory.buyAnObject(objet) #il achete donc l'objet
                             merchant.inventory.removeItemFromInventory(choix2) #le marchand perd l'objet

                        else:
                            print("VOUS N'AVEZ PAS ASSEZ D'ARGENT POUR ACQUERIR CET OBJET\n")

        elif choix=="2": #si le joueur souhaite vendre il ouvre son inventaire inactif

            taille = len(hero.inventory.objectList)
            choix2 = 100
            while choix2 != taille:  # le joueur voit affiche la totalite de l'inventaire du marchand  et doit entrer le numero pour voir l'objet ou entrer taille+1 pour terminer
                hero.inventory.displayInventoryInactive()
                print("ENTREZ LE NUMERO DE L'OBJET OU " + str(taille ) + " POUR RETOURNER EN ARRIERE")

                # choix de l'objet a voir ou fin du commerce
                choix2 = int(input())
                while choix2 < 0 or choix2 > taille :
                    print("ENTREZ LE NUMERO DE L'OBJET OU " + str(taille ) + " POUR RETOURNER EN ARRIERE")
                    choix2 = int(input())

                if choix2 != taille :  # si c'est un objet on affiche les caracteristiques et on propose de l'acheter
                    hero.inventory.displayAnItemFromYourInventoryInactive(choix2)
                    objet = hero.inventory.objectList[choix2]

                    # saisie de l'action de vendre ou non
                    print("\n1: VENDRE L'OBJET\n2: RETOUR")
                    choix3 = str(input())
                    while choix3 != "1"and choix3 != "2":
                        print("\n1: VENDRE L'OBJET\n2: RETOUR")
                        choix3 = str(input())

                    if choix3 == "1":  # si le joueur choisit de vendre
                        #pas de conditions d'argent cette fois-ci mais le prix a la revente est divise par deux
                        hero.inventory.sellAnObject(choix2)
                        merchant.inventory.addItemToInventory(objet) #le marchand recupere l'objet




def gestionInventaire(hero):
    #auteur: Gabriel Desmullier
    #permet au joueur de gerer son inventaire
    choix="5"
    while choix!="3":#tant que le joueur ne choisit pas retour au jeu on lui propose les actions
        print("\nACCES A L'INVENTAIRE:\n1: INVENTAIRE INACTIF\n2: INVENTAIRE ACTIF\n3: RETOUR\n")
        choix = str(input())
        while choix!="1" and choix!="2" and choix!="3": #saisie du choix
            print("\nACCES A L'INVENTAIRE:\n1: INVENTAIRE INACTIF\n2: INVENTAIRE ACTIF\n3: RETOUR\n")
            choix=str(input())

        if choix=="1": #c'est depuis l'inventaire inactif que le joueur peut prendre des consommables, ou s'equipper
            hero.inventory.displayInventoryInactive() #on affiche l'inventaire inactif
            taille=len(hero.inventory.objectList)
            #on lui permet de regarder un objet
            choix2=100
            while choix2<0 or choix2>taille:
                 print("ENTREZ LE NUMERO DE L'OBJET OU "+str(taille)+" POUR RETOUR\n")
                 choix2=int(input())

            if choix2!=taille: #si le numero correspond à un objet on affiche les caractéristiques
                hero.inventory.displayAnItemFromYourInventoryInactive(choix2)
                objet = hero.inventory.objectList[choix2]  #pour chaque objet l'action 1 est differente on affiche le string de l'action

                if str(objet.__class__)=="<class 'Objet.Weapon'>":
                    print("\n1: PRENDRE l'ARME")

                elif str(objet.__class__)=="<class 'Objet.Armor'>":
                    print("\n1: S'EQUIPER")

                elif str(objet.__class__) == "<class 'Objet.Jewel'>":
                    print("\n1: S'EQUIPER")

                elif str(objet.__class__) == "<class 'Objet.Consumable'>":
                    print("\n1: CONSOMMER")

                print("2: RETOUR")
                #choix de l'action
                choix3="3"
                while choix3!="1" and choix3!="2":
                    print("CHOISISSEZ UNE ACTION:\n")
                    choix3=str(input())

                if choix3=="1": #le choix 1 correspond a une multitude de fonctions
                    if str(objet.__class__)=="<class 'Objet.Weapon'>": #si c'est une arme
                        hero.inventory.addWeapon(choix2,hero)

                    elif str(objet.__class__) == "<class 'Objet.Armor'>": #si c'est une armure on doit determiner dans quel slot on la range
                        if objet.armorSlot=="head":
                            hero.inventory.equipHead(choix2,hero)
                        elif objet.armorSlot=="arms":
                            hero.inventory.equipArms(choix2,hero)
                        elif objet.armorSlot=="legs":
                            hero.inventory.equipLegs(choix2,hero)
                        elif objet.armorSlot=="chest":
                            hero.inventory.equipChest(choix2,hero)
                        elif objet.armorSlot=="pants":
                            hero.inventory.equipPants(choix2,hero)

                    elif str(objet.__class__) == "<class 'Objet.Jewel'>":
                        hero.inventory.addJewel(choix2,hero)

                    elif str(objet.__class__) == "<class 'Objet.Consumable'>": #si c'est un consomable, on le consomme
                        hero.inventory.consumeConsumable(choix2,hero)


        elif choix=="2": #si le choix est 2 on affiche l'inventaire actif
             hero.inventory.displayInventoryActive()
              #on aurait pu par la suite lui permettre d'atteindre les objets de l'inventaire actif



def actionJoueur(hero,level):
    #auteur Gabriel Desmullier
    #interaction d'un personnage avec le jeu: acces inventaire ou deplacement
    key=str(input())

    if key == "z":
            level.movehero(hero, [-1, 0])
    elif key == "s":
            level.movehero(hero,[1, 0])
    elif key == "d":
            level.movehero(hero,[0, 1])
    elif key == "q":
            level.movehero(hero,[0, -1])
    elif key=="a":
            gestionInventaire(hero)
    elif key=="e":
          hero.afficher_stats()
    #codes triches
    elif key=="LifeForever": #code triche vie au maximum
        hero.health = 150
    elif key=="Indestructible": #code triche invincible: pour parrer la totalite des coups de l'ennemi
        hero.parry_chance=100
        hero.armor = 100
    elif key=="Master":#code triche maitre! : des coups 100% gagnants
        hero.dodge_chance=100
        hero.critical_hit_chance=100
        hero.parry_chance = 100
    elif key=="TimeIsMoney": #code triche pour avoir beaucoup d'argent
        hero.inventory.gold=100000
    elif key=="Speed": #augmente la vitesse
        hero.speed=3
    elif key=="Suicide": #fonction tentative de suicide
        hero.health=0















