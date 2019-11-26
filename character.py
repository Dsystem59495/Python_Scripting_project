##################################################
# Gabriel Desmullier
# Projet Python RPG 2019
##################################################

import random

import Objet as ob





#classe de l'inventaire
class Inventory():
    # auteur Gabriel Desmullier


    def __init__(self,id):
        # auteur Gabriel Desmullier
        #initialisation des espaces de l'inventaire avec l'inventaire inactif= listes d'objets non utilise et inventaire actif=equipement
        self.id=id
        self.objectList = []  # listes des objects possedes
        self.gold = 10
        self.handSlot = []
        self.headSlot = []
        self.chestSlot = []
        self.pantsSlot = []
        self.armsSlot = []
        self.legsSlot = []
        self.jewelSlot = []





    def earnGold(self,value):
        # auteur Gabriel Desmullier
        #ajoute de l'or
        self.gold=self.gold+value

    def loseGold(self,value):
        # auteur Gabriel Desmullier
        #perdre de l'or
        self.gold=self.gold-value

    def displayInventoryInactive(self):
        # auteur Gabriel Desmullier
        #afficher tous les elements de l'inventaire(uniquement ceux qui ne sont pas portes)
        print("OBJETS DE L'INVENTAIRE INACTIF:")
        for i in range (len(self.objectList)):
            print(str(i)+": "+self.objectList[i].name)


    def displayAnItemFromYourInventoryInactive(self,indice):
        # auteur Gabriel Desmullier
        #afficher un element non porte de l'inventaire
        print("OBJET DANS L'INVENTAIRE INACTIF:")
        self.objectList[indice].display()

    def addItemToInventory(self,object):
        # auteur Gabriel Desmullier
        #ajouter gratuitement un objet a l'inventaire
        self.objectList.append(object)

    def removeItemFromInventory(self,indice):
        # auteur Gabriel Desmullier
        #retirer un objet de l'inventaire
        del [self.objectList[indice]]


    def buyAnObject(self,object):
        # auteur Gabriel Desmullier
        #acheter un objet et le mettre dans l'inventaire
        if object.goldValue>self.gold:
            print("VOUS N'AVEZ PAS ASSEZ D'ARGENT POUR ACHETER CET OBJET")
        else:
            self.loseGold(object.goldValue)
            self.addItemToInventory(object)

    def sellAnObject(self,indice):
        # auteur Gabriel Desmullier
        #vendre un objet et le retirer de l'inventaire
        self.earnGold(round(self.objectList[indice].goldValue/2)) #ah! les prix du marche de l'occasion! divise par deux
        del[self.objectList[indice]]
        print("VOUS VENEZ DE VENDRE UN OBJET")

    def displayInventoryActive(self):
        # auteur Gabriel Desmullier
        #affiche l'inventaire actif
        print("INVENTAIRE ACTIF:")
        print("ARMES")
        if len(self.handSlot)!=0:
           print("MAIN GAUCHE: "+self.handSlot[0].name)
           if len(self.handSlot)!=1:
                print("MAIN DROITE: "+self.handSlot[1].name)
           else:
               print("MAIN DROITE:")
        else:
            print("MAIN GAUCHE:\nMAIN DROITE:")
        print("\nARMURE")
        if len(self.headSlot)!=0:
           print("TETE: "+self.headSlot[0].name)
        else:
            print("TETE:")
        if len(self.chestSlot) != 0:
            print("CORPS: " + self.chestSlot[0].name)
        else:
            print("CORPS:")
        if len(self.armsSlot) != 0:
            print("PROTECTION BRAS: "+self.armsSlot[0].name)
        else:
            print("PROTECTION BRAS: ")
        if len(self.pantsSlot)!=0:
            print("PANTALON: " + self.pantsSlot[0].name)
        else:
            print("PANTALON:")
        if len(self.legsSlot)!=0:
            print("PROTECTION JAMBES: " + self.legsSlot[0].name)
        else:
            print("PROTECTION JAMBES:")
        print("\nJOYAUX")
        if len(self.jewelSlot)!=0:
              print("JOYAU 1: "+self.jewelSlot[0].name)
              if len(self.jewelSlot)!=1:
                 print("JOYAU 2: " + self.jewelSlot[1].name)
              else:
                  print("JOYAU 2:")
        else:
            print("JOYAU 1:")
            print("JOYAU 2:")

    def consumeConsumable(self,indice,hero):
        # auteur Gabriel Desmullier
        #prendre un consomable
        if str(self.objectList[indice].__class__) == "<class 'Objet.Consumable'>": #on regarde si c'est bien un consomable
            hero.addConsumableStat(self.objectList[indice]) #on donne ses statsau hero
            self.removeItemFromInventory(indice) #on retire l'objet de l'inventaire inactif


    #les fonctions suivantes permettent de placer un objet dans son emplacement
    def equipHead(self,indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__) == "<class 'Objet.Armor'>" and self.objectList[indice].armorSlot=="head": #l'objet est bien une armure et le slot est bien la tete
            if len(self.headSlot)==0: #si le slot est vide tant mieux
               self.headSlot.append(self.objectList[indice]) #on ajoute simplement l'objet
               hero.addArmorStat(self.objectList[indice])
               del[self.objectList[indice]]
            else:
                self.objectList.append(self.headSlot[0]) #sinon on doit remettre l'objet en place dans l'inventaire inactif
                hero.removeArmorStat(self.headSlot[0]) #pour pouvoir placer l'objet dans le slot
                self.headSlot[0]=self.objectList[indice]
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]] #l'objet place dans le slot est supprime de l'inventaire inactif

        else:
            print("je pense qu'il ya erreur ici")

    def equipChest(self, indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__) == "<class 'Objet.Armor'>" and self.objectList[indice].armorSlot == "chest":
            if len(self.chestSlot) == 0:
                self.chestSlot.append(self.objectList[indice])
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.chestSlot[0])
                hero.removeArmorStat(self.chestSlot[0])
                self.chestSlot[0] = self.objectList[indice]
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]
        else:
            print("je pense qu'il ya erreur ici")

    def equipArms(self, indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__) == "<class 'Objet.Armor'>" and self.objectList[indice].armorSlot == "arms":
            if len(self.armsSlot )== 0:
                self.armsSlot.append(self.objectList[indice])
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.armsSlot[0])
                hero.removeArmorStat(self.armsSlot[0])
                self.armsSlot[0] = self.objectList[indice]
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]
        else:
            print("je pense qu'il ya erreur ici")

    def equipPants(self, indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__) == "<class 'Objet.Armor'>" and self.objectList[indice].armorSlot == "pants":
            if len(self.pantsSlot) == 0:
                self.pantsSlot.append(self.objectList[indice])
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.pantsSlot[0])
                hero.removeArmorStat(self.pantsSlot[0])
                self.pantsSlot[0] = self.objectList[indice]
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]

        else:
            print("je pense qu'il ya erreur ici")

    def equipLegs(self, indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__) == "<class 'Objet.Armor'>" and self.objectList[indice].armorSlot == "legs":
            if len(self.legsSlot) == 0:
                self.legsSlot.append(self.objectList[indice])
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.legsSlot[0])
                hero.removeArmorStat(self.legsSlot[0])
                self.legsSlot[0] = self.objectList[indice]
                hero.addArmorStat(self.objectList[indice])
                del [self.objectList[indice]]

        else:
            print("je pense qu'il ya erreur ici")


    def addWeapon(self,indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__ )== "<class 'Objet.Weapon'>":
            if len(self.handSlot)==0 or len(self.handSlot)==1: #si aucune arme ou une seule arme et placer dans le slot, on peut ajouter directement l'arme
                self.handSlot.append(self.objectList[indice])
                hero.addWeaponStat(self.objectList[indice])
                del [self.objectList[indice]]
            else: #si les deux slots sont pris on va devoir demander au joueur de choisir quelle arme la nouvelle arme va t-elle remplacee
                print("VOUS N'AVEZ QUE DEUX MAINS, SELECTIONNEZ UNE ARME A ECHANGER")
                print("MAIN GAUCHE : "+self.handSlot[0].name+"(ENTREZ 1)")
                print("MAIN DROITE : " + self.handSlot[1].name + "(ENTREZ 2)")

                #saisie du choix
                entry=str(input())
                while (entry!="1" and entry!="2"):
                    print("ENTREZ 1 OU 2, CE N'EST POURTANT PAS COMPLIQUE")
                    entry = str(input())

                    #execution du remplacement
                if entry=="1":
                    self.objectList.append(self.handSlot[0])
                    hero.removeWeaponStat(self.handSlot[0])
                    self.handSlot[0] = self.objectList[indice]
                    hero.addWeaponStat(self.objectList[indice])
                    del [self.objectList[indice]]
                else:
                    self.objectList.append(self.handSlot[1])
                    hero.removeWeaponStat(self.handSlot[0])
                    self.handSlot[1] = self.objectList[indice]
                    hero.addWeaponStat(self.objectList[indice])
                    del [self.objectList[indice]]

        else:
            print("je pense qu'il y a erreur ici")


    def addJewel(self,indice,hero):
        # auteur Gabriel Desmullier
        if str(self.objectList[indice].__class__) == "<class 'Objet.Jewel'>":
            if len(self.jewelSlot)==0 or len(self.jewelSlot)==1:
                self.jewelSlot.append(self.objectList[indice])
                hero.addJewelStat(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                print("VOUS N'AVEZ LE DROIT QU'A DEUX JOYAUX, SELECTIONNEZ UN JOYAU A ECHANGER")
                print("JOYAU 1 : "+self.jewelSlot[0].name+"(ENTREZ 1)")
                print("JOYAU 2 : " + self.jewelSlot[1].name + "(ENTREZ 2)")
                entry=str(input())
                while (entry!="1" and entry!="2"):
                    print("ENTREZ 1 OU 2, CE N'EST POURTANT PAS COMPLIQUE")
                    entry = str(input())
                if entry=="1":
                    self.objectList.append(self.jewelSlot[0])
                    hero.removeJewelStat(self.jewelSlot[0])
                    self.jewelSlot[0] = self.objectList[indice]
                    hero.addJewelStat(self.objectList[indice])
                    del [self.objectList[indice]]
                else:
                    self.objectList.append(self.jewelSlot[1])
                    hero.removeJewelStat(self.jewelSlot[1])
                    self.jewelSlot[1] = self.objectList[indice]
                    hero.addJewelStat(self.objectList[indice])
                    del [self.objectList[indice]]

        else:
            print("je pense qu'il y a erreur ici")





    def saveInventory(self,filePath):
        #auteur Gabriel Desmullier
        #sauvegarder l'inventaire a la suite d'un fichier
        file= open(filePath, "a")
        file.write("\nINVENTORY\n")
        #Une ligne ecrite= 1 emplacement dans l'inventaire
        for object in self.objectList:
            file.write(str(object.__class__)+","+str(object.id)+";") #liste des objets de l'inventaire inactif type + id
        file.write("\n"+str(self.gold)) #gold
        if len(self.headSlot)!=0:
            file.write("\n" + str(self.headSlot[0].id))#tete uniquement identifiant
        else:
            file.write("\n0")
        if len(self.chestSlot) != 0:
            file.write("\n" + str(self.chestSlot[0].id))#corps
        else:
            file.write("\n0")
        if len(self.armsSlot) != 0:
            file.write("\n" + str(self.armsSlot[0].id))#protection bras
        else:
            file.write("\n0")
        if len(self.pantsSlot) != 0:
            file.write("\n" + str(self.pantsSlot[0].id))#pantalon
        else:
            file.write("\n0")
        if len(self.legsSlot) != 0:
            file.write("\n" + str(self.legsSlot[0].id))#protections des chambes
        else:
            file.write("\n0")
        if len(self.handSlot)!=0:
            if len(self.handSlot)==2:
                   file.write("\n" + str(self.handSlot[0].id)+","+self.handSlot[1].id)#armes
            elif len(self.handSlot)==1:
                   file.write("\n" + str(self.handSlot[0].id)+",0")  # armes
        else:
            file.write("\n0,0")
        if len(self.jewelSlot)!=0:
            if len(self.jewelSlot)==2:
               file.write("\n" + str(self.jewelSlot[0].id) + "," + self.jewelSlot[1].id)  #joyaux
            elif len(self.jewelSlot)==1:
               file.write("\n" + str(self.jewelSlot[0].id)+",0")  #joyaux
        else:
            file.write("\n0,0")
        file.close()

    def loadInventory(self,filePath):
        # auteur Gabriel Desmullier
        #charger un inventaire depuis un fichier
        file = open(filePath, "r")
        ligne=file.readline()

        while str(ligne)!="INVENTORY\n":
            ligne = file.readline()



        inventoryInactive=file.readline()
        engr=inventoryInactive.split(";") #on recupere l'inventaire inactif
        for eng in engr:   #pour chaque objet on va determiner sa classe et on va ensuite charger l'objet depuis la bdd grace a son id
            object=eng.split(",")
            if str(object[0])=="<class '__main__.Weapon'>":
                self.addItemToInventory(ob.chargeAWeaponFromDB(int(object[1])))
            elif str(object[0])=="<class '__main__.Armor'>" :
                self.addItemToInventory(ob.chargeAnArmorFromDB(int(object[1])))
            elif str(object[0])=="<class '__main__.Jewel'>" :
                self.addItemToInventory(ob.chargeAJewelFromDB(int(object[1])))
            elif str(object[0])=="<class '__main__.Consumable'>":
                self.addItemToInventory(ob.chargeAConsumableFromDB(int(object[1])))

        self.gold=int(file.readline())#chargement de l'or
        #chargement de l'armure
        id=int(file.readline())
        if id!=0:
           self.headSlot[0]=ob.chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
           self.chestSlot[0] = ob.chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
            self.armsSlot[0] = ob.chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
            self.pantsSlot[0] = ob.chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
             self.legsSlot[0] = ob.chargeAnArmorFromDB(id)
        #chargement des armes
        weapons=file.readline().split(",")
        if int(weapons[0])!=0:
            self.handSlot[0]=ob.chargeAWeaponFromDB(int(weapons[0]))
        if int(weapons[1])!=0:
            self.handSlot[1] = ob.chargeAWeaponFromDB(int(weapons[1]))
        #chargement des joyaux
        jewel=file.readline().split(",")
        if int(jewel[0])!=0:
            self.jewelSlot[0]=ob.chargeAJewelFromDB(int(jewel[0]))
        if int(jewel[1]) != 0:
            self.jewelSlot[1] = ob.chargeAJewelFromDB(int(jewel[1]))
        file.close()

    def createMerchantInventory(self,level):
        # auteur Gabriel Desmullier
        #creation d'un inventaire pseudo-aleatoirement pour un marchand en fonction de son level

        if level==1:
            itemNumber=random.randint(5,10) #nombres d'items dans son inventaire, plus son niveau est eleve plus il vendra d'items
            for i in range(itemNumber):
                typeItem=random.randint(1,4) #selection du type d'item: arme, armure, joyau, consomable
                if typeItem==1: #weapon
                    id=random.randint(1,6) #selection de l'id de l'item en fonction du level
                    self.addItemToInventory(ob.chargeAWeaponFromDB(id)) #ajout a l'inventaire inactif
                elif typeItem==2: #armor
                    id=random.randint(1,7)
                    self.addItemToInventory(ob.chargeAnArmorFromDB(id))
                elif typeItem==3: #jewel
                    id = random.randint(1, 3)
                    self.addItemToInventory(ob.chargeAJewelFromDB(id))
                elif typeItem==4: #consumable
                    id = random.randint(1,7)
                    self.addItemToInventory(ob.chargeAConsumableFromDB(id))

        elif level==2:
            itemNumber=random.randint(10,15)
            for i in range(itemNumber):
                typeItem=random.randint(1,4)
                if typeItem==1: #weapon
                    id=random.randint(1,11)
                    self.addItemToInventory(ob.chargeAWeaponFromDB(id))
                elif typeItem==2: #armor
                    id=random.randint(1,13)
                    self.addItemToInventory(ob.chargeAnArmorFromDB(id))
                elif typeItem==3: #jewel
                    id = random.randint(4, 6)
                    self.addItemToInventory(ob.chargeAJewelFromDB(id))
                elif typeItem==4: #consumable
                    id = random.randint(1,7)
                    self.addItemToInventory(ob.chargeAConsumableFromDB(id))
        else:
            itemNumber = random.randint(15, 20)
            for i in range(itemNumber):
                typeItem = random.randint(1, 4)
                if typeItem == 1:  # weapon
                    id = random.randint(1,16)
                    self.addItemToInventory(ob.chargeAWeaponFromDB(id))
                elif typeItem == 2:  # armor
                    id = random.randint(1, 19)
                    self.addItemToInventory(ob.chargeAnArmorFromDB(id))
                elif typeItem == 3:  # jewel
                    id = random.randint(7, 9)
                    self.addItemToInventory(ob.chargeAJewelFromDB(id))
                elif typeItem == 4:  # consumable
                    id = random.randint(1, 7)
                    self.addItemToInventory(ob.chargeAConsumableFromDB(id))


    def createMonsterInventory(self,monster,head,chest,arms,pants,legs,weapon1,weapon2,jewel1,jewel2):
        # auteur Gabriel Desmullier
        #donne des armes aux monstres et applique les stats de l'arme au monstre
        if head!=0:
            self.headSlot.append(ob.chargeAnArmorFromDB(head))
            monster.addArmorStat(self.headSlot[0])
        if chest!=0:
            self.chestSlot.append(ob.chargeAnArmorFromDB(chest))
            monster.addArmorStat(self.chestSlot[0])
        if arms!=0:
            self.armsSlot.append(ob.chargeAnArmorFromDB(arms))
            monster.addArmorStat(self.armsSlot[0])
        if pants!=0:
            self.pantsSlot.append(ob.chargeAnArmorFromDB(pants))
            monster.addArmorStat(self.pantsSlot[0])
        if legs!=0:
            self.legsSlot.append(ob.chargeAnArmorFromDB(legs))
            monster.addArmorStat(self.legsSlot[0])
        if weapon1!=0:
            self.handSlot.append(ob.chargeAWeaponFromDB(weapon1))
            monster.addWeaponStat(ob.chargeAWeaponFromDB(weapon1))
        if weapon2!=0:
            self.handSlot.append(ob.chargeAWeaponFromDB(weapon2))
            monster.addWeaponStat(ob.chargeAWeaponFromDB(weapon2))
        if jewel1!=0:
            self.jewelSlot.append(ob.chargeAJewelFromDB(jewel1))
            monster.addJewelStat(ob.chargeAJewelFromDB(jewel1))
        if jewel2!=0:
            self.jewelSlot.append(ob.chargeAJewelFromDB(jewel2))
            monster.addJewelStat(ob.chargeAJewelFromDB(jewel2))











class Character():
    #auteur Romain Dermu
    
    def __init__(self,id,name,level,speed):
        # auteur Romain Dermu
        self.id=id
        self.name = name
        self.inventory=Inventory(id)
        self.level = level
        self.speed = speed

    def addInventory(self,inventory):
        # auteur Gabriel Desmullier
        #fonction supplementaire non utilise dans le jeu mais utilise pour les tests
        self.inventory=inventory




        
class Hero(Character):
    # auteur Romain Dermu
    
    def __init__(self,id,name,level,speed):
        # auteur Romain Dermu
        super().__init__(id,name,level,speed)
        self.health = 150
        self.max_health = 150
        self.shield = 50
        self.dodge_chance = 50 #en %
        self.parry_chance = 30 #en %
        self.critical_hit_chance = 20 #en %
        self.magic_points = 100
        self.min_attack = 10
        self.max_attack = 30
        self.armor = 10
        self.exp = 0
        self.position=0

    def afficher_stats(self):
        # auteur Romain Dermu
        print(self.name,"   Level ",self.level,"  EXP:",self.exp,"/",100,"\n")
        print("Health ",self.health)
        print("MP         ",self.magic_points)




    def grade(self):
        #auteur Gabriel Desmullier
        #augmentation du niveau
        if self.exp>=100:
            self.level=self.level+1
            print("Niveau "+str(self.level)+" ATTEINT!")
            self.exp=self.exp-100
            self.dodge_chance = self.dodge_chance+5
            self.parry_chance = self.parry_chance+5
            self.critical_hit_chance = self.critical_hit_chance+5
            self.magic_points = self.magic_points+30
            self.min_attack = self.min_attack+10
            self.max_attack = self.max_attack+10



    def addArmorStat(self,armor):
        # auteur Gabriel Desmullier
        #ajoute les states d'un objet armure aux stats du hero
        if self.level>armor.levelRequired: #ajoute les stats que si le hero a le niveau recqui
            self.armor=self.armor+armor.armorPoint
            self.shield=self.shield+armor.shieldBonus

    def removeArmorStat(self,armor):
        # auteur Gabriel Desmullier
        #retire les stats d'une armure
        if self.level > armor.levelRequired:
            self.armor = self.armor - armor.armorPoint
            self.shield = self.shield - armor.shieldBonus

    def addWeaponStat(self, weapon):
        #auteur Gabriel Desmullier
        # ajoute les stats d'une arme aux stats du hero
        if self.level > weapon.levelRequired:
            self.max_attack=self.max_attack+weapon.damageMaxBonus
            self.min_attack=self.min_attack+weapon.damageMinBonus
            self.parry_chance=self.parry_chance+weapon.parryBonus
            self.dodge_chance=self.dodge_chance+weapon.dodgeBonus
            self.critical_hit_chance=self.critical_hit_chance+weapon.criticalHitBonus

    def removeWeaponStat(self, weapon):
        # auteur Gabriel Desmullier
        #retire les stats d'une arme
        if self.level > weapon.levelRequired:
            self.max_attack=self.max_attack-weapon.damageMaxBonus
            self.min_attack=self.min_attack-weapon.damageMinBonus
            self.parry_chance=self.parry_chance-weapon.parryBonus
            self.dodge_chance=self.dodge_chance-weapon.dodgeBonus
            self.critical_hit_chance=self.critical_hit_chance-weapon.criticalHitBonus

    def addJewelStat(self, jewel):
        # auteur Gabriel Desmullier
        # ajoute les stats d'un joyau aux stats du hero
        if self.level > jewel.levelRequired:
            self.max_attack=self.max_attack+jewel.damageMaxBonus
            self.min_attack=self.min_attack+jewel.damageMinBonus
            self.parry_chance=self.parry_chance+jewel.parryBonus
            self.dodge_chance=self.dodge_chance+jewel.dodgeBonus
            self.critical_hit_chance=self.critical_hit_chance+jewel.criticalHitBonus
            self.armor=self.armor+jewel.armorPoint
            self.shield=self.shield+jewel.shieldBonus
            self.magic_points=self.magic_points+jewel.magicPointsBonus

    def removeJewelStat(self, jewel):
        # auteur Gabriel Desmullier
        # retire les stats d'un joyau des stats du hero
        if self.level > jewel.levelRequired:
            self.max_attack=self.max_attack-jewel.damageMaxBonus
            self.min_attack=self.min_attack-jewel.damageMinBonus
            self.parry_chance=self.parry_chance-jewel.parryBonus
            self.dodge_chance=self.dodge_chance-jewel.dodgeBonus
            self.critical_hit_chance=self.critical_hit_chance-jewel.criticalHitBonus
            self.armor=self.armor-jewel.armorPoint
            self.shield=self.shield-jewel.shieldBonus
            self.magic_points=self.magic_points-jewel.magicPointsBonus

    def addConsumableStat(self,consumable):
        # auteur Gabriel Desmullier
        #ajoute les stats d'un consumable
        self.max_attack = self.max_attack + consumable.damageMaxBonus
        self.min_attack = self.min_attack + consumable.damageMinBonus
        self.parry_chance = self.parry_chance + consumable.parryBonus
        self.dodge_chance = self.dodge_chance + consumable.dodgeBonus
        self.critical_hit_chance = self.critical_hit_chance + consumable.criticalHitBonus
        self.shield = self.shield + consumable.shieldBonus
        self.magic_points = self.magic_points + consumable.magicPointsBonus
        self.health = self.health + consumable.healthBonus
        if self.health>self.max_health: #le personnage a une sante max qu'il ne peut pas depasser
            self.health=self.max_health



        
class Monster(Character):
    # auteur Romain Dermu

    def __init__(self,id,name,level,speed,description):
        # auteur Romain Dermu
        super().__init__(id,name,level,speed)
        self.health = 150
        self.max_health = 150
        self.min_attack = 10
        self.max_attack = 30
        self.shield = 50
        self.dodge_chance = 50  # en %
        self.parry_chance = 30 # en %
        self.critical_hit_chance = 20  # en %
        self.magic_points = 100
        self.armor = 10  # en %
        self.description=description
        self.position=0


        
    def low_level_smart_move(self,hero_position):
        # auteur Romain Dermu
        direction = [0,0]
        if abs(self.position[0] - hero_position[0] < self.position[1] - hero_position[1]):
            if self.position[0] < hero_position[0]:
                direction[0] = 1
            elif self.position[0] > hero_position[0]:
                direction[0] = -1
            else:
                if self.position[1] < hero_position[1]:
                    direction[1] = 1
                elif self.position[1] > hero_position[1]:
                    direction[1] = -1
        else:
            if self.position[1] < hero_position[1]:
                direction[1] = 1
            elif self.position[1] > hero_position[1]:
                direction[1] = -1
            else:
                if self.position[0] < hero_position[0]:
                    direction[0] = 1
                elif self.position[0] > hero_position[0]:
                    direction[0] = -1
        return direction
    
    def random_move(self):
        # auteur Romain Dermu
        direction = [random.choice([-1,0,1]),random.choice([-1,0,1])]
        return direction
        
    def high_level_smart_move(self,hero_position):
        # auteur Romain Dermu
        direction = [0,0]
        if self.position[0] < hero_position[0]:
            direction[0] = 1
        elif self.position[0] > hero_position[0]:
            direction[0] = -1
        if self.position[1] < hero_position[1]:
            direction[1] = 1
        elif self.position[1] > hero_position[1]:
            direction[1] = -1
        return direction

    def addArmorStat(self,armor):
        # auteur Gabriel Desmullier
        #ajoute les stats d'un objet armure aux stats du monstre
        if self.level>armor.levelRequired: #ajoute les stats que si le monstre a le niveau recqui
            self.armor=self.armor+armor.armorPoint
            self.shield=self.shield+armor.shieldBonus



    def addWeaponStat(self, weapon):
        # auteur Gabriel Desmullier
        # ajoute les stats d'une arme aux stats du monstre
        if self.level > weapon.levelRequired:
            self.max_attack=self.max_attack+weapon.damageMaxBonus
            self.min_attack=self.min_attack+weapon.damageMinBonus
            self.parry_chance=self.parry_chance+weapon.parryBonus
            self.dodge_chance=self.dodge_chance+weapon.dodgeBonus
            self.critical_hit_chance=self.critical_hit_chance+weapon.criticalHitBonus



    def addJewelStat(self, jewel):
        # auteur Gabriel Desmullier
        # ajoute les stats d'un joyau aux stats du monstre
        if self.level > jewel.levelRequired:
            self.max_attack=self.max_attack+jewel.damageMaxBonus
            self.min_attack=self.min_attack+jewel.damageMinBonus
            self.parry_chance=self.parry_chance+jewel.parryBonus
            self.dodge_chance=self.dodge_chance+jewel.dodgeBonus
            self.critical_hit_chance=self.critical_hit_chance+jewel.criticalHitBonus
            self.armor=self.armor+jewel.armorPoint
            self.shield=self.shield+jewel.shieldBonus
            self.magic_points=self.magic_points+jewel.magicPointsBonus



    def displayMonster(self):
        # auteur Gabriel Desmullier
        #affiche le monstre
        print("TYPE DE MONSTRE: "+self.name)
        print("DESCRIPTION: "+self.description)
        print("SANTE: "+str(self.health))


def chargeAMonsterFromDB(id):
    # auteur Gabriel Desmullier
    #charger un monstre depuis la bdd a partir de son id
    file = open(r'Monstre.txt', 'r+') #ouverture bdd
    for i in range(id):
        ligneInutile = file.readline()  # lignes precedentes inutiles
    ligneUtile = file.readline() #lecture de la bonne ligne correspondant a l'id
    ligne = ligneUtile.split(";") #separation des informations

    if int(ligne[0])==id:

        monster=Monster(id,ligne[1],int(ligne[3]),int(ligne[13]),ligne[2]) #creation du monstre
        monster.inventory.createMonsterInventory(monster,int(ligne[4]),int(ligne[5]),int(ligne[6]),int(ligne[7]),int(ligne[8]),int(ligne[9]),int(ligne[10]),int(ligne[11]),int(ligne[12]));
        #ajout de l'inventaire
        return monster

    else:#on ne sait jamais
        print(" Je ne comprend pas!!!")


class Merchant(Character):
    # auteur Romain Dermu
    
    def __init__(self,id,name,level,speed):
        # auteur Romain Dermu
        super().__init__(id,name,level,speed)
        self.position=0
        self.inventory.createMerchantInventory(level) #creation de l'inventaire en fonction du niveau du marchand



    def random_move(self):
        # auteur Romain Dermu
        direction = [random.choice([-1,0,1]),random.choice([-1,0,1])]
        return direction

