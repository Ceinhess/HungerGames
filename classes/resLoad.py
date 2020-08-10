import pyglet
import json
from pyglet.gl import *
import os

glEnable(GL_TEXTURE_2D)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)                                                                                                                               

derground = pyglet.graphics.OrderedGroup(0)
background = pyglet.graphics.OrderedGroup(1)
middleground = pyglet.graphics.OrderedGroup(2)
groupsList = []
for i in range(3,199):
    groupsList.append(pyglet.graphics.OrderedGroup(i))
filtres = pyglet.graphics.OrderedGroup(200)
foreground = pyglet.graphics.OrderedGroup(201)
fondForeground = pyglet.graphics.OrderedGroup(202)
textForeground = pyglet.graphics.OrderedGroup(203)
upper = pyglet.graphics.OrderedGroup(500)
test = pyglet.graphics.OrderedGroup(1000)

batch = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()




"""prenoms = ["Theo","Arnaud","Benjamin","Louis","Jordan","Maxime","Enzo","Kylian","Robert","Yann","Billy","Eude","Jean","Philippe","Francois","Morgan","Paul","Clement","Josh",
           "Raphael","Jim","Alex","Tom","Pierre","Alexandre","Nabil","Emannuel","Julien","William","Joffrey","John","Sofian"]"""

prenoms = []

with open('Joueurs.txt') as json_file:
        prenoms = json.load(json_file)

noms = ["Metivier","Trinette ","Beltane ","Boisvert","Mireault","Boileau","Frechette","Primeau","Monjeau","Marseau"]

genres = ["Foret","Plaine","Marais","Zone Urbaine"]

riflesFaibles = ["Desert Eagle","Baretta","Colt","Glock","Tokarev"]
riflesNormales = ["Uzi","MP5","MAC10","P90","MAG-7"]
riflesPuissantes = ["M24","Dragunov SVU ","M16","AK-47"]

armesFaibles = ["Baton","Batte de baseball"]
armesNormales = ["Marteau","Couteau de cuisine"]
armesPuissantes = ["Machette","Tronconneuse","Couteau militaire"]

CForet = (22,188,0,255)
CUrbain = (190,190,190,255)
CPlaine = (120,220,0,255)
CMarais = (0,150,90,255)

aSize = 5
fSize = 500/aSize

print(11//2)

sec = []
temp = []
nb = 1
joueurs = []
temps = -1
phase = "Jour"
speed = 1/60
actionsRestantes = 0
finishedActions = False
nbBlocked = 0
joueurActionActif = 0

resumeJoueurActif = False
joueurMenu = None
winScreen = None
gameWon = False
GPair = False
mainMenu = True

secteurUrbain_img = pyglet.image.load("res/sprites/secteurs/secteurUrbain.png")
secteurUrbain_img.anchor_x = secteurUrbain_img.width//2
secteurUrbain_img.anchor_y = secteurUrbain_img.height//2

secteurForet_img = pyglet.image.load("res/sprites/secteurs/secteurForet.png")
secteurForet_img.anchor_x = secteurForet_img.width//2
secteurForet_img.anchor_y = secteurForet_img.height//2

secteurMarais_img = pyglet.image.load("res/sprites/secteurs/secteurMarais.png")
secteurMarais_img.anchor_x = secteurMarais_img.width//2
secteurMarais_img.anchor_y = secteurMarais_img.height//2

secteurPlaine_img = pyglet.image.load("res/sprites/secteurs/secteurPlaine.png")
secteurPlaine_img.anchor_x = secteurPlaine_img.width//2
secteurPlaine_img.anchor_y = secteurPlaine_img.height//2

lumiere_img = pyglet.image.load("res/sprites/GUI/lumiere.png")
lumiere_img.anchor_x = lumiere_img.width//2
lumiere_img.anchor_y = lumiere_img.height//2

winFond_img = pyglet.image.load("res/sprites/GUI/winFond.png")
winFond_img.anchor_x = winFond_img.width//2
winFond_img.anchor_y = winFond_img.height//2

fond_img = pyglet.image.load("res/sprites/GUI/fond.png")
fondMenu_img = pyglet.image.load("res/sprites/GUI/fondMenu.png")
fondMenus_img = pyglet.image.load("res/sprites/GUI/fondMenus.png")
suivantButton_img = pyglet.image.load("res/sprites/GUI/suivantButton.png")
sizeButton_img = pyglet.image.load("res/sprites/GUI/sizeButton.png")
startButton_img = pyglet.image.load("res/sprites/GUI/startButton.png")
speedButton_img = pyglet.image.load("res/sprites/GUI/speedButton.png")
fondArene_img = pyglet.image.load("res/sprites/GUI/fondArene.png")
filtreJour_img = pyglet.image.load("res/sprites/GUI/filtreJour.png")
filtreSoir_img = pyglet.image.load("res/sprites/GUI/filtreSoir.png")
filtreNuit_img = pyglet.image.load("res/sprites/GUI/filtreNuit.png")
resumeJoueur_img = pyglet.image.load("res/sprites/GUI/resume.png")

pyglet.font.add_file('res/font/ARCADECLASSIC.ttf')
arcade_classic = pyglet.font.load('ArcadeClassic')

pyglet.font.add_file('res/font/Pixeltype.ttf')
pixel_type = pyglet.font.load('Pixeltype')

pyglet.font.add_file('res/font/Pixel-Life.ttf')
pixelartFont = pyglet.font.load('Pixel-Life')

decoMarais = []
decoForet = []
decoUrbain = []
decoPlaine = []

for filename in os.listdir("res/sprites/secteursDeco/marais"):
    decoMarais.append(pyglet.image.load("res/sprites/secteursDeco/marais/"+filename))
    
for filename in os.listdir("res/sprites/secteursDeco/foret"):
    decoForet.append(pyglet.image.load("res/sprites/secteursDeco/foret/"+filename))
    
for filename in os.listdir("res/sprites/secteursDeco/urbain"):
    decoUrbain.append(pyglet.image.load("res/sprites/secteursDeco/urbain/"+filename))
    
for filename in os.listdir("res/sprites/secteursDeco/plaine"):
    decoPlaine.append(pyglet.image.load("res/sprites/secteursDeco/plaine/"+filename))

ActionJourMarais = [" observe ses ennemis de loin.",
                    " se motive a traverser le marais.",
                    " se couvre de boue pour mieux se camoufler.",
                    " evite le contact avec les autres.",
                    " est completement perdu.",
                    " repere des ruines, mais s'en approche pas."]
ActionSoirMarais = [" fais un stock de baies.",
                    " chasse ce qu'il arrive a trouver dans le marais.",
                    " ramasse du petit bois.",
                    " allume un feu."
                    " se fait un lit de feuilles.",
                    " remplit sa gourde d'eau qu'il a trouve.",
                    " trouve une boite... vide.",
                    " change de position au cas ou."]
ActionNuitMarais = [" s'endort paisiblement.",
                    " souffre d'une grosse insomnie.",
                    " n'arrive pas a dormir a cause d'une intoxication alimentaire.",
                    " compte les moutons, sans resultat.",
                    " compte les moutons, et s'endort.",
                    " profite d'un sommeil reparateur.",
                    ", ayant peur du marais de nuit, reste eveille.",
                    " eteint son feu sans faire expres.",
                    ", n'arrivant pas a dormir, se balade.",
                    " pleure en pensant a ses parents.",
                    " vois des lumieres au loin, et n'arrive pas a dormir.",
                    " s'endort.",
                    " reste de garde toute la nuit."]

ActionJourPlaine = [" court a travers les champs pour se defouller.",
                    " enquete dans des ruines.",
                    " recolte des legumes dans un potager abandonne.",
                    " fuit un ennemi.",
                    " est trop fatigue et finit par se reposer.",
                    " ne trouve rien a fouiller.",
                    " trouve le campement abandonne d'une autre personne."]
ActionSoirPlaine = [" ramasse du petit bois.",
                    " recolte des champs pour pouvoir manger.",
                    " chasse les animaux present dans les plaines.",
                    " utilise des branches et des feuilles pour cacher son campement."
                    " s'installe dans les ruines d'une maison.",
                    " reussit a allumer son feu."]
ActionNuitPlaine = [" s'endort paisiblement.",
                    " ne dort pas a cause d'une grosse insomnie.",
                    " compte les moutons, sans resultat.",
                    " compte les moutons, et s'endort.",
                    " profite d'un sommeil reparateur.",
                    " entends des voix dans les ruines.",
                    " perd son feu a cause du vent.",
                    ", n'arrivant pas a dormir, se balade.",
                    " pleure en pensant a ses parents.",
                    " vois des lumieres au loin, et n'arrive pas a dormir.",
                    " s'endort.",
                    " reste de garde toute la nuit.",
                    " a peur des ombres des ruines."]

ActionJourUrbain = [" ne trouve rien dans un batiment.",
                    " cherche les carcasses de voitures.",
                    " cours a travers une zone industrielle.",
                    " fait du reperage sur un toit.",
                    " fouille des petits magasins.",
                    " cherche des munitions.",
                    " fait un stock de provisions.",
                    " bande ses blessures comme il peut.",
                    " trouve un GPS.",
                    " repere un ennemi, mais l'ignore."]
ActionSoirUrbain = [" prepare un abri.",
                    " fait un stock de nourriture et de boissons.",
                    " s'abrite dans un batiment isole.",
                    " se pose sur un toit.",
                    " engage une conversation avec un autre survivant.",
                    " s'abrite dans une voiture encore fonctionelle."]
ActionNuitUrbain = [" s'endort paisiblement.",
                    " ne dort pas a cause d'une grosse insomnie.",
                    " compte les moutons, et s'endort.",
                    " profite d'un sommeil reparateur.",
                    " entends des voix en bas des immeubles.",
                    " provoque un incendie dans la ville. Bravo.",
                    ", n'arrivant pas a dormir, se balade.",
                    " pleure en pensant a ses parents.",
                    " vois des lumieres au loin, et n'arrive pas a dormir.",
                    " s'endort.",
                    " reste de garde toute la nuit.",
                    " a peur des ombres des batiments.",
                    " entends des vehicules qui roulent."]

ActionJourForet = [" coupe du bois en prevision.",
                   " vole un campement abandonne.",
                   " cours toute la journee apres un animal.",
                   " repense a ses actions passees.",
                   " prie pour sa survie.",
                   " trouve un paquet de provisions.",
                   " essaye de renover une tronconneuse, sans resultat.",
                   " fuit.",
                   " fabrique une petite cabane. Elle s'ecroule."]
ActionSoirForet = [" recolte du bois.",
                   " allume un feu, mais l'eteint apres car il est dans une foret.",
                   " s'abrite dans une cabane.",
                   " se fait un toit de feuilles.",
                   " fait cuire sa viande avec un petit feu.",
                   " s'endort deja.",
                   " relache la pression."]
ActionNuitForet = [" s'endort paisiblement.",
                    " ne dort pas a cause d'une grosse insomnie.",
                    " compte les moutons, et s'endort.",
                    " profite d'un sommeil reparateur.",
                    " entends des voix en bas des immeubles.",
                    " provoque un incendie qui se propage dans la foret.",
                    ", n'arrivant pas a dormir, va s'entrainer.",
                    " pleure..",
                    " vois des lumieres au loin, et n'arrive pas a dormir.",
                    " s'endort.",
                    " reste de garde toute la nuit.",
                    " a peur des ombres des arbres."]
