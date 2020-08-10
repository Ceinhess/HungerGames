import pyglet
from classes.resLoad import *
import random
from pyglet import clock
import math
from pyglet.gl import *

window = pyglet.window.Window(1280,720,caption='HG test')

class secteur():
    def __init__(self,xGrid,yGrid,x,y,nom,genre):
        self.x, self.y, self.nom, self.genre = 400+xGrid*fSize, 600+((yGrid-aSize)*fSize), nom, genre
        print(self.y)
        self.xGrid = xGrid
        self.yGrid = yGrid
        self.menuActif = False
        self.blocked = 0 # 0 = non, 1 = will, 2 = oui
        self.batiments = []
        
        glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        
        self.texture = pyglet.sprite.Sprite(secteurUrbain_img,
                                          x= self.x+fSize//2,
                                          y= self.y+fSize//2,
                                          batch = batch,
                                          group = middleground)
        self.texture2 = pyglet.sprite.Sprite(secteurUrbain_img,
                                          x= self.x,
                                          y= self.y,
                                          batch = batch,
                                          group = groupsList[aSize-self.yGrid])
        
        glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        
        self.texture2.scale = fSize/32
        
        if self.genre == "Plaine":
            self.texture.image = secteurPlaine_img
            self.texture2.image = decoPlaine[random.randint(0,len(decoPlaine)-1)]
            self.couleur = CPlaine
            batList = ["Village","Eglise","Champs","Ruines"]
            batRareList = ["Grand village",]
            batChance = random.randint(1,13)
            if batChance == 1:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif batChance == 2:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
            elif 2 < batChance < 6:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif 6 < batChance < 11:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            else:
                self.batiments.append("Champs")
            
        elif self.genre == "Marais":
            self.texture.image = secteurMarais_img
            self.texture2.image = decoMarais[random.randint(0,len(decoMarais)-1)]
            self.couleur = CMarais
            batList = ["Cabane","Ruines","Ruines","Ancien chantier"]
            batRareList = ["Station d'epuration"]
            batChance = random.randint(1,13)
            if batChance == 1:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif 1 < batChance < 3:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif 3 < batChance < 8:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            else:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            
        elif self.genre == "Zone Urbaine":
            self.texture.image = secteurUrbain_img
            self.texture2.image = decoUrbain[random.randint(0,len(decoUrbain)-1)]
            self.couleur = CUrbain
            batList = ["Hopital","Centre Commercial","Pharmacie"]
            batRareList = ["Usine d'armes","Bunker"]
            batChance = random.randint(1,12)
            if batChance == 1:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif 1 < batChance < 3:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif 3 < batChance < 8:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            else:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            
            
        elif self.genre == "Foret":
            self.texture.image = secteurForet_img
            self.texture2.image = decoForet[random.randint(0,len(decoForet)-1)]
            self.couleur = CForet
            batList = ["Village","Eglise","Scierie","Ruines"]
            batRareList = ["Bunker"]
            batChance = random.randint(1,13)
            if batChance == 1:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif batChance == 2:
                self.batiments.append(batRareList[random.randint(0,len(batRareList)-1)])
            elif 2 < batChance < 6:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            elif 6 < batChance < 11:
                self.batiments.append(batList[random.randint(0,len(batList)-1)])
            else:
                self.batiments.append("Ruines")
            
        
        glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        
        self.texture.scale = (fSize+3)/self.texture.width
        
        
        self.text = pyglet.text.Label(text=str(nom),
                                         font_size=25-aSize,
                                         batch = batch,
                                         x=self.x+fSize-10, 
                                         y=self.y+5,
                                         font_name='Pixeltype',
                                         anchor_x='center', anchor_y='center',
                                         group=foreground, bold = True,
                                         color = (255,255,255,255))
        
        self.nombre = pyglet.text.Label(text="",
                                         font_size=50,
                                         font_name='Pixeltype',
                                         batch = batch,
                                         x=self.x+fSize//2+3, 
                                         y=self.y+fSize//2,
                                         anchor_x='center', anchor_y='center',
                                         group=foreground, bold = True)
        
        self.joueursPresents = []
    
    def extend(self):
        if self.blocked !=4:
            if self.yGrid != 0:
                if sec[self.xGrid][self.yGrid-1].blocked == 0 and (sec[self.xGrid][self.yGrid-1].nom*2)%(aSize**2) != 1:
                    sec[self.xGrid][self.yGrid-1].blocked = 1
                    sec[self.xGrid][self.yGrid-1].texture.color = (255,70,130)
                    sec[self.xGrid][self.yGrid-1].texture2.color = (255,70,130)
            if (self.xGrid+1)%aSize != 0:
                if sec[self.xGrid+1][self.yGrid].blocked == 0 and (sec[self.xGrid+1][self.yGrid].nom*2)%(aSize**2) != 1:
                    sec[self.xGrid+1][self.yGrid].blocked = 1
                    sec[self.xGrid+1][self.yGrid].texture.color = (255,70,130)
                    sec[self.xGrid+1][self.yGrid].texture2.color = (255,70,130)
            if self.yGrid != aSize-1:
                if sec[self.xGrid][self.yGrid+1].blocked == 0 and (sec[self.xGrid][self.yGrid+1].nom*2)%(aSize**2) != 1:
                    sec[self.xGrid][self.yGrid+1].blocked = 1
                    sec[self.xGrid][self.yGrid+1].texture.color = (255,70,130)
                    sec[self.xGrid][self.yGrid+1].texture2.color = (255,70,130)
            if (self.xGrid+1)%aSize != 1:
                if sec[self.xGrid-1][self.yGrid].blocked == 0 and (sec[self.xGrid-1][self.yGrid].nom*2)%(aSize**2) != 1:
                    sec[self.xGrid-1][self.yGrid].blocked = 1
                    sec[self.xGrid-1][self.yGrid].texture.color = (255,70,130)
                    sec[self.xGrid-1][self.yGrid].texture2.color = (255,70,130)
            self.blocked = 4


class resume():
    def __init__(self,joueursPresents,genre, nb, couleur,blocked,batiments):
        self.joueursPresents, self.genre, self.nb = joueursPresents, genre, nb
        self.batiments = batiments
        self.y = 630
        self.textes = []
        
        self.textSecteur = pyglet.text.Label(text=("Secteur "+str(self.nb)),
                              font_size=44,
                              batch = batch,
                              font_name='Pixeltype',
                              x=1100, y=680,
                              anchor_x='center', anchor_y='center',
                              group=foreground, bold = True)
        if blocked == 0:
            pass
        elif blocked == 1:
            self.textSecteur.color = (255,200,200,255)
        else:
            self.textSecteur.color = (255,40,40,255)
        
        
        self.textGenre = pyglet.text.Label(text=genre,
                              font_size=26,
                              batch = batch,
                              x=1100, y=660,
                              font_name='Pixeltype',
                              anchor_x='center', anchor_y='center',
                              group=foreground, bold = True,
                              color = couleur)
        
        self.fondMenu = pyglet.sprite.Sprite(fondMenus_img,
                                          x= 950,
                                          y= 0,
                                          batch = batch,
                                          group = middleground)
        
        
        for bats in self.batiments:
            self.textes.append(batButton(bats,self.y))
            self.y -= 35
        for p in joueursPresents:
            self.textes.append(joueurButton(p,self.y))
            self.y -= 35
        self.yB = self.y
        self.yH = 630
        
    def __delete__(self):
        for textess in self.textes:
            textess.__delete__()
        self.textGenre.delete()
        self.textSecteur.delete()
        self.fondMenu.delete()
        del self.textes, self.y, self.joueursPresents
        
        
class logs():
    def __init__(self):
        self.text = []
        self.messages = []
        self.yH = 50
        self.yB = 50
        self.pair = False
        
        self.textSecteur = pyglet.text.Label(text=("Logs "),
                              font_size=44,
                              batch = batch,
                              x=175, y=680,
                              font_name='Pixeltype',
                              anchor_x='center', anchor_y='center',
                              group=foreground, bold = True)
        
        self.fondMenu = pyglet.sprite.Sprite(fondMenus_img,
                                          x= 25,
                                          y= 0,
                                          batch = batch,
                                          group = middleground)
        
    def update(self,message,continu = False, deplacement = False, type = None):
        for mess in self.messages:
            if continu == False:
                mess.y+=16
                mess.update()
            else:
                mess.y+=16
                mess.update()
        
        if joueurActionActif%2 != 0:
            self.pair = True
        
        
        if len(message) > 43:
            self.messages.insert(0,logText(message,50,self.pair,type))
            self.update(message[43:], True, deplacement, type)
            
        else:
            self.messages.insert(0,logText(message,50,self.pair,type))
            if self.pair == True and deplacement == False:
                self.pair = False
            elif deplacement == False:
                self.pair = True
        
        if continu == False:
            self.yH+=16
        else:
            self.yH+=16
        self.messages[0].update()
        self.text.insert(0,message)
        
    def __delete__(self):
        for textes in self.text:
            textes.delete()
        self.textSecteur.delete()
        self.fondMenu.delete()
        del self.text, self.y
        
        
class joueur():
    def __init__(self,x,y,nom,nb):
        self.x, self.y, self.nom, self.nb = x, y, nom, nb
        self.state = "Vivant"
        self.hp = 100
        self.inventaire = []
        self.rifle = "Rien"
        self.arme = "Rien"
    
    def mort(self):
        if self in joueurs:
            joueurs.remove(self)
        if self in sec[self.x][self.y].joueursPresents:
            sec[self.x][self.y].joueursPresents.remove(self)
        self.state = "Mort"
    
    def attack(self,adv,type):
        if type == "CAC":
            if self.arme in armesFaibles:
                power = 0.7
            elif self.arme in armesNormales:
                power = 1
            elif self.arme in armesPuissantes:
                power = 1.4
            else:
                power = 0.5
            
            if adv.arme in armesFaibles:
                advPower = 0.7
            elif adv.arme in armesNormales:
                advPower = 1
            elif adv.arme in armesPuissantes:
                advPower = 1.4
            else:
                advPower = 0.5
                
            dmg = math.floor(random.randint(30,65)*power)
            advDmg = math.floor(random.randint(30,65)*advPower)
            
            if self.arme != "Rien":
                chatLog.update(self.nom+" attaque "+adv.nom+" avec son "+self.arme+", lui infligeant "+str(dmg)+" degats.", False, False, "Battle")
            else:
                chatLog.update(self.nom+" attaque "+adv.nom+" avec ses poings, lui infligeant "+str(dmg)+" degats.", False, False, "Battle")
            
            if adv.arme != "Rien":
                chatLog.update(adv.nom+" attaque "+self.nom+" avec son "+adv.arme+", lui mettant "+str(advDmg)+" degats.", False, False, "Battle")
            else:
                chatLog.update(adv.nom+" attaque "+self.nom+" avec ses poings, lui mettant "+str(advDmg)+" degats.", False, False, "Battle")
            
            
        if type == "DIST":
            if self.rifle in riflesFaibles:
                power = 0.7
            elif self.rifle in riflesNormales:
                power = 1.1
            elif self.rifle in riflesNormales:
                power = 1.7
            else:
                power = 0.2
            
            if adv.rifle in riflesFaibles:
                advPower = 0.7
            elif adv.rifle in riflesNormales:
                advPower = 1.1
            elif adv.rifle in riflesNormales:
                advPower = 1.7
            else:
                advPower = 0.2
                
            dmg = math.floor(random.randint(30,65)*power)
            advDmg = math.floor(random.randint(30,65)*advPower)
            
            if self.rifle != "Rien":
                chatLog.update(self.nom+" attaque "+adv.nom+" avec son "+self.rifle+", lui infligeant "+str(dmg)+" degats.", False, False, "Battle")
            else:
                chatLog.update(self.nom+" attaque "+adv.nom+" avec ses poings, lui infligeant "+str(dmg)+" degats.", False, False, "Battle")
            
            if adv.rifle != "Rien":
                chatLog.update(adv.nom+" attaque "+self.nom+" avec son "+adv.rifle+", lui mettant "+str(advDmg)+" degats.", False, False, "Battle")
            else:
                chatLog.update(adv.nom+" attaque "+self.nom+" avec ses poings, lui mettant "+str(advDmg)+" degats.", False, False, "Battle")
            
        
        
        
        self.hp -= int(advDmg)
        adv.hp -= int(dmg)
        
        if len(joueurs) > 2:
            if self.hp <= 0 and adv.hp > 0:
                chatLog.update(self.nom+" meurt suite a cet affrontement.", False, False, "Death")
                self.mort()
                
            if self.hp > 0 and adv.hp <= 0:
                chatLog.update(adv.nom+" meurt suite a cet affrontement.", False, False, "Death")
                adv.mort()
                
            if self.hp > 0 and adv.hp > 0:
                chatLog.update("Ils decident d'en rester la, aucun d'eux ne meurt.", False, False, "EndBattle")
            
            if self.hp <= 0 and adv.hp <= 0:
                chatLog.update(adv.nom+" et "+self.nom+" meurent des suites de leurs blessures.", False, False, "Death")
                self.mort()
                adv.mort()
        else:
            if self.hp <= 0 and adv.hp > 0:
                chatLog.update(self.nom+" meurt suite a cet affrontement.", False, False, "Death")
                self.mort()
                chatLog.update(adv.nom+" remporte la premiere place du Hunger Games !", False, False, "Win")
                
            if self.hp > 0 and adv.hp <= 0:
                chatLog.update(adv.nom+" meurt suite a cet affrontement.", False, False, "Death")
                adv.mort()
                chatLog.update(self.nom+" remporte la premiere place du Hunger Games !", False, False, "Win")
                
            if self.hp > 0 and adv.hp > 0:
                chatLog.update("Ils decident d'en rester la, aucun d'eux ne meurt.", False, False, "EndBattle")
            
            if self.hp <= 0 and adv.hp <= 0:
                if self.hp >= adv.hp:
                    
                    chatLog.update(self.nom+" elimine "+adv.nom+" dans une derniere bataille decisive.", False, False, "Death")
                    adv.mort()
                    chatLog.update(self.nom+" remporte la premiere place du Hunger Games !", False, False, "Win")
                else:
                    chatLog.update(self.nom+" elimine "+adv.nom+" dans une derniere bataille decisive.", False, False, "Death")
                    self.mort()
                    chatLog.update(adv.nom+" remporte la premiere place du Hunger Games !", False, False, "Win")
        
        for x in range(0, aSize):
            for y in range(0,aSize):
                updateSecteurNumber(sec[x][y])
    
    
    def move(self):
        direction = random.randint(1,4)
        if direction == 1: #Ouest
            if self.y != 0:
                if sec[self.x][self.y-1].blocked == 0:
                    sec[self.x][self.y].joueursPresents.remove(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    self.y-=1
                    
                    sec[self.x][self.y].joueursPresents.append(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    chatLog.update(self.nom+" se deplace vers l'ouest.", True, True,"Deplacement")
                else:
                    self.move()
            else:
                self.move()
        elif direction == 2: #sud
            if (self.x+1)%aSize != 0:
                if sec[self.x+1][self.y].blocked == 0:
                    sec[self.x][self.y].joueursPresents.remove(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    self.x+=1
                    
                    sec[self.x][self.y].joueursPresents.append(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    chatLog.update(self.nom+" se deplace vers le sud.", True, True,"Deplacement")
                else:
                    self.move()
            else:
                self.move()
        elif direction == 3: # est
            if self.y != aSize-1:
                if sec[self.x][self.y+1].blocked == 0:
                    sec[self.x][self.y].joueursPresents.remove(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    self.y+=1
                    
                    sec[self.x][self.y].joueursPresents.append(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    chatLog.update(self.nom+" se deplace vers l'est.", True, True,"Deplacement")
                else:
                    self.move()
            else:
                self.move()
        elif direction == 4: # nord
            if (self.x+1)%aSize != 1:
                if sec[self.x-1][self.y].blocked == 0:
                    sec[self.x][self.y].joueursPresents.remove(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    self.x-=1
                    
                    sec[self.x][self.y].joueursPresents.append(self)
                    updateSecteurNumber(sec[self.x][self.y])
                    
                    chatLog.update(self.nom+" se deplace vers le nord.", True, True,"Deplacement")
                else:
                    self.move()
            else:
                self.move()
        else:
            self.move()
        
class joueurButton():
    def __init__(self,joueur,y):
        self.joueur = joueur
        self.y = y
        self.text = pyglet.text.Label(text=joueur.nom,
                              font_size=30,
                              batch = batch,
                              x=1100, y=self.y,
                              font_name='Pixeltype',
                              anchor_x='center', anchor_y='center',
                              group=foreground)
        self.text.color = (255,int(2.5*self.joueur.hp),int(2.5*self.joueur.hp),255)
        
    def update(self):
        self.text.y = self.y
        if self.y > 642:
            self.text.color = (255,255,255,0)
        else:
            self.text.color = (255,int(2.5*self.joueur.hp),int(2.5*self.joueur.hp),255)
        
    def checkClicked(self,y):
        global joueurMenu
        if self.y-10 < y < self.y +10:
            joueurMenu = playerResume(900,self.y,self.joueur)
        
    def __delete__(self):
        self.text.delete()
        del self.y, self.joueur

class batButton():
    def __init__(self,bat,y):
        self.bat = bat
        self.y = y
        self.text = pyglet.text.Label(text=bat,
                              font_size=30,
                              batch = batch,
                              font_name='Pixeltype',
                              x=1100, y=self.y,
                              anchor_x='center', anchor_y='center',
                              group=foreground,
                              color = (150,95,75,255))
        
    def update(self):
        self.text.y = self.y
        if self.y > 642:
            self.text.color = (255,255,255,0)
        else:
            self.text.color = (255,255,255,255)
        
    def checkClicked(self,y):
        pass
        
    def __delete__(self):
        self.text.delete()
        del self.y, self.bat


class logText():
    def __init__(self,message,y,pair,genre = None):
        self.message, self.y = message, y
        self.genre = genre
        self.pair = GPair
        print(self.pair)
        self.text = pyglet.text.Label(text=message[:43],
                         font_size=12,
                         font_name='Pixel-Life',
                         batch = batch,
                         x=35, y=self.y,
                         anchor_x='left', anchor_y='center',
                         group=foreground)
        
    def update(self):
        self.text.y = self.y
        if self.y > 642:
            self.text.color = (255,255,255,0)
        else:
            if self.pair:
                self.text.color = (255,255,255,255)
            else:
                self.text.color = (190,190,240,255)
            if self.genre == "Death":
                self.text.color = (240,100,110,255)
            elif self.genre == "Battle":
                self.text.color = (200,100,0,255)
            elif self.genre == "EndBattle":
                self.text.color = (200,150,100,255)
            elif self.genre == "Win":
                self.text.color = (255,255,58,255)
            elif self.genre == "Deplacement":
                self.text.color = (190,230,170,255)
    
    def delete(self):
        if self in chatLog.messages:
            chatLog.messages.remove(self)
        self.text.delete()
        del self.y, self.message

class playerResume():
    def __init__(self,x,y, perso):
        global resumeJoueurActif
        
        self.resumeFond = pyglet.sprite.Sprite(resumeJoueur_img,
                                    x= x-400,
                                    y= y-100,
                                    batch = batch,
                                    group = fondForeground)
        
        self.textNom = pyglet.text.Label(text="Nom: "+perso.nom,
                              font_size=44,
                              font_name='Pixeltype',
                              batch = batch,
                              x=x-375, y=y+55,
                              anchor_x='left', anchor_y='center',
                              group=textForeground, bold = True)
        
        self.textVie = pyglet.text.Label(text="Vie: "+str(perso.hp)+"/100",
                              font_size=30,
                              font_name='Pixeltype',
                              batch = batch,
                              x=x-375, y=y+20,
                              anchor_x='left', anchor_y='center',
                              group=textForeground, bold = False)
        
        self.textRifle = pyglet.text.Label(text="Arme a feu: "+perso.rifle,
                              font_size=30,
                              font_name='Pixeltype',
                              batch = batch,
                              x=x-375, y=y-5,
                              anchor_x='left', anchor_y='center',
                              group=textForeground, bold = False)
        
        self.textArme = pyglet.text.Label(text="Arme Melee: "+perso.arme,
                              font_size=30,
                              font_name='Pixeltype',
                              batch = batch,
                              x=x-375, y=y-30,
                              anchor_x='left', anchor_y='center',
                              group=textForeground, bold = False)
        
        resumeJoueurActif = True
        
    def delete(self):
        self.textArme.delete()
        self.textRifle.delete()
        self.textVie.delete()
        self.textNom.delete()
        del self.resumeFond
        

class winningScreen():
    def __init__(self,perso):
        self.winFond = pyglet.sprite.Sprite(winFond_img,
                                    x= 640,
                                    y= 370,
                                    batch = batch,
                                    group = fondForeground)
        self.lumiere = pyglet.sprite.Sprite(lumiere_img,
                                    x= 640,
                                    y= 330,
                                    batch = batch,
                                    group = foreground)
        self.winnerText = pyglet.text.Label(text="gagnant",
                              font_size=20,
                              batch = batch,
                              font_name='Pixeltype',
                              x=640, y=405,
                              anchor_x='center', anchor_y='center',
                              group=textForeground, bold = False)
        self.winnerText.color = (200,200,100,200)
        self.winName = pyglet.text.Label(text=perso.nom,
                              font_size=60,
                              batch = batch,
                              font_name='Pixeltype',
                              x=640, y=380,
                              anchor_x='center', anchor_y='center',
                              group=textForeground, bold = False)
        self.winName.color = (255,255,120,255)
        
        
    def update(self):
        self.lumiere.rotation += 5

class startingMenu():
    def __init__(self):
        self.fond = pyglet.sprite.Sprite(fondMenu_img,
                                    x= 0,
                                    y= 0,
                                    batch = batch,
                                    group = derground)
        
        self.start = pyglet.sprite.Sprite(startButton_img,
                                    x= 515,
                                    y= 40,
                                    batch = batch,
                                    group = foreground)
        
        self.size = pyglet.sprite.Sprite(sizeButton_img,
                                    x= 420,
                                    y= 500,
                                    batch = batch,
                                    group = foreground)
        
        self.textSize = pyglet.text.Label(text="Taille de la map",
                              font_size=36,
                              font_name='Pixeltype',
                              batch = batch,
                              x=640, y=580,
                              anchor_x='center', anchor_y='center',
                              group=textForeground, bold = False,
                              color=(45,180,15,255))
        
        self.textTitle = pyglet.text.Label(text="Hunger Games",
                              font_size=80,
                              font_name='Pixeltype',
                              batch = batch,
                              x=640, y=650,
                              anchor_x='center', anchor_y='center',
                              group=textForeground, bold = False,
                              color=(45,211,15,255))
        
        self.textVersion = pyglet.text.Label(text="v 1.0",
                              font_size=24,
                              font_name='Pixeltype',
                              batch = batch,
                              x=1260, y=8,
                              anchor_x='center', anchor_y='center',
                              group=textForeground, bold = False,
                              color=(45,150,15,175))
        
        self.textCredits = pyglet.text.Label(text="Credits",
                              font_size=24,
                              font_name='Pixeltype',
                              batch = batch,
                              x=5, y=8,
                              anchor_x='left', anchor_y='center',
                              group=textForeground, bold = False,
                              color=(45,150,15,175),
                              multiline=True,
                              width=300)
        
    def destroy(self):
        del self.start, self.fond, self.size
        self.textTitle.delete()
        self.textVersion.delete()
        self.textSize.delete()
        self.textCredits.delete()

@window.event() 
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    if 950 < x < 1250 and 0 < y < 650:
        for a in sec:
            for secteurs in a:
                if secteurs.menuActif == True:
                    
                    if scroll_y > 0 and secteurs.menu.yH > 630:
                        secteurs.menu.yB-=35
                        secteurs.menu.yH-=35
                        for b in secteurs.menu.text:
                            b.y -= 35
                            b.update()
                            
                    elif scroll_y < 0 and secteurs.menu.yB < 0:
                        secteurs.menu.yB+=35
                        secteurs.menu.yH+=35
                        for b in secteurs.menu.text:
                            b.y += 35
                            b.update()
                            
    elif 25 < x < 325 and 0<y<630 and finishedActions:
        if scroll_y > 0 and chatLog.yH > 670:
            chatLog.yB-=80
            chatLog.yH-=80
            for b in chatLog.messages:
                b.y -= 80
                b.update()
                
        elif scroll_y < 0 and chatLog.yB < 50:
            chatLog.yB+=80
            chatLog.yH+=80
            for b in chatLog.messages:
                b.y += 80
                b.update()
        
        for b in chatLog.messages:
            if b.y > 650:
                b.color = (255,255,255,0)
            else:
                b.color = (255,255,255,255)
                            
@window.event()
def on_mouse_press(x, y, button, modifiers):
    global speed, resumeJoueurActif, joueurMenu, mainMenu, aSize, fSize
    if not mainMenu:
        if not resumeJoueurActif:
            if 400 < x < 900 and 100 < y < 600 and button == pyglet.window.mouse.LEFT:
                for a in sec:
                    for secteurs in a:
                        if secteurs.x < x < secteurs.x + fSize and secteurs.y < y < secteurs.y +fSize:
                            if secteurs.menuActif == False:
                                secteurs.menu = resume(secteurs.joueursPresents,secteurs.genre, secteurs.nom, secteurs.couleur,secteurs.blocked,secteurs.batiments)
                                secteurs.menuActif = True
                                if secteurs.blocked == 0:
                                    secteurs.texture.color = (200,200,200)
                                    secteurs.texture2.color = (200,200,200)
                                elif secteurs.blocked == 1:
                                    secteurs.texture.color = (200,100,100)
                                    secteurs.texture2.color = (200,100,100)
                                else:
                                    secteurs.texture.color = (180,50,50)
                                    secteurs.texture2.color = (180,50,50)
                        elif secteurs.menuActif == True:
                            secteurs.menu.__delete__()
                            secteurs.menuActif = False
                            if secteurs.blocked == 0:
                                secteurs.texture.color = (255,255,255)
                                secteurs.texture2.color = (255,255,255)
                            elif secteurs.blocked == 1:
                                secteurs.texture.color = (255,80,80)
                                secteurs.texture2.color = (255,80,80)
                            else:
                                secteurs.texture.color = (255,0,0)
                                secteurs.texture2.color = (255,0,0)
                        
            
            elif 545 < x < 750 and 15 < y < 85 and button == pyglet.window.mouse.LEFT and finishedActions == True and len(joueurs) != 1 :
                advanceTime()
                
            elif 0 < x < 25 and 75 < y < 100 and button == pyglet.window.mouse.LEFT:
                speed = 1.5
            elif 0 < x < 25 and 50 < y < 75 and button == pyglet.window.mouse.LEFT:
                speed = 0.75
            elif 0 < x < 25 and 25 < y < 50 and button == pyglet.window.mouse.LEFT:
                speed = 0.25
            elif 0 < x < 25 and 0 < y < 25 and button == pyglet.window.mouse.LEFT:
                speed = 1/120
                
            elif 900 < x < 1280 and button == pyglet.window.mouse.LEFT:
                for a in sec:
                    for secteurs in a:
                        if secteurs.menuActif:
                            for but in secteurs.menu.textes:
                                but.checkClicked(y)
                
            elif button == pyglet.window.mouse.RIGHT:
                for a in sec:
                    for secteurs in a:
                        if secteurs.menuActif == True:
                            secteurs.menu.__delete__()
                            secteurs.menuActif = False
                            if secteurs.blocked == 0:
                                secteurs.texture.color = (255,255,255)
                                secteurs.texture2.color = (255,255,255)
                            elif secteurs.blocked == 1:
                                secteurs.texture.color = (255,80,80)
                                secteurs.texture2.color = (255,80,80)
                            else:
                                secteurs.texture.color = (255,0,0)
                                secteurs.texture2.color = (255,0,0)
        else:
            resumeJoueurActif = False
            joueurMenu.delete()
            
    else:
        if 515 < x < 765 and 40 < y < 115: #start button in main menu
            generateGame()
            menu.destroy()
            mainMenu = False
            
        #all the map sizes buttons
        elif 430 < x < 490 and 500 < y < 560:
            aSize = 3
        
        elif 520 < x < 580 and 500 < y < 560:
            aSize = 5
        
        elif 610 < x < 670 and 500 < y < 560:
            aSize = 7
        
        elif 700 < x < 760 and 500 < y < 560:
            aSize = 9
        
        elif 790 < x < 850 and 500 < y < 560:
            aSize = 11
        
        elif 0 < x < 100 and 0 < y < 25:
            menu.textCredits.text = ("Fait par: \n@Ceinhes\nConseils graphiques:\n@LouviersTW\n@LeTechwad\n@GogoLePlusBo")
            menu.textCredits.y = 60
        
        
        fSize = 500/aSize
        

def updateSecteurNumber(sect):
    if len(sect.joueursPresents) != 0:
        sect.nombre.text = str(len(sect.joueursPresents))
    elif len(sect.joueursPresents) == 0:
        sect.nombre.text = ""

def advanceTime(dt = 0):
    global temps, finishedActions, sec, nbBlocked, joueurActionActif, phase
    temps += 1
    finishedActions = False
    joueurActionActif = 0
    while len(chatLog.messages) != 0:
        for m in chatLog.messages:
            m.delete()
            
    for t in chatLog.text:
        chatLog.text.remove(t)
        del t
        
    chatLog.text = []
    chatLog.messages = []
    chatLog.yH = 50
    chatLog.yB = 50
    chatLog.pair = False
    
    for y in sec:
        for secteurs in y:
            updateSecteurNumber(secteurs)
            """if len(secteurs.joueursPresents) != 0:
                secteurs.nombre.text = str(len(secteurs.joueursPresents))
            elif len(secteurs.joueursPresents) == 0:
                secteurs.nombre.text = """""
        
    
    if temps == 3:
        sec[0][0].blocked = 1
        sec[0][0].texture.color = (255,80,80)
        sec[0][0].texture2.color = (255,80,80)
        sec[aSize-1][0].blocked = 1
        sec[aSize-1][0].texture.color = (255,80,80)
        sec[aSize-1][0].texture2.color = (255,80,80)
        sec[0][aSize-1].blocked = 1
        sec[0][aSize-1].texture.color = (255,80,80)
        sec[0][aSize-1].texture2.color = (255,80,80)
        sec[aSize-1][aSize-1].blocked = 1
        sec[aSize-1][aSize-1].texture.color = (255,80,80)
        sec[aSize-1][aSize-1].texture2.color = (255,80,80)
        
        
        
    
    if temps%3 == 0 and temps != 3:
        for a in sec:
            for secteurs in a:
                if secteurs.blocked == 2:
                    secteurs.blocked = 3
                    secteurs.texture.color = (255,0,0)
                    secteurs.texture2.color = (255,0,0)
        for a in sec:
            for secteurs in a:
                if secteurs.blocked == 1:
                    secteurs.blocked = 2
                    secteurs.texture.color = (255,0,0)
                    secteurs.texture2.color = (255,0,0)
        for a in sec:
            for secteurs in a:
                if secteurs.blocked == 3:
                    secteurs.extend()
    
    nbBlocked = 0
    for a in sec:
            for secteurs in a:
                if secteurs.blocked != 0:
                    nbBlocked += 1
    
    if temps % 3 == 0:
        phase = "Jour"
        phaseText.color = (255,255,100,255)
        jourText.color = (200,200,100,255)
        filtre.image = filtreJour_img
        for j in joueurs:
            if j.hp < 75:
                j.hp*=100/(100-j.hp)
                if j.hp >75:
                    j.hp = 75
                    
    elif temps % 3 == 1:
        phase = "Soir"
        phaseText.color = (140,220,220,255)
        jourText.color = (140,170,170,255)
        filtre.image = filtreSoir_img
    else:
        phase = "Nuit"
        phaseText.color = (140,140,240,255)
        jourText.color = (120,120,200,255)
        filtre.image = filtreNuit_img
    phaseText.text = phase
    jourText.text = ("Jour "+str((temps//3)+1))
    
    actionPickingLoop(0, 0)


def logSpace():
    for texte in chatLog.messages:
        texte.y+=15
        texte.update()


def actionPickingLoop(dt,nb):
    global finishedActions, GPair
    if nb<len(joueurs):
        if joueurs[nb].state != "Mort":
            pickAction(joueurs[nb])
            logSpace()
            GPair = not GPair
            
            clock.schedule_once(actionPickingLoop,speed,nb+1)
        else:
            actionPickingLoop(0,nb+1)
        
    else:
        finishedActions = True

def pickAction(perso):
    global phase
    if phase != "Nuit":
        ac = random.randint(1,100)
    else:
        ac = random.randint(45,77)

    isMoving = random.randint(1,4)
    moved = False
    print(temps, temps%3)
    
    if (sec[perso.x][perso.y].blocked > 1):
        moved = True
        
    elif (sec[perso.x][perso.y].blocked == 1 and temps%3 == 1):
        moved = True
        
    elif isMoving == 1 and nbBlocked != (aSize**2)-1 and temps%3 != 2:
        moved = True
        
    elif sec[perso.x][perso.y].blocked > 0 and phase == "Soir":
        moved = True
        
    if moved == True:
        perso.move()
    
    sameSecPlayers = []
    for j in joueurs:
        if j.x == perso.x and j.y == perso.y and j.state != "Mort":
            sameSecPlayers.append(j)
    sameSecPlayers.remove(perso)
    
    if sec[perso.x][perso.y].genre == "Marais":
        if 0 <= ac < 50: #["Cabane","Ruines","Ruines","Ancien chantier"]
            if len(sec[perso.x][perso.y].batiments) == 1:
                batInt = 0
            else:
                batInt = random.randint(0,len(sec[perso.x][perso.y].batiments)-1)
            
            batLooted = sec[perso.x][perso.y].batiments[batInt]
            
            if batLooted == "Cabane":
                loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                chatLog.update(perso.nom+" fouille la cabane dans un marais et trouve un "+loot,True)
                if perso.rifle == "Rien":
                    chatLog.update("Il s'en equipe.",True)
                    perso.rifle = loot
                else:
                    loot = armesFaibles[random.randint(0,len(armesFaibles)-1)]
                    if perso.arme == "Rien":
                        chatLog.update("Ayant mieux, il se rabat sur un "+loot,True)
                    else:
                        chatLog.update("Il decide de le laisser.",True)
                    
            elif batLooted == "Ruines":
                if ac > 35:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille des ruines des marais, il deniche un "+loot,True)
                    if perso.rifle not in riflesNormales or perso.rifle not in riflesPuissantes:
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                elif 35 > ac > 15:
                    loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille des ruines innondees, il deniche un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                else:
                    chatLog.update(perso.nom+" fouille des ruines, mais n'y trouve rien.",True)
                    
            elif batLooted == "Ancien chantier":
                if ac > 25:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" cherche des ruines d'un ancien chantier enfoui, trouvant un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" fouille des restes d'un vieux chantier, il trouve un "+loot,True)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
        
            elif batLooted == "Station d'epuration":
                if ac > 40:
                    loot = riflesPuissantes[random.randint(0,len(riflesPuissantes)-1)]
                    chatLog.update(perso.nom+" cherche des ruines d'un ancien chantier enfoui, trouvant un "+loot,True)
                    if (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" fouille des restes d'un vieux chantier, il trouve un "+loot,True)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
        
        elif 50 <= ac < 75:
            if phase == "Jour":
                chatLog.update(perso.nom+ActionJourMarais[random.randint(0,len(ActionJourMarais)-1)],True)
            if phase == "Soir":
                chatLog.update(perso.nom+ActionSoirMarais[random.randint(0,len(ActionSoirMarais)-1)],True)
            if phase == "Nuit":
                chatLog.update(perso.nom+ActionNuitMarais[random.randint(0,len(ActionNuitMarais)-1)],True)
                        
    elif sec[perso.x][perso.y].genre == "Plaine":
        if 0 <= ac < 50: # ["Village","Eglise","Champs","Ruines"] ["Grand village",]
            if len(sec[perso.x][perso.y].batiments) <= 1:
                batInt = 0
            else:
                batInt = random.randint(0,len(sec[perso.x][perso.y].batiments)-1)
            
            batLooted = sec[perso.x][perso.y].batiments[batInt]
            
            if batLooted == "Village":
                loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                chatLog.update(perso.nom+" visite un village abandonne, trouvant un "+loot,True)
                if perso.rifle == "Rien":
                    chatLog.update("Il s'en equipe.",True)
                    perso.rifle = loot
                else:
                    loot = armesFaibles[random.randint(0,len(armesFaibles)-1)]
                    if perso.arme == "Rien":
                        chatLog.update("Ayant mieux, il se rabat sur un "+loot,True)
                    else:
                        chatLog.update("Il decide de le laisser.",True)
                    
            elif batLooted == "Ruines":
                if ac > 35:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille des ruines, il trouve un "+loot,True)
                    if perso.rifle not in riflesNormales or perso.rifle not in riflesPuissantes:
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                elif 35 > ac > 15:
                    loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille des ruines de bombardements, il deniche un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                else:
                    chatLog.update(perso.nom+" fouille des ruines, mais n'y trouve rien.",True)
                    
            elif batLooted == "Eglise":
                if ac > 25:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" cherche une vieille eglise, et trouve un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" fouille un lieu de culte, il trouve un "+loot,moved)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
            
            elif batLooted == "Champs":
                if ac > 35:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" trouve une boite dans des champs, contenant un "+loot,True)
                    if perso.rifle not in riflesNormales or perso.rifle not in riflesPuissantes:
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                elif 35 > ac > 15:
                    loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" trouve un "+loot+" dans un champs.",True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                else:
                    chatLog.update(perso.nom+" passe dans des champs, mais n'y trouve rien.",True)
            
            elif batLooted == "Grand village":
                if ac > 40:
                    loot = armesPuissantes[random.randint(0,len(armesPuissantes)-1)]
                    chatLog.update(perso.nom+" fouille les reste d'un riche village, trouvant un "+loot,True)
                    if (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" pille un grand village, il trouve un "+loot,True)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
        
        elif 50 <= ac < 75:
            if phase == "Jour":
                chatLog.update(perso.nom+ActionJourPlaine[random.randint(0,len(ActionJourPlaine)-1)],True)
            if phase == "Soir":
                chatLog.update(perso.nom+ActionSoirPlaine[random.randint(0,len(ActionSoirPlaine)-1)],True)
            if phase == "Nuit":
                chatLog.update(perso.nom+ActionNuitPlaine[random.randint(0,len(ActionNuitPlaine)-1)],True)
            
                                
                                
    elif sec[perso.x][perso.y].genre == "Foret":
        if 0 <= ac < 50: #["Village","Eglise","Scierie","Ruines"] ["Bunker"]
            if len(sec[perso.x][perso.y].batiments) <= 1:
                batInt = 0
            else:
                batInt = random.randint(0,len(sec[perso.x][perso.y].batiments)-1)
            
            batLooted = sec[perso.x][perso.y].batiments[batInt]
            
            if batLooted == "Village":
                loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                chatLog.update(perso.nom+" visite un village abandonne, trouvant un "+loot,True)
                if perso.rifle == "Rien":
                    chatLog.update("Il s'en equipe.",True)
                    perso.rifle = loot
                else:
                    loot = armesFaibles[random.randint(0,len(armesFaibles)-1)]
                    if perso.arme == "Rien":
                        chatLog.update("Ayant mieux, il se rabat sur un "+loot,True)
                    else:
                        chatLog.update("Il decide de le laisser.",True)
                    
            elif batLooted == "Ruines":
                if ac > 35:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille des ruines, il trouve un "+loot,True)
                    if perso.rifle not in riflesNormales or perso.rifle not in riflesPuissantes:
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                elif 35 > ac > 15:
                    loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille des ruines de bombardements, il deniche un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                else:
                    chatLog.update(perso.nom+" fouille des ruines, mais n'y trouve rien.",True)
                    
            elif batLooted == "Eglise":
                if ac > 25:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" cherche une vieille eglise, et trouve un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesFaibles[random.randint(0,len(armesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille un lieu de culte, il trouve un "+loot,True)
                    if (perso.arme not in armesFaibles) or (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
            
            elif batLooted == "Scierie":
                if ac > 30:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" trouve une malle dans une scierie, contenant un "+loot,True)
                    if perso.rifle not in riflesNormales or perso.rifle not in riflesPuissantes:
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                elif 30 > ac > 10:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" trouve un "+loot+" dans une scierie.",True)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.")
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                else:
                    chatLog.update(perso.nom+" passe dans des champs, mais n'y trouve rien.",True)
            
            elif batLooted == "Bunker":
                if ac > 30:
                    loot = armesPuissantes[random.randint(0,len(armesPuissantes)-1)]
                    chatLog.update(perso.nom+" fouille un vieux bunker, trouvant un "+loot,True)
                    if (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" pille un bunker, il trouve un "+loot,moved)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
        
        elif 50 <= ac < 75:
            if phase == "Jour":
                chatLog.update(perso.nom+ActionJourForet[random.randint(0,len(ActionJourForet)-1)],True)
            if phase == "Soir":
                chatLog.update(perso.nom+ActionSoirForet[random.randint(0,len(ActionSoirForet)-1)],True)
            if phase == "Nuit":
                chatLog.update(perso.nom+ActionNuitForet[random.randint(0,len(ActionNuitForet)-1)],True)
        
    elif sec[perso.x][perso.y].genre == "Zone Urbaine":
        if 0 <= ac < 50: #["Hopital","Centre Commercial","Pharmacie"] ["Usine d'armes","Bunker"]
            if len(sec[perso.x][perso.y].batiments) <= 1:
                batInt = 0
            else:
                batInt = random.randint(0,len(sec[perso.x][perso.y].batiments)-1)
            
            batLooted = sec[perso.x][perso.y].batiments[batInt]
            if batLooted == "Pharmacie":
                loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                chatLog.update(perso.nom+" visite une pharmacie, trouvant dans la reserve un "+loot,True)
                if perso.rifle == "Rien":
                    chatLog.update("Il s'en equipe.",True)
                    perso.rifle = loot
                else:
                    loot = armesFaibles[random.randint(0,len(armesFaibles)-1)]
                    if perso.arme == "Rien":
                        chatLog.update("Ayant mieux, il se rabat sur un "+loot,True)
                    else:
                        chatLog.update("Il decide de le laisser.",True)
                    
            elif batLooted == "Centre Commercial":
                if ac > 35:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille une boutique d'un centre commercial, il trouve un "+loot,True)
                    if perso.rifle not in riflesNormales or perso.rifle not in riflesPuissantes:
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                elif 35 > ac > 15:
                    loot = riflesFaibles[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" fouille un centre commercial, il deniche un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.")
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                        
                else:
                    chatLog.update(perso.nom+" fouille une zone commerciale, mais n'y trouve rien.",True)
                    
            elif batLooted == "Hopital":
                if ac > 25:
                    loot = riflesNormales[random.randint(0,len(riflesFaibles)-1)]
                    chatLog.update(perso.nom+" cherche un vieux hopital, et trouve un "+loot,True)
                    if (perso.rifle not in riflesFaibles) or (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" fouille un hopital, il trouve un "+loot,True)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
            
            elif batLooted == "Bunker":
                if ac > 20:
                    loot = armesPuissantes[random.randint(0,len(armesPuissantes)-1)]
                    chatLog.update(perso.nom+" fouille un vieux bunker, trouvant un "+loot,True)
                    if (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
                else:
                    loot = armesNormales[random.randint(0,len(armesNormales)-1)]
                    chatLog.update(perso.nom+" pille un bunker, il trouve un "+loot,True)
                    if (perso.arme not in armesNormales) or (perso.arme not in armesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.arme = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
            
            elif batLooted == "Usine d'armes":
                if ac > 20:
                    loot = riflesPuissantes[random.randint(0,len(riflesPuissantes)-1)]
                    chatLog.update(perso.nom+" fouille une usine abandonnee d'armes, denichant au passage un "+loot,True)
                    if (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il laisse sa trouvaille sur place.",True)
                else:
                    loot = riflesNormales[random.randint(0,len(riflesNormales)-1)]
                    chatLog.update(perso.nom+" cherche dans des restes d'une usine militaire, il trouve un "+loot,True)
                    if (perso.rifle not in riflesNormales) or (perso.rifle not in riflesPuissantes):
                        chatLog.update("Il s'en equipe.",True)
                        perso.rifle = loot
                    else:
                        chatLog.update("Ayant deja mieux, il le laisse.",True)
        
        elif 50 <= ac < 75:
            if phase == "Jour":
                chatLog.update(perso.nom+ActionJourUrbain[random.randint(0,len(ActionJourUrbain)-1)],True)
            if phase == "Soir":
                chatLog.update(perso.nom+ActionSoirUrbain[random.randint(0,len(ActionSoirUrbain)-1)],True)
            if phase == "Nuit":
                chatLog.update(perso.nom+ActionNuitUrbain[random.randint(0,len(ActionNuitUrbain)-1)],True)
        
    if 75 <= ac <= 100 and len(sameSecPlayers) >= 1:
        adv = sameSecPlayers[random.randint(0,len(sameSecPlayers)-1)]
        types = ["CAC","DIST"]
        perso.attack(adv,types[random.randint(0,1)])
    elif 75 <= ac <= 100 and len(sameSecPlayers) <= 0:
        
        chatLog.update(perso.nom+" se repose.",True)
                    

### initialisation du jeu
def generateGame():
    global phaseText,jourText,fond,Bsuivant,Bspeed,filtre, nb, joueur,chatLog
    chatLog = logs()
    
    for y in range(0,aSize):
        sec.append([])
        for x in range(0,aSize):
            sec[y].append(secteur(x,y,x+(aSize-1),aSize-y,nb, genres[random.randint(0,(len(genres)-1))]))
            nb += 1
    
    i = 0
    for n in prenoms:
        joueurs.append(joueur(random.randint(0,aSize-1),
                              random.randint(0,aSize-1),
                              n,
                              i))
        i+=1
    
    for joueur in joueurs:
        sec[joueur.x][joueur.y].joueursPresents.append(joueur)
        
    for y in sec:
        for secteurs in y:
            if len(secteurs.joueursPresents) != 0:
                secteurs.nombre.text = str(len(secteurs.joueursPresents))
            
    phaseText = pyglet.text.Label(text=phase,
                                  font_size=80,
                                  font_name='Pixeltype',
                                  batch = batch,
                                  x=640, y=680,
                                  anchor_x='center', anchor_y='center',
                                  group=foreground)
    
    jourText = pyglet.text.Label(text=("Jour "+str((temps//3)+1)),
                                  font_size=30,
                                  batch = batch,
                                  x=640, y=652,
                                  font_name='Pixeltype',
                                  anchor_x='center', anchor_y='center',
                                  group=foreground,
                                  color=(220,220,240,255))
    
    fond = pyglet.sprite.Sprite(fond_img,
                               x= 0,
                               y= 0,
                               batch = batch,
                               group = derground)
    
    Bsuivant = pyglet.sprite.Sprite(suivantButton_img,
                               x= 545,
                               y= 15,
                               batch = batch,
                               group = foreground)
    
    Bspeed = pyglet.sprite.Sprite(speedButton_img,
                               x= 0,
                               y= 0,
                               batch = batch,
                               group = foreground)
    
    fondArene = pyglet.sprite.Sprite(fondArene_img,
                               x= 390,
                               y= 90,
                               batch = batch,
                               group = middleground)
    fondArene.scale = 1.02
    
    filtre = pyglet.sprite.Sprite(filtreJour_img,
                               x= 0,
                               y= 0,
                               batch = batch,
                               group = filtres)
    
    advanceTime()

def gameloop(dt):
    global winScreen, gameWon
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    if len(joueurs) == 1 and not gameWon:
        winScreen = winningScreen(joueurs[0])
        gameWon = True
    if gameWon:
        winScreen.update()


@window.event()
def on_draw():
    window.clear()
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    batch.draw()
    
    
if __name__ == '__main__':
    
    clock.schedule_interval(gameloop,1/20)
    
    menu = startingMenu()
    
    
    pyglet.app.run()