##################################################
# Gabriel Desmullier
# Projet Python RPG 2019
##################################################


import copy
import ast
from interaction import *
import character as ch

class Map:
    # auteur Gabriel Desmullier
    "a Map"
    length=25 #taille de la carte
    width=50
    groundMap = []  # texture du sol
    decorMap = []  # position d'elements: arbres, batiments
    characterMap = []  # position des personnages: hero, marchant, monstre



    def _init__(self,id):
        # auteur Gabriel Desmullier
      self.id=id


    def initialiseListe(self):
        # auteur Gabriel Desmullier
        #donner la bonne taille aux listes et les remplir d'un meme motif
        self.groundMap = [[" " for i in range(50)] for j in range(25)]  # texture du sol
        self.decorMap = [[0 for i in range(50)] for j in range(25)]  # position d'elements: arbres, batiments
        self.characterMap = [[0 for i in range(50)] for j in range(25)]  # position des personnages: hero, marchant, monstre



    def groundMapInitialisation(self,river,chemin):
        #auteur Gabriel Desmullier
        #texturation de la carte et bordure
        #bordure de la carte
        for j in range(self.width):
            self.groundMap[0][j]="-"
            self.groundMap[self.length-1][j] = "-"

        for i in range(self.length):
            self.groundMap[i][0]="|"
            self.groundMap[i][self.width-1]="|"

        #ajout de fleurs * pour faire beau mais pas que
        for i in range(1,self.length-1):
            for j in range(1,self.width-1):
                nombre=random.randint(0,50)
                if nombre==0:               #les fleurs sont tres rares
                    self.groundMap[i][j]="*"


        # ajout de riviere si demandee
        if river==True:

            # on determine la case de depart de la riviere sur la bordure
            number = random.randint(0, 1)
            if number == 0:
                iDebut = random.randint(1, self.length - 2)
                liste = [1, self.width - 2]
                jDebut = random.choice(liste)
            else:
                jDebut = random.randint(1, self.width - 2)
                liste = [1, self.length - 2]
                iDebut = random.choice(liste)

            self.groundMap[iDebut][jDebut] = "~"
            # on va determiner les directions possibles a prendre pour la riviere pour eviter qu'elle ne fasse demi-tour
            direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            # suppression direction
            if iDebut == 1:
                direction.remove([-1, 0])
            if iDebut == self.length - 2:
                direction.remove([1, 0])
            if jDebut == 1:
                direction.remove([0, -1])
            if jDebut == self.width - 2:
                direction.remove([0, 1])

            # premiere iteration necessairement a l'exterieur de la boucle
            i = iDebut
            j = jDebut
            if iDebut == 1:
                i = iDebut + 1
            if iDebut == self.length - 2:
                i = iDebut - 1
            if jDebut == 1:
                j = jDebut + 1
            if jDebut == self.width - 2:
                j = jDebut - 1

            newDirection = random.choice(direction)
            ancienneDirection = newDirection
            self.groundMap[i][j] = "~"
            while (i > 1 and i < self.length - 2) and (j > 1 and j < self.width - 2):
                newDirection = random.choice(direction)
                while newDirection == ancienneDirection:
                    newDirection = random.choice(direction)
                ancienneDirection = newDirection
                i = i + newDirection[0]
                j = j + newDirection[1]
                self.groundMap[i][j] = "~"

                #creation de chemins #
        for k in range(chemin):
                    # on determine la case de depart du chemin sur la bordure
                    number = random.randint(0, 1)
                    if number == 0:
                        iDebut = random.randint(1, self.length - 2)
                        liste = [1, self.width - 2]
                        jDebut = random.choice(liste)
                    else:
                        jDebut = random.randint(1, self.width - 2)
                        liste = [1, self.length - 2]
                        iDebut = random.choice(liste)

                    self.groundMap[iDebut][jDebut] = "#"
                    # on va determiner les directions possibles a prendre pour le chemin
                    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                    # suppression direction
                    if iDebut == 1:
                        direction.remove([-1, 0])
                    if iDebut == self.length - 2:
                        direction.remove([1, 0])
                    if jDebut == 1:
                        direction.remove([0, -1])
                    if jDebut == self.width - 2:
                        direction.remove([0, 1])


                    # premiere iteration necessairement a l'exterieur de la boucle
                    i=iDebut
                    j=jDebut
                    if iDebut == 1:
                        i = iDebut + 1
                    if iDebut == self.length - 2:
                        i = iDebut - 1
                    if jDebut == 1:
                        j = jDebut + 1
                    if jDebut == self.width - 2:
                        j = jDebut - 1

                    newDirection = random.choice(direction)
                    ancienneDirection=newDirection
                    self.groundMap[i][j] = "#"
                    while (i > 1 and i < self.length - 2) and (j > 1 and j < self.width - 2):
                        newDirection = random.choice(direction)
                        while newDirection == ancienneDirection:
                            newDirection = random.choice(direction)
                        ancienneDirection = newDirection
                        i = i + newDirection[0]
                        j = j + newDirection[1]
                        self.groundMap[i][j] = "#"

    def decorMapInitialisation(self, arbres, maisons):
        #auteur Gabriel Desmullier
        # ajout d'elements de decor

        #ajout des arbres: il y a 4 types d'arbres:
        #           ^             _
        #    ^     /|\     _     ( )
        #   /|\    /|\    ( )   (   )
        #    |      |      |      |
        #    1      2      3      4

        #generation de la porte dans l'espace des monstres

        i=random.randint(1,5)
        j=random.randint(1,5)
        iBis=random.randint(0,1)
        jBis=random.randint(0,1)
        if iBis==1:        #determine si la porte est en haut ou en bas
            i=self.length-2-i
        if jBis==1:        #determine si la porte est a droite ou a gauche
            j=self.width-2-j
        self.decorMap[i][j]=8


        #generation des arbres
        for i in range(arbres):
            type=random.randint(1,4) #type d'arbre a planter

            i=random.randint(1,self.length-2) #position sur la carte
            j=random.randint(1,self.width-2)
            while self.groundMap[i][j]!=" " and self.decorMap[i][j]==0: #les arbres poussent uniquement dans l'herbe (au moins le pied du tronc)
                i = random.randint(1, self.length - 2)
                j = random.randint(1, self.width - 2)
            self.decorMap[i][j]=type

            if type==1 or type==3: #gestion de la transparance et du placement des decors( pour eviter qu'un arbre soit sur un autre)
                if i-1>=1:          #-1 sert a bloquer la case et a indiquer a un personnage qu'il n'est plus visible
                    self.decorMap[i-1][j]=-1
                    if j-1>=1:
                        self.decorMap[i-1][j-1]=-1
                    if j+1<=self.width-2:
                        self.decorMap[i - 1][j + 1] = -1
                if i-2>=1:
                    self.decorMap[i - 2][j] = -1

            if type==2:
                if i-1>=1:
                    self.decorMap[i-1][j]=-1
                    if j-1>=1:
                        self.decorMap[i-1][j-1]=-1
                    if j+1<=self.width-2:
                        self.decorMap[i - 1][j + 1] = -1
                if i-2>=1:
                    self.decorMap[i - 2][j] = -1
                    if j-1>=1:
                        self.decorMap[i-2][j-1]=-1
                    if j+1<=self.width-2:
                        self.decorMap[i - 2][j + 1] = -1
                if i-3>=1:
                    self.decorMap[i - 3][j] = -1

            if type==4:
                     if i - 1 >= 1:
                         self.decorMap[i - 1][j] = -1
                         if j - 1 >= 1:
                             self.decorMap[i - 1][j - 1] = -1
                             if j - 2 >= 1:
                                 self.decorMap[i - 1][j - 2] = -1
                         if j + 1 <= self.width - 2:
                             self.decorMap[i - 1][j + 1] = -1
                             if j + 2 <= self.width - 2:
                                 self.decorMap[i - 1][j + 2] = -1
                     if i - 2 >= 1:
                         self.decorMap[i - 2][j] = -1
                         if j - 1 >= 1:
                             self.decorMap[i - 2][j - 1] = -1
                         if j + 1 <= self.width - 2:
                             self.decorMap[i - 2][j + 1] = -1
                     if i - 3 >= 1:
                         self.decorMap[i - 3][j] = -1


        #ajout des maisons: il y a trois types de maisons
        #
        #    _____         /|\     _____
        #   // o \\    ////|o|    ///|\\\
        #   |o H o|    |  H o|    |o H  |
        #      5          6          7
        for i in range(maisons):
            type=random.randint(5,7)
            code=False
            while code==False: #les maisons ont besoins d'espaces vides pour etre construites
                i = random.randint(1, self.length - 2)
                j = random.randint(1, self.width - 7)
                number=0
                for c in range(0,7):
                    if self.groundMap[i][j+c]==" " and self.decorMap[i][j+c]==0:  #on cherche donc un espace horizontal de 5 cases vides
                        number=number+1

                if number>6:
                    code=True
            self.decorMap[i][j]=type
            if type == 5 or type==7:  # transparance

                self.decorMap[i][j + 1] = -2 #-2= base la maison et -1 derriere la maison
                self.decorMap[i][j + 2] = -2 #-2= inaccecible pour un personnage -1 accessible mais personnage cache
                self.decorMap[i][j + 3] = -2
                self.decorMap[i][j + 4] = -2
                self.decorMap[i][j + 5] = -2
                self.decorMap[i][j + 6] = -2
                if i - 1 >= 1:
                    self.decorMap[i - 1][j] =-1
                    self.decorMap[i - 1][j + 1] = -1
                    self.decorMap[i - 1][j + 2] = -1
                    self.decorMap[i - 1][j + 3] = -1
                    self.decorMap[i - 1][j + 4] = -1
                    self.decorMap[i - 1][j + 5] = -1
                    self.decorMap[i - 1][j + 6] = -1
                if i - 2 >= 1:
                    self.decorMap[i - 2][j + 1] = -1
                    self.decorMap[i - 2][j + 2] = -1
                    self.decorMap[i - 2][j + 3] = -1
                    self.decorMap[i - 2][j + 4] = -1
                    self.decorMap[i - 2][j + 5] = -1
            if type == 6:  #

                self.decorMap[i][j + 1] = -2
                self.decorMap[i][j + 2] = -2
                self.decorMap[i][j + 3] = -2
                self.decorMap[i][j + 4] = -2
                self.decorMap[i][j + 5] = -2
                self.decorMap[i][j + 6] = -2
                if i - 1 >= 1:
                    self.decorMap[i - 1][j] = -1
                    self.decorMap[i - 1][j + 1] = -1
                    self.decorMap[i - 1][j + 2] = -1
                    self.decorMap[i - 1][j + 3] = -1
                    self.decorMap[i - 1][j + 4] = -1
                    self.decorMap[i - 1][j + 5] = -1
                    self.decorMap[i - 1][j + 6] = -1
                if i - 2 >= 1:
                    self.decorMap[i - 2][j + 4] = -1
                    self.decorMap[i - 2][j + 5] = -1
                    self.decorMap[i - 2][j + 6] = -1


    def adMonster(self):
        # auteur Gabriel Desmullier
        #les monstres doivent apparaitres au bord de la carte
        i=random.randint(1,5)
        j=random.randint(1,5)
        iBis=random.randint(0,1)
        jBis=random.randint(0,1)
        if iBis==1:        #determine si le monstre est en haut ou en bas
            i=self.length-2-i
        if jBis==1:        #determine si le monstre est a droite ou a gauche
            j=self.width-2-j
        while self.decorMap[i][j]!=0 or self.decorMap[i][j]!=-1 and self.characterMap[i][j]!=0: #il ne doit pas etre sur un autre personnage ni sur un decor
            i = random.randint(1, 5)
            j = random.randint(1, 5)
            iBis = random.randint(0, 1)
            jBis = random.randint(0, 1)
            if iBis == 1:  # determine si le monstre est en haut ou en bas
                i = self.length - 2 - i
            if jBis == 1:  # determine si le monstre est a droite ou a gauche
                j = self.width - 2 - j


        self.characterMap[i][j]= 3 #on ajoute le monstre a la carte
        return [i,j] #on renvoie les coordonnees

    def adMerchant(self):
        # auteur Gabriel Desmullier
        #les marchands apparaaissent partout sur la carte
        i=random.randint(1,self.length-2)
        j=random.randint(1,self.width-2)
        while self.decorMap[i][j] != 0 or self.decorMap[i][j] != -1 and self.characterMap[i][j] != 0:
            i = random.randint(1, self.length - 2)
            j = random.randint(1, self.width - 2)

        self.characterMap[i][j]= 2 #on ajoute le marchand a la carte
        return [i,j] #on renvoie les coordonnees

    def adHero(self):
        # auteur Gabriel Desmullier
        #le hero apparait au milieu de la carte
        i=random.randint(9,14)
        j=random.randint(20,40)
        while self.decorMap[i][j] != 0 or self.decorMap[i][j] != -1 and self.characterMap[i][j] != 0:
            i = random.randint(9, 14)
            j = random.randint(20, 40)

        self.characterMap[i][j]= 1 #on ajoute le hero a la carte
        return [i,j] #on renvoie les coordonnees

    def printMap(self):
        # auteur Gabriel Desmullier
        #affichage des differents niveaux de la carte

       printableMap=copy.deepcopy(self.groundMap)

         #prise en compte texture du sol

       #prise en compte du decor
       for i in range (self.length):
           for j in range (self.width):
            cas=self.decorMap[i][j]
            #           ^             _
            #    ^     /|\     _     ( )
            #   /|\    /|\    ( )   (   )
            #    |      |      |      |
            #    1      2      3      4
            if cas==1:  #affichage de l'arbre 1 en partant du tronc
                printableMap[i][j]="|"
                if i-1>=1:
                    printableMap[i-1][j]="|"
                    if j-1>=1:
                        printableMap[i-1][j-1]="/"
                    if j+1<=self.width-2:
                        printableMap[i - 1][j + 1] = "\\"
                if i-2>=1:
                    printableMap[i - 2][j] = "^"

            if cas==2:  #affichage de l'arbre 2
                printableMap[i][j]="|"
                if i-1>=1:
                    printableMap[i-1][j]="|"
                    if j-1>=1:
                        printableMap[i-1][j-1]="/"
                    if j+1<=self.width-2:
                        printableMap[i - 1][j + 1] = "\\"
                if i-2>=1:
                    printableMap[i - 2][j] = "|"
                    if j-1>=1:
                       printableMap[i-2][j-1]="/"
                    if j+1<=self.width-2:
                        printableMap[i - 2][j + 1] = "\\"
                if i-3>=1:
                    printableMap[i - 3][j] = "^"

            if cas == 3:  # affichage de l'arbre 3
                printableMap[i][j] = "|"
                if i - 1 >= 1:
                    printableMap[i - 1][j] = " "
                    if j - 1 >= 1:
                        printableMap[i - 1][j - 1] = "("
                    if j + 1 <= self.width - 2:
                        printableMap[i - 1][j + 1] = ")"
                if i - 2 >= 1:
                    printableMap[i - 2][j] = "_"

            if cas == 4:  # affichage de l'arbre 4
                printableMap[i][j] = "|"
                if i - 1 >= 1:
                    printableMap[i - 1][j] = " "
                    if j - 1 >= 1:
                        printableMap[i - 1][j - 1] = " "
                        if j-2>=1:
                            printableMap[i - 1][j - 2] = "("
                    if j + 1 <= self.width - 2:
                        printableMap[i - 1][j + 1] = " "
                        if j+2<=self.width-2:
                            printableMap[i - 1][j + 2] = ")"
                if i - 2 >= 1:
                    printableMap[i - 2][j] = " "
                    if j - 1 >= 1:
                        printableMap[i - 2][j - 1] = "("
                    if j + 1 <= self.width - 2:
                        printableMap[i - 2][j + 1] = ")"
                if i - 3 >= 1:
                    printableMap[i - 3][j] = "_"
            #
            #    _____         /|\     _____
            #   // o \\    ////|o|    ///|\\\
            #   |o H o|    |  H o|    |o H  |
            #      5          6          7
            if cas==5: #affichage maison 1
                printableMap[i][j]="|"  #la gestion de la limite horizontale a deja ete faite lors du placement des maisons
                printableMap[i][j+1] = "o"
                printableMap[i][j+2] = " "
                printableMap[i][j+3] = "H"
                printableMap[i][j+4] = " "
                printableMap[i][j+5] = "o"
                printableMap[i][j+6] = "|"
                if i-1>=1:
                    printableMap[i-1][j] = "/"
                    printableMap[i-1][j + 1] = "/"
                    printableMap[i-1][j + 2] = " "
                    printableMap[i-1][j + 3] = "o"
                    printableMap[i-1][j + 4] = " "
                    printableMap[i-1][j + 5] = "\\"
                    printableMap[i-1][j + 6] = "\\"
                if i-2>=1:
                    printableMap[i - 2][j + 1] = "_"
                    printableMap[i - 2][j + 2] = "_"
                    printableMap[i - 2][j + 3] = "_"
                    printableMap[i - 2][j + 4] = "_"
                    printableMap[i - 2][j + 5] = "_"
            if cas==6: #affichage maison 2
                printableMap[i][j]="|"
                printableMap[i][j+1] = " "
                printableMap[i][j+2] = " "
                printableMap[i][j+3] = "H"
                printableMap[i][j+4] = " "
                printableMap[i][j+5] = "o"
                printableMap[i][j+6] = "|"
                if i-1>=1:
                    printableMap[i-1][j] = "/"
                    printableMap[i-1][j + 1] = "/"
                    printableMap[i-1][j + 2] = "/"
                    printableMap[i-1][j + 3] = "/"
                    printableMap[i-1][j + 4] = "|"
                    printableMap[i-1][j + 5] = "o"
                    printableMap[i-1][j + 6] = "|"
                if i-2>=1:
                    printableMap[i - 2][j + 4] = "/"
                    printableMap[i - 2][j + 5] = "|"
                    printableMap[i - 2][j + 6] = "\\"

            if cas == 7:  # affichage maison 3
                printableMap[i][j] = "|"
                printableMap[i][j + 1] = "o"
                printableMap[i][j + 2] = " "
                printableMap[i][j + 3] = "H"
                printableMap[i][j + 4] = " "
                printableMap[i][j + 5] = " "
                printableMap[i][j + 6] = "|"
                if i - 1 >= 1:
                    printableMap[i - 1][j] = "/"
                    printableMap[i - 1][j + 1] = "/"
                    printableMap[i - 1][j + 2] = "/"
                    printableMap[i - 1][j + 3] = "|"
                    printableMap[i - 1][j + 4] = "\\"
                    printableMap[i - 1][j + 5] = "\\"
                    printableMap[i - 1][j + 6] = "\\"
                if i - 2 >= 1:
                    printableMap[i - 2][j + 1] = "_"
                    printableMap[i - 2][j + 2] = "_"
                    printableMap[i - 2][j + 3] = "_"
                    printableMap[i - 2][j + 4] = "_"
                    printableMap[i - 2][j + 5] = "_"

            if  cas==8: #si c'est une porte elle se cache parmi les fleurs
                printableMap[i][j] = "*"




       #prise en compte personnages
       for i in range (self.length):
           for j in range (self.width):
               cas = self.characterMap[i][j]
               if cas==1: #le hero
                   #  G
                   # -M0
                  if self.decorMap[i][j]==0:  #un personnage situe derriere un decor ne doit pas etre vu
                      printableMap[i][j]="M"
                      if j-1>=1:
                          printableMap[i][j-1]="-"
                      if j+1<=self.width-2:
                          printableMap[i][j+1] = "0"
                      if i-1>=1:
                          printableMap[i-1][j] = "G"

               if cas == 2:  # marchand
                   #  C
                   # -M-
                   if self.decorMap[i][j] == 0:  # un personnage situe derriere un decor ne doit pas etre vu
                       printableMap[i][j] = "M"
                       if j - 1 >= 1:
                           printableMap[i][j - 1] = "-"
                       if j + 1 <= self.width - 2:
                           printableMap[i][j + 1] ="-"
                       if i - 1 >= 1:
                           printableMap[i - 1][j] = "C"

               if cas == 3:  # monstre
                   #  M
                   # 'W0
                   if self.decorMap[i][j] == 0:  # un personnage situe derriere un decor ne doit pas etre vu
                       printableMap[i][j] = "W"
                       if j - 1 >= 1:
                           printableMap[i][j - 1] = "'"
                       if j + 1 <= self.width - 2:
                           printableMap[i][j + 1] = "0"
                       if i - 1 >= 1:
                           printableMap[i - 1][j] = "M"


       for row in printableMap: #affichage de la table
           for elem in row:
               print(elem, end=' ') #erreur etrange
           print()



    def moveCharacter(self,position,direction,speed):
        # auteur Gabriel Desmullier
        #deplacement de n'importe quel personnage a partir de ses coordonnee et d'une direction
        #position [i,j](i ligne, j colonne) direction exemple [1,0] speed: nombre de cases parcourues en un tour
        if self.groundMap[position[0]][position[1]]=="#": #si le personnage commence son mouvement depuis une case chemin, il obtient un bonus de mouvement
            speed=speed+1

        code=False
        for c in range(speed):
            iNew=position[0]+int(direction[0])
            jNew=position[1]+int(direction[1])

            if iNew==1 or iNew==self.length-2 : #gestion bordure
                code=True
            #si sortie de carte, pas de mouvement
            if (jNew==1 or jNew==self.width-2) and code==False:
                code=True

            #gestion obstacle

            if ((self.decorMap[iNew][jNew]!=0 and self.decorMap[iNew][jNew]!=-1 and self.decorMap[iNew][jNew]!=8) or self.characterMap[iNew][jNew]!=0) and code==False:
            #si obstacle pas de mouvement, une porte n'est pas un obstacle
                code=True

            #arrivee dans une riviere: on ne peut avancer qu'une case a la fois dans une riviere
            if self.groundMap[iNew][jNew]=="~" and code==False:
                variable=self.characterMap[position[0]][position[1]] #mise a jour de la position
                self.characterMap[position[0]][position[1]]=0
                position[0]=iNew
                position[1]=jNew
                self.characterMap[position[0]][position[1]]=variable
                code=True #fin de mouvement car on est en riviere

            if code==True: #fin du deplacement
                break
            else:  #mise a jour du deplacement
                variable = self.characterMap[position[0]][position[1]]
                self.characterMap[position[0]][position[1]] = 0
                position[0] = iNew
                position[1] = jNew
                self.characterMap[position[0]][position[1]] = variable

        return position

    def checkHeroDoor(self,pos):
        # auteur Gabriel Desmullier
        #fonction qui verifit si un personnage est arrive a la porte si c'est le cas la partie doit etre enregistre et un nouveau niveau doit etre charge
        position=copy.deepcopy(pos)

        if self.decorMap[position[0]][position[1]]==8:
            return True
        elif self.decorMap[position[0]+1][position[1]]==8:
            return True
        elif self.decorMap[position[0]-1][position[1]]==8:
            return True
        elif self.decorMap[position[0]+1][position[1]+1]==8:
            return True
        elif self.decorMap[position[0]-1][position[1]-1]==8:
            return True
        elif self.decorMap[position[0]][position[1]+1]==8:
            return True
        elif self.decorMap[position[0]][position[1]-1]==8:
            return True
        elif self.decorMap[position[0]+1][position[1]-1]==8:
            return True
        elif self.decorMap[position[0]-1][position[1]+1]==8:
            return True
        else:
            return False



    def checkHero(self,position): #position du marchand ou du monstre
        # auteur Gabriel Desmullier
        # fonction qui verifit si un marchand ou un monstre est a cote du hero
            if self.characterMap[position[0]][position[1]] == 1:
                return True
            elif self.characterMap[position[0] + 1][position[1]] == 1:
                return True
            elif self.characterMap[position[0] - 1][position[1]] == 1:
                return True
            elif self.characterMap[position[0] + 1][position[1] + 1] == 1:
                return True
            elif self.characterMap[position[0] - 1][position[1] - 1] == 1:
                return True
            elif self.characterMap[position[0]][position[1] + 1] == 1:
                return True
            elif self.characterMap[position[0]][position[1] - 1] == 1:
                return True
            elif self.characterMap[position[0] + 1][position[1] - 1] == 1:
                return True
            elif self.characterMap[position[0] - 1][position[1] + 1] == 1:
                return True
            else:
                return False





#classe level, initialise la carte avec les monstres en fonction du level de la carte
class Level:
    # auteur Gabriel Desmullier
    "a level"
    map=Map()
    def __init__(self,levelNumber,hero):
        # auteur Gabriel Desmullier
        #les personnages du niveau, seul le hero vient de l'exterieur

        self.monsters=[]
        self.merchants=[]

        file = open(r'levelMap.txt', 'r+', encoding="utf-8")
        enregistrement = []

        title=file.readline()#premiere ligne inutile
        for i in range(30):
            enregistrement.append(file.readline()) #enregistrement de toutes les lignes
        file.close()

        #enregistrements des parametres de la carte en fonction du niveau
        engr=enregistrement[levelNumber-1].split(";")
        name=engr[1]
        river=engr[2]
        roads=int(engr[3])
        trees=int(engr[4])
        houses=int(engr[5])
        merchants=int(engr[6])
        monster=int(engr[7])
        levelMonster=int(engr[8])
        levelMerchant=int(engr[9])

        #creation de la carte

        self.map.initialiseListe()
        self.map.groundMapInitialisation(ast.literal_eval(river),roads)
        self.map.decorMapInitialisation(trees,houses)

        #ajout personnages

        for i in range(merchants):
            merchant= ch.Merchant(i,"Marchand "+str(i),levelMerchant,1)
            merchant.position=self.map.adMerchant()
            self.merchants.append(merchant)
        for i in range(monster):
            if levelMonster==1:

                id=random.randint(1,3)
            elif levelMonster==2:

                id=random.randint(4,6)
            else:

                id=random.randint(7,9)
            monster=ch.chargeAMonsterFromDB(id)
            monster.position=self.map.adMonster()
            self.monsters.append(monster)

        self.heroPosition = self.map.adHero() #le level ne garde que la position du hero
        hero.position=self.heroPosition

        print("#############################################")
        print("level:"+str(levelNumber))
        print(str(name))
        print("#############################################")

    def levelPrintMap(self):
        self.map.printMap()

    def moveMonsters(self):
        # auteur Gabriel Desmullier
        #avance tous les monstre d'une maniere qui depend de leur level
        for monster in self.monsters:

            if monster.level==1: #les monstres de niveau 1 se deplacent aleatoirement
                directionMonster=monster.random_move()
                monster.position=self.map.moveCharacter(monster.position,directionMonster,monster.speed)
            elif monster.level==2: #les monstres de niveau 2 se deplacent selon 4 directions
                directionMonster=monster.high_level_smart_move(self.heroPosition)
                monster.position = self.map.moveCharacter(monster.position, directionMonster, monster.speed)
            elif monster.level==3: #les monstres de niveau 3 se deplacent selon 8 directions possibles(diagonales en plus)
                directionMonster = monster.low_level_smart_move(self.heroPosition)
                monster.position = self.map.moveCharacter(monster.position, directionMonster, monster.speed)


    def moveMerchants(self):
        # auteur Gabriel Desmullier
        #avance les marchands de maniere random
        for merchant in self.merchants:
            directionMerchant=merchant.random_move()
            merchant.position=self.map.moveCharacter(merchant.position,directionMerchant,merchant.speed)

    def movehero(self,hero,direction):
        # auteur Gabriel Desmullier
        hero.position=self.map.moveCharacter(hero.position,direction,hero.speed)

    def battles(self,hero):
        # auteur Gabriel Desmullier
        #cherche les monstres qui sont au combat avec le hero et execute les combats, est renvoi l'etat de vie du hero
        for monster in self.monsters:
            if self.map.checkHero(monster.position)==True: #si un monstre est a cote du hero
                result = combat(hero,monster) #il y a un combat
                if result==True:
                    self.map.characterMap[monster.position[0]][monster.position[1]]=0 #le monstre est retire de la carte
                    self.monsters.remove(monster) #supprimer le monstre de la liste
                    hero.inventory.gold=hero.inventory.gold+30
                    hero.exp=hero.exp+10 #gain d'or et d'experience
                else:
                    return False #le hero est mort
        return True

    def shopping(self,hero):
        # auteur Gabriel Desmullier
        #execute l'interaction marchand pour tous les marchands a proximite
        for merchant in self.merchants:
            if self.map.checkHero(merchant.position)==True:
                interactionMerchant(hero,merchant)















