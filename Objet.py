##################################################
# Gabriel Desmullier
# Projet Python RPG 2019
##################################################


class Object:
    # auteur Gabriel Desmullier
    "an Object"

    def __init__(self, id, name, description, goldValue):
        # auteur Gabriel Desmullier
        self.id = id
        self.name=name
        self.description=description
        self.goldValue = goldValue

    def display(self):
        # auteur Gabriel Desmullier
        #affiche les attributs commun d'un objet
        print("ITEM: " +str(self.name))
        print("DESCRIPTION: "+str(self.description))
        print("PRICE: "+str(self.goldValue)+" bitcoins")




class Equipment(Object):
    # auteur Gabriel Desmullier
    #classe equipement qui herite d'Object
    "an equipment"

    def __init__(self,id, name, description,goldValue,levelRequired):
        # auteur Gabriel Desmullier
        super().__init__(id, name, description,goldValue)
        self.levelRequired=levelRequired

    def display(self):
        # auteur Gabriel Desmullier
        super().display()#affiche des attributs commun
        print("LEVEL REQUIRED: "+str(self.levelRequired)) #affichage attribut specifique


class Weapon(Equipment):
    # auteur Gabriel Desmullier
    "a weapon to kill everybody"

    def __init__(self,id, name, description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus):
        # auteur Gabriel Desmullier
        super().__init__(id, name, description,goldValue,levelRequired)
        self.dodgeBonus=dodgeBonus
        self.parryBonus=parryBonus
        self.criticalHitBonus=criticalHitBonus
        self.damageMinBonus=damageMinBonus
        self.damageMaxBonus=damageMaxBonus

    def display(self):
        # auteur Gabriel Desmullier
        super().display()
        print("DODGE BONUS: "+str(self.dodgeBonus))
        print("PARRY BONUS: " + str(self.parryBonus))
        print("CRITICAL HIT BONUS: " + str(self.dodgeBonus))
        print("MINIMAL DAMAGE BONUS: " + str(self.damageMinBonus))
        print("MAXIMAL DAMAGE BONUS: " + str(self.damageMaxBonus))


class Armor(Equipment):
    # auteur Gabriel Desmullier
    "a armor to protect your privacy"

    def __init__(self,id, name, description,goldValue,levelRequired,armorPoint,shieldBonus,armorSlot):
        # auteur Gabriel Desmullier
        super().__init__(id, name, description,goldValue,levelRequired)
        self.armorPoint=armorPoint
        self.shieldBonus=shieldBonus
        self.armorSlot=armorSlot

    def display(self):
        # auteur Gabriel Desmullier
        super().display()
        print("ARMOR TYPE: " + str(self.armorSlot))
        print("ARMOR POINTS: "+str(self.armorPoint))
        print("SHIELD BONUS: "+str(self.shieldBonus))


class Jewel(Equipment):
    # auteur Gabriel Desmullier
    "my precious jewel"

    def __init__(self,id, name, description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus,armorPoint,shieldBonus,magicPointsBonus):
        # auteur Gabriel Desmullier
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
        # auteur Gabriel Desmullier
        super().display()
        print("DODGE BONUS: "+str(self.dodgeBonus))
        print("PARRY BONUS: " + str(self.parryBonus))
        print("CRITICAL HIT BONUS: " + str(self.dodgeBonus))
        print("MINIMAL DAMAGE BONUS: " + str(self.damageMinBonus))
        print("MAXIMAL DAMAGE BONUS: " + str(self.damageMaxBonus))
        print("ARMOR POINTS: "+str(self.armorPoint))
        print("SHIELD BONUS: "+str(self.shieldBonus))
        print("MAGIC POINTS BONUS: " + str(self.magicPointsBonus))



class Consumable(Object):
    # auteur Gabriel Desmullier
    "a consumable"
    def __init__(self,id, name, description,goldValue,healthBonus,shieldBonus,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus,damageMaxBonus,magicPointsBonus):
        # auteur Gabriel Desmullier
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
        # auteur Gabriel Desmullier
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
    # auteur Gabriel Desmullier
    #extrait une arme de la bdd a partir de son id
    file = open(r'Weapons.txt', 'r+')

    for i in range(id):
        ligneInutile= file.readline()  # lignes precedentes inutiles
    ligneUtile=file.readline() #recuperation de la ligne interressante
    ligne=ligneUtile.split(";") #separartion de l'information
    IdLigne=int(ligne[0]) #stockage de l'information
    name=ligne[1]
    description=ligne[2]
    goldValue=int(ligne[3])
    levelRequired=int(ligne[4])
    dodgeBonus=int(ligne[5])
    parryBonus=int(ligne[6])
    criticalHitBonus=int(ligne[7])
    damageMinBonus=int(ligne[8])
    damageMaxBonus=int(ligne[9])
    if IdLigne==id: #creation de l'objet
       return Weapon(id,name,description,goldValue,levelRequired,dodgeBonus,parryBonus,criticalHitBonus,damageMinBonus, damageMaxBonus)
    else:
        print("erreur indice fonction chargement")

def chargeAnArmorFromDB(id):
    # auteur Gabriel Desmullier
    #creation d'une armure a partir de la bdd grace a son id
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
    # auteur Gabriel Desmullier
    #creation d'un joyau depuis la bdd grace a son id
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
    # auteur Gabriel Desmullier
    #creation d'un consommable depuis la bdd grace a son id
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



