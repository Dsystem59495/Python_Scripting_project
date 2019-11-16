import random

class Object:
    "an Object"

    def __init__(self, id, name, description, goldValue):
        self.id = id
        self.name=name
        self.description=description
        self.goldValue = goldValue

    def display(self):
        print("ITEM: " +str(self.name))
        print("DESCRIPTION: "+str(self.description))
        print("PRICE: "+str(self.goldValue)+" bitcoins")




class Equipment(Object):
    "an equipment"

    def __init__(self,id, name, description,goldValue,levelRequired):
        super().__init__(id, name, description,goldValue)
        self.levelRequired=levelRequired

    def display(self):
        super().display()
        print("LEVEL REQUIRED: "+str(self.levelRequired))


class Weapon(Equipment):
    "a weapon to kill everybody"

    def __init__(self,id, name, description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus):
        super().__init__(id, name, description,goldValue,levelRequired)
        self.dodgeBonus=dodgeBonus
        self.parryBonus=parryBonus
        self.criticalHitBonus=criticalHitBonus
        self.damageMinBonus=damageMinBonus
        self.damageMaxBonus=damageMaxBonus

    def display(self):
        super().display()
        print("DODGE BONUS: "+str(self.dodgeBonus))
        print("PARRY BONUS: " + str(self.parryBonus))
        print("CRITICAL HIT BONUS: " + str(self.dodgeBonus))
        print("MINIMAL DAMAGE BONUS: " + str(self.damageMinBonus))
        print("MAXIMAL DAMAGE BONUS: " + str(self.damageMaxBonus))


class Armor(Equipment):
    "a armor to protect your privacy"

    def __init__(self,id, name, description,goldValue,levelRequired,armorPoint,shieldBonus,armorSlot):
        super().__init__(id, name, description,goldValue,levelRequired)
        self.armorPoint=armorPoint
        self.shieldBonus=shieldBonus
        self.armorSlot=armorSlot

    def display(self):
        super().display()
        print("ARMOR TYPE: " + str(self.armorSlot))
        print("ARMOR POINTS: "+str(self.armorPoint))
        print("SHIELD BONUS: "+str(self.shieldBonus))


class Jewel(Equipment):
    "my precious jewel"

    def __init__(self,id, name, description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus,armorPoint,shieldBonus,magicPointsBonus):
        super().__init__(id, name, description,goldValue,levelRequired)
        self.dodgeBonus=dodgeBonus
        self.parryBonus=parryBonus
        self.criticalHitBonus=criticalHitBonus
        self.damageMinBonus=damageMinBonus
        self.damageMaxBonus=damageMaxBonus
        self.armorPoint=armorPoint
        self.shieldBonus=shieldBonus
        self.magicPointsBonus=magicPointsBonus

    def display(self):
        super.display()
        print("DODGE BONUS: "+str(self.dodgeBonus))
        print("PARRY BONUS: " + str(self.parryBonus))
        print("CRITICAL HIT BONUS: " + str(self.dodgeBonus))
        print("MINIMAL DAMAGE BONUS: " + str(self.damageMinBonus))
        print("MAXIMAL DAMAGE BONUS: " + str(self.damageMaxBonus))
        print("ARMOR POINTS: "+str(self.armorPoint))
        print("SHIELD BONUS: "+str(self.shieldBonus))
        print("MAGIC POINTS BONUS: " + str(self.magicPointsBonus))



class Consumable(Object):
    "a consumable"
    def __init__(self,id, name, description,goldValue,healthBonus,shieldBonus,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus,magicPointsBonus):
        super().__init__(id, name, description,goldValue)
        self.dodgeBonus=dodgeBonus
        self.parryBonus=parryBonus
        self.criticalHitBonus=criticalHitBonus
        self.damageMinBonus=damageMinBonus
        self.damageMaxBonus=damageMaxBonus
        self.shieldBonus=shieldBonus
        self.magicPointsBonus=magicPointsBonus
        self.healthBonus=healthBonus

    def display(self):
        super().display()
        print("HEALTH BONUS: "+str(self.healthBonus))
        print("DODGE BONUS: " + str(self.dodgeBonus))
        print("PARRY BONUS: " + str(self.parryBonus))
        print("CRITICAL HIT BONUS: " + str(self.dodgeBonus))
        print("MINIMAL DAMAGE BONUS: " + str(self.damageMinBonus))
        print("MAXIMAL DAMAGE BONUS: " + str(self.damageMaxBonus))
        print("SHIELD BONUS: "+str(self.shieldBonus))
        print("MAGIC POINTS BONUS: " + str(self.magicPointsBonus))



#pour extraires des objects de la Base de donnees

def chargeAWeaponFromDB(id):
    file = open(r'Weapons.txt', 'r+')

    for i in range(id):
        ligneInutile= file.readline()  # lignes precedentes inutiles
    ligneUtile=file.readline()
    ligne=ligneUtile.split(";")
    IdLigne=int(ligne[0])
    name=ligne[1]
    description=ligne[2]
    goldValue=int(ligne[3])
    levelRequired=int(ligne[4])
    dodgeBonus=int(ligne[5])
    parryBonus=int(ligne[6])
    criticalHitBonus=int(ligne[7])
    damageMinBonus=int(ligne[8])
    damageMaxBonus=int(ligne[9])
    if IdLigne==id:
       return Weapon(id,name,description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus, damageMaxBonus)
    else:
        print("erreur indice fonction chargement")

def chargeAnArmorFromDB(id):
    file = open(r'Armor.txt', 'r+')

    for i in range(id):
        ligneInutile= file.readline()  # lignes precedentes inutiles
    ligneUtile=file.readline()
    ligne=ligneUtile.split(";")
    IdLigne=int(ligne[0])
    name=ligne[1]
    description=ligne[2]
    goldValue=int(ligne[3])
    levelRequired=int(ligne[4])
    armorPoint=int(ligne[5])
    shieldBonus=int(ligne[6])
    armorSlot=ligne[7]
    if IdLigne==id:
       return Armor(id,name,description,goldValue,levelRequired,armorPoint,shieldBonus,armorSlot)
    else:
        print("erreur indice fonction chargement")

def chargeAJewelFromDB(id):
    file = open(r'Jewel.txt', 'r+')
    for i in range(id):
        ligneInutile = file.readline()  # lignes precedentes inutiles
    ligneUtile = file.readline()
    ligne = ligneUtile.split(";")
    IdLigne = int(ligne[0])
    name = ligne[1]
    description = ligne[2]
    goldValue = int(ligne[3])
    levelRequired = int(ligne[4])
    dodgeBonus=int(ligne[5])
    parryBonus=int(ligne[6])
    criticalHitBonus=int(ligne[7])
    damageMinBonus=int(ligne[8])
    damageMaxBonus=int(ligne[9])
    armorPoint=int(ligne[10])
    shieldBonus=int(ligne[11])
    magicPointsBonus=int(ligne[12])
    if IdLigne==id:
       return Jewel(id,name,description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus,armorPoint,shieldBonus,magicPointsBonus)
    else:
        print("erreur indice fonction chargement")

def chargeAConsumableFromDB(id):
    file = open(r'Consumable.txt', 'r+')
    for i in range(id):
        ligneInutile = file.readline()  # lignes precedentes inutiles
    ligneUtile = file.readline()
    ligne = ligneUtile.split(";")
    IdLigne = int(ligne[0])
    name = ligne[1]
    description = ligne[2]
    goldValue = int(ligne[3])
    healthBonus=int(ligne[4])
    shieldBonus=int(ligne[5])
    dodgeBonus=int(ligne[6])
    parryBonus=int(ligne[7])
    criticalHitBonus=int(ligne[8])
    damageMinBonus=int(ligne[9])
    damageMaxBonus=int(ligne[10])
    magicPointsBonus=int(ligne[11])
    if IdLigne==id:
       return Consumable(id,name,description,goldValue,healthBonus,shieldBonus,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus,magicPointsBonus)
    else:
        print("erreur indice fonction chargement")






#classe de l'inventaire
class Inventory:
    objectList=[] #listes des objects possedes
    gold=10
    handSlot=[]
    hansSlotLen=2
    headSlot=[]
    chestSlot=[]
    pantsSlot=[]
    armsSlot=[]
    legsSlot=[]
    armorSlotLen=1
    jewelSlot=[]
    jewelSlotLen=2

    def __init__(self,id):
        self.id=id

    def earnGold(self,value):
        self.gold=self.gold+value

    def loseGold(self,value):
        self.gold=self.gold-value

    def displayInventoryInactive(self): #afficher tous les elements de l'inventaire(uniquement ceux qui ne sont pas portes)
        print("VOTRE INVENTAIRE INACTIF:")
        for i in range (len(self.objectList)):
            print(str(i)+": "+self.objectList[i].name)


    def displayAnItemFromYourInventoryInactive(self,indice): #afficher un element non pporte de l'inventaire
        print("OBJET DANS VOTRE INVENTAIRE INACTIF:")
        self.objectList[indice].display()

    def addItemToInventory(self,object): #ajouter gratuitement un objet a l'inventaire
        self.objectList.append(object)


    def buyAnObject(self,object): #acheter un objet et le mettre dans l'inventaire
        if object.goldValue>self.gold:
            print("VOUS N'AVEZ PAS ASSEZ D'ARGENT POUR ACHETER CET OBJET")
        else:
            self.loseGold(object.goldValue)
            self.addItemToInventory(object)

    def sellAnObject(self,indice): #ventre un objet et le retirer de l'inventaire
        self.earnGold(round(self.objectList[indice].goldValue/2)) #ah! les prix du marche de l'occasion!
        del[self.objectList[indice]]
        print("VOUS VENEZ DE VENDRE UN OBJET")

    def displayInventoryActive(self):
        print("VOTRE INVENTAIRE ACTIF:")
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
        if len(self.chestSlot) != 0:
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



    #les fonctions suivantes servent a equiper le joueur, il manque cependant les fonctions pour changer les stats des personnages
    def equipHead(self,indice):
        if self.objectList[indice].type==Armor and self.objectList[indice].armorSlot=="head":
            if len(self.headSlot==0):
               self.headSlot.append(self.objectList[indice])
               del[self.objectList[indice]]
            else:
                self.objectList.append(self.headSlot[0])
                self.headSlot[0]=self.objectList[indice]
                del [self.objectList[indice]]

        else:
            print("je pense qu'il ya erreur ici")

    def equipChest(self, indice):
        if self.objectList[indice].type == Armor and self.objectList[indice].armorSlot == "chest":
            if len(self.chestSlot == 0):
                self.chestSlot.append(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.chestSlot[0])
                self.chestSlot[0] = self.objectList[indice]
                del [self.objectList[indice]]
        else:
            print("je pense qu'il ya erreur ici")

    def equipArms(self, indice):
        if self.objectList[indice].type == Armor and self.objectList[indice].armorSlot == "arms":
            if len(self.armsSlot == 0):
                self.armsSlot.append(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.armsSlot[0])
                self.armsSlot[0] = self.objectList[indice]
                del [self.objectList[indice]]
        else:
            print("je pense qu'il ya erreur ici")

    def equipPants(self, indice):
        if self.objectList[indice].type == Armor and self.objectList[indice].armorSlot == "pants":
            if len(self.pantsSlot == 0):
                self.pantsSlot.append(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.pantsSlot[0])
                self.pantsSlot[0] = self.objectList[indice]
                del [self.objectList[indice]]

        else:
            print("je pense qu'il ya erreur ici")

    def equipLegs(self, indice):
        if self.objectList[indice].type == Armor and self.objectList[indice].armorSlot == "legs":
            if len(self.legsSlot == 0):
                self.legsSlot.append(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                self.objectList.append(self.legsSlot[0])
                self.legsSlot[0] = self.objectList[indice]
                del [self.objectList[indice]]

        else:
            print("je pense qu'il ya erreur ici")


    def addWeapon(self,indice):
        if self.objectList[indice].type == Weapon:
            if len(self.handSlot)==0 or len(self.handSlot)==1:
                self.handSlot.append(self.objectList[indice])
                del [self.objectList[indice]]
            else:
                print("VOUS N'AVEZ QUE DEUX MAINS, SELECTIONNEZ UNE ARME A ECHANGER")
                print("MAIN GAUCHE : "+self.handSlot[0].name+"(ENTREZ 1)")
                print("MAIN DROITE : " + self.handSlot[1].name + "(ENTREZ 2)")
                entry=str(input())
                while (entry!="1" and entry!="2"):
                    print("ENTREZ 1 OU 2, CE N'EST POURTANT PAS COMPLIQUE")
                    entry = str(input())
                if entry=="1":
                    self.objectList.append(self.handSlot[0])
                    self.handSlot[0] = self.objectList[indice]
                    del [self.objectList[indice]]
                else:
                    self.objectList.append(self.handSlot[1])
                    self.handSlot[1] = self.objectList[indice]
                    del [self.objectList[indice]]

        else:
            print("je pense qu'il y a erreur ici")


    def addJewel(self,indice):
        if self.objectList[indice].type == Jewel:
            if len(self.jewelSlot)==0 or len(self.jewelSlot)==1:
                self.jewelSlot.append(self.objectList[indice])
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
                    self.jewelSlot[0] = self.objectList[indice]
                    del [self.objectList[indice]]
                else:
                    self.objectList.append(self.jewelSlot[1])
                    self.jewelSlot[1] = self.objectList[indice]
                    del [self.objectList[indice]]

        else:
            print("je pense qu'il y a erreur ici")





    def saveInventory(self,filePath): #sauvegarder l'inventaire a la suite d'un fichier
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

    def loadInventory(self,filePath):#charger un inventaire depuis un fichier
        file = open(filePath, "r")
        ligne=file.readline()

        while str(ligne)!="INVENTORY\n":
            ligne = file.readline()



        inventoryInactive=file.readline()
        engr=inventoryInactive.split(";") #on recupere l'inventaire inactif
        for eng in engr:   #pour chaque objet on va determiner sa classe et on va ensuite charger l'objet depuis la bdd grace a son id
            object=eng.split(",")
            if str(object[0])=="<class '__main__.Weapon'>":
                self.addItemToInventory(chargeAWeaponFromDB(int(object[1])))
            elif str(object[0])=="<class '__main__.Armor'>" :
                self.addItemToInventory(chargeAnArmorFromDB(int(object[1])))
            elif str(object[0])=="<class '__main__.Jewel'>" :
                self.addItemToInventory(chargeAJewelFromDB(int(object[1])))
            elif str(object[0])=="<class '__main__.Consumable'>":
                self.addItemToInventory(chargeAConsumableFromDB(int(object[1])))

        self.gold=int(file.readline())#chargement de l'or
        #chargement de l'armure
        id=int(file.readline())
        if id!=0:
           self.headSlot[0]=chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
           self.chestSlot[0] = chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
            self.armsSlot[0] = chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
            self.pantsSlot[0] = chargeAnArmorFromDB(id)
        id = int(file.readline())
        if id != 0:
             self.legsSlot[0] = chargeAnArmorFromDB(id)
        #chargement des armes
        weapons=file.readline().split(",")
        if int(weapons[0])!=0:
            self.handSlot[0]=chargeAWeaponFromDB(int(weapons[0]))
        if int(weapons[1])!=0:
            self.handSlot[1] = chargeAWeaponFromDB(int(weapons[1]))
        #chargement des joyaux
        jewel=file.readline().split(",")
        if int(jewel[0])!=0:
            self.jewelSlot[0]=chargeAJewelFromDB(int(jewel[0]))
        if int(jewel[1]) != 0:
            self.jewelSlot[1] = chargeAJewelFromDB(int(jewel[1]))
        file.close()

    def createMerchantInventory(self,level): #création d'un inventaire pseudo-aleatoirement pour un marchand en fonction de son level

        if level==1:
            itemNumber=random.randint(5,10)
            for i in range(itemNumber):
                typeItem=random.randint(1,4)
                if typeItem==1: #weapon
                    id=random.randint(1,6)
                    self.addItemToInventory(chargeAWeaponFromDB(id))
                elif typeItem==2: #armor
                    id=random.randint(1,7)
                    self.addItemToInventory(chargeAnArmorFromDB(id))
                elif typeItem==3: #jewel
                    id = random.randint(1, 3)
                    self.addItemToInventory(chargeAJewelFromDB(id))
                elif typeItem==4: #consumable
                    id = random.randint(1,7)
                    self.addItemToInventory(chargeAConsumableFromDB(id))

        elif level==2:
            itemNumber=random.randint(10,15)
            for i in range(itemNumber):
                typeItem=random.randint(1,4)
                if typeItem==1: #weapon
                    id=random.randint(1,11)
                    self.addItemToInventory(chargeAWeaponFromDB(id))
                elif typeItem==2: #armor
                    id=random.randint(1,13)
                    self.addItemToInventory(chargeAnArmorFromDB(id))
                elif typeItem==3: #jewel
                    id = random.randint(4, 6)
                    self.addItemToInventory(chargeAJewelFromDB(id))
                elif typeItem==4: #consumable
                    id = random.randint(1,7)
                    self.addItemToInventory(chargeAConsumableFromDB(id))
        else:
            itemNumber = random.randint(15, 20)
            for i in range(itemNumber):
                typeItem = random.randint(1, 4)
                if typeItem == 1:  # weapon
                    id = random.randint(1,16)
                    self.addItemToInventory(chargeAWeaponFromDB(id))
                elif typeItem == 2:  # armor
                    id = random.randint(1, 19)
                    self.addItemToInventory(chargeAnArmorFromDB(id))
                elif typeItem == 3:  # jewel
                    id = random.randint(7, 9)
                    self.addItemToInventory(chargeAJewelFromDB(id))
                elif typeItem == 4:  # consumable
                    id = random.randint(1, 7)
                    self.addItemToInventory(chargeAConsumableFromDB(id))


    def createMonsterInventory(self,head,chest,arms,pants,legs,weapon1,weapon2,jewel1,jewel2): #donne des armes aux monstres en fonction du niveau
        if head!=0:
            self.headSlot.append(chargeAnArmorFromDB(head))
        if chest!=0:
            self.chestSlot.append(chargeAnArmorFromDB(chest))
        if arms!=0:
            self.armsSlot.append(chargeAnArmorFromDB(arms))
        if pants!=0:
            self.pantsSlot.append(chargeAnArmorFromDB(pants))
        if legs!=0:
            self.legsSlot.append(chargeAnArmorFromDB(legs))
        if weapon1!=0:
            self.handSlot.append(chargeAWeaponFromDB(weapon1))
        if weapon2!=0:
            self.handSlot.append(chargeAWeaponFromDB(weapon2))
        if jewel1!=0:
            self.jewelSlot.append(chargeAJewelFromDB(jewel1))
        if jewel2!=0:
            self.jewelSlot.append(chargeAJewelFromDB(jewel2))






#reste a faire creer inventaire pour monstre
moninventaire=Inventory(1)


moninventaire.loadInventory("C:\\Users\\Gabriel\\Documents\\PythonRPGprojet\\pythoncode\\testsauvegardeinventaire.txt")
moninventaire.displayInventoryInactive()
moninventaire.displayInventoryActive()





































