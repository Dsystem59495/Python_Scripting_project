##################################################
# Gabriel Desmullier
# Projet Python RPG 2019
##################################################


import character as ch
import map as mp
from interaction import *

class Partie():
    # auteur Gabriel Desmullier

    def __init__(self):
        # auteur Gabriel Desmullier
        #initialisation de la partie
        self.level=1
        self.heroVivant=True
        print("*  ** *** ** ** ** *** * ** * ** ***   *** * ** * ** * ** * * ** ")
        print("               ASCII ADVENTURE            /\ /\         / \      ")
        print("             G                           /  /   \  /\  /    \    ")
        print(",,_,__,__,,,-M0 ,,__,_,_,,,____,,,__,_,_/         /  /        \  ")
        print("***,**,**,*',',* * *,,,'''*,* **,* *'**'* **,* ** *'''** ** ,* **")


        nomHero=str(input("Quel est votre nom?\n"))
        while nomHero.upper()=="ROMAIN":        #petite blague pour ceux qui voudraient appeller leur personnage Romain
            nomHero = str(input("Quel est votre nom?\n"))

        self.hero=ch.Hero(0,nomHero,1,1)

        print("Votre mission "+self.hero.name+" sera de ramasser le plus de fleurs magiques * parmi les fleurs *.\nIl n'y a qu'une seule fleur magique par niveau. Trouvez cette fleur et vous changerez de niveau.\nPrenez garde! les monstre M sont nombreux.\nAllez rencontrer des marchands C pour ameliorer votre equipement.\nDeplacez vous avec z,q,s,d et accedez a votre inventaire avec a\nEntrez n'importe quoi pour commencer\n")
        commencer=str(input())




    def levelPlay(self):
        # auteur Gabriel Desmullier
        #pour jouer un  niveau

        currentLevel=mp.Level(self.level,self.hero)
        while currentLevel.map.checkHeroDoor(self.hero.position)==False and self.heroVivant==True: #tant que la fleur n'est pas trouve  et que le hero est vivant on rejoue

            #commerce?
            currentLevel.shopping(self.hero)
            #combats? et mort  eventuellement?
            self.heroVivant=currentLevel.battles(self.hero)

            #deplacement des autres personnages
            currentLevel.moveMonsters()
            currentLevel.moveMerchants()
            #affichage de la carte
            currentLevel.levelPrintMap()

            actionJoueur(self.hero, currentLevel) #action du joueur
            self.hero.grade() #test de niveau






        #une fois que le hero est sorti mise a jour de l'avancee (level) et enregistrement
        if self.level<30:
            self.level=self.level+1
            #recompense du joueur pour avoir terminer le niveau
            self.hero.exp=self.hero.exp+20
            self.hero.inventory.gold=self.hero.inventory.gold+50
        elif self.level==30 and self.heroVivant==True:
            print("** ** ** * *  ** * ** * ** * * ** * ** * *** *** * **")
            print("VICTOIRE FINALE")
            print("** ** ** * *  ** * ** * ** * * ** * ** * *** *** * **")
            print("CREDIT:")
            print("PROJET PYTHON RPG M1 2019")
            print("ASCII ADVENTURE")
            print("REALISATION: Gabriel Desmullier")
            print("PROGRAMMATION: Gabriel Desmullier")
            print("TEST: Gabriel Desmullier")

        if self.heroVivant==False: #si le hero est mort durant le niveau la partie revient au niveau 1
            print("\n\n\n\n\nGAME OVER\n"+self.hero.name+" est mort\n\n\n")
            self.level=1
            self.heroVivant=True
            self.hero.health=150

    def play(self):
        # auteur Gabriel Desmullier
        #jeu jusqu'à la fin
        while self.level<=30:
            self.levelPlay()



mypartie=Partie()
mypartie.play()
