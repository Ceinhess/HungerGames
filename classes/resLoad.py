import pyglet
import json

derground = pyglet.graphics.OrderedGroup(0)
background = pyglet.graphics.OrderedGroup(1)
middleground = pyglet.graphics.OrderedGroup(2)
filtres = pyglet.graphics.OrderedGroup(3)
foreground = pyglet.graphics.OrderedGroup(4)
fondForeground = pyglet.graphics.OrderedGroup(5)
textForeground = pyglet.graphics.OrderedGroup(6)
upper = pyglet.graphics.OrderedGroup(50)
test = pyglet.graphics.OrderedGroup(100)

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
w = 5
h = 5
resumeJoueurActif = False
joueurMenu = None
winScreen = None
gameWon = False

secteurUrbain_img = pyglet.image.load("res/sprites/secteurUrbain.png")
secteurUrbain_img.anchor_x = secteurUrbain_img.width//2
secteurUrbain_img.anchor_y = secteurUrbain_img.height//2

secteurForet_img = pyglet.image.load("res/sprites/secteurForet.png")
secteurForet_img.anchor_x = secteurForet_img.width//2
secteurForet_img.anchor_y = secteurForet_img.height//2

secteurMarais_img = pyglet.image.load("res/sprites/secteurMarais.png")
secteurMarais_img.anchor_x = secteurMarais_img.width//2
secteurMarais_img.anchor_y = secteurMarais_img.height//2

secteurPlaine_img = pyglet.image.load("res/sprites/secteurPlaine.png")
secteurPlaine_img.anchor_x = secteurPlaine_img.width//2
secteurPlaine_img.anchor_y = secteurPlaine_img.height//2

lumiere_img = pyglet.image.load("res/sprites/lumiere.png")
lumiere_img.anchor_x = lumiere_img.width//2
lumiere_img.anchor_y = lumiere_img.height//2

winFond_img = pyglet.image.load("res/sprites/winFond.png")
winFond_img.anchor_x = winFond_img.width//2
winFond_img.anchor_y = winFond_img.height//2

fond_img = pyglet.image.load("res/sprites/fond.png")
fondMenus_img = pyglet.image.load("res/sprites/fondMenus.png")
suivantButton_img = pyglet.image.load("res/sprites/suivantButton.png")
speedButton_img = pyglet.image.load("res/sprites/speedButton.png")
fondArene_img = pyglet.image.load("res/sprites/fondArene.png")
filtreJour_img = pyglet.image.load("res/sprites/filtreJour.png")
filtreSoir_img = pyglet.image.load("res/sprites/filtreSoir.png")
filtreNuit_img = pyglet.image.load("res/sprites/filtreNuit.png")
resumeJoueur_img = pyglet.image.load("res/sprites/resume.png")



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
