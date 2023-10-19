import turtle as t
from random import randint, choice
HAUTEUR_DESSIN = 600
LARGEUR_DESSIN = 1500
NIVEAU_SOL = -200
t.colormode(255)
t.title("La ri zabim")  #Change le titre
t.bgcolor("skyblue")  #Met fond en noir
t.setup(LARGEUR_DESSIN, HAUTEUR_DESSIN) # Taille fenêtre
t.speed(10)

def batiment(pos_case, largeur_case, nb_etages):
    HAUTEUR_MUR = 50
    def facade():
        def etage(num_etage):
            def mur():
                t.up()
                t.goto(pos_case, NIVEAU_SOL + HAUTEUR_MUR * num_etage)
                #t.color("black", choice(["pink", "blue", "green"]))
                t.color("black",(randint(0,255),randint(0,255) ,randint(0,255)))
                t.begin_fill()
                t.down()
                for i in range(2):
                    t.forward(largeur_case)
                    t.left(90)
                    t.forward(HAUTEUR_MUR)
                    t.left(90)
                t.up()
                t.end_fill()
            
            def ouvertures():
                LARGEUR_FENETRE = 20
                if largeur_case < 150:
                    nb_fenetres = 2
                elif 150 <= largeur_case < 200:
                    nb_fenetres = 3
                else:
                    nb_fenetres = 4
                ecart = (largeur_case - nb_fenetres  * LARGEUR_FENETRE) / (nb_fenetres + 1)
                for num_fenetre in range(nb_fenetres):
                    t.up()
                    if num_etage == 0:
                        HAUTEUR_BAS = 0
                        HAUTEUR_FENETRE = 40                        
                    else:
                        HAUTEUR_BAS = 10
                        HAUTEUR_FENETRE = 30
                    t.goto(pos_case + (ecart + (LARGEUR_FENETRE + ecart) * num_fenetre) \
                           , NIVEAU_SOL + HAUTEUR_BAS + HAUTEUR_MUR * num_etage)
                    #t.color("black", choice(["pink", "blue", "green"]))
                    t.color("black",(randint(0,255),randint(0,255) ,randint(0,255)))
                    t.begin_fill()
                    t.down()
                    for i in range(2):
                        t.forward(LARGEUR_FENETRE)
                        t.left(90)
                        t.forward(HAUTEUR_FENETRE)
                        t.left(90)
                    t.up()
                    t.end_fill()                
                
            mur()
            ouvertures()
        
        for num in range(nb_etages):
            etage(num)

        
    def toit():
        def toit_simple():
            HAUTEUR_TOIT = 20
            t.up()
            t.color("black",choice(["green", "red", "grey"]))
            t.begin_fill()
            t.goto(pos_case, NIVEAU_SOL + HAUTEUR_MUR * nb_etages)
            t.down()
            t.goto(pos_case + largeur_case / 2\
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages + HAUTEUR_TOIT)
            t.goto(pos_case + largeur_case \
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages)
            t.goto(pos_case, NIVEAU_SOL + HAUTEUR_MUR * nb_etages)
            t.end_fill()
            
        def toit_chapeau():
            HAUTEUR_TOIT = 20
            t.up()
            t.color("black",choice(["green", "red", "grey"]))
            t.begin_fill()
            t.goto(pos_case, NIVEAU_SOL + HAUTEUR_MUR * nb_etages)
            t.down()
            t.goto(pos_case + largeur_case / 4\
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages + (HAUTEUR_TOIT / 3))
            t.goto(pos_case + largeur_case / 2.2\
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages + HAUTEUR_TOIT)
            t.goto(pos_case + largeur_case / 1.8\
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages + HAUTEUR_TOIT)
            t.goto(pos_case + largeur_case * 3 / 4\
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages + (HAUTEUR_TOIT / 3))
            t.goto(pos_case + largeur_case \
                   , NIVEAU_SOL + HAUTEUR_MUR * nb_etages)
            t.goto(pos_case, NIVEAU_SOL + HAUTEUR_MUR * nb_etages)
            t.end_fill()
        if nb_etages < 3:
            if choice([True, False]):
                toit_simple()
            else:
                toit_chapeau()
    t.pensize(2)
    facade()
    toit()

def route():
    t.up()
    t.setheading(0)
    t.goto(- LARGEUR_DESSIN / 2 , (- (HAUTEUR_DESSIN / 2) + NIVEAU_SOL) / 2)
    t.pensize(-NIVEAU_SOL / 2)
    t.color("grey")
    t.down()    
    t.forward(LARGEUR_DESSIN)
    t.up()
    
class Batiment:
    
    def __init__(self, pos_case, largeur_case, nb_etages):
        self._pos_case = pos_case
        self._largeur_case = largeur_case
        self._nb_etages = nb_etages
        
    def dessiner_batiment(self):
        batiment(self._pos_case, self._largeur_case, self._nb_etages)

        

route()
position_x = - LARGEUR_DESSIN / 2
largeur_case = randint(100, 250)
case1 = Batiment(pos_case = 100, largeur_case = 100, nb_etages = 2)
case1.dessiner_batiment()
i = 0
while (position_x + largeur_case) < LARGEUR_DESSIN / 2: # Tant qu'il est possible d'ajouter
    case1.append(Batiment(pos_case, largeur_case, nb_etages))
    case[i].dessiner_batiment()
    position_x += largeur_case
    largeur_case = randint(100, 250)
case = Batiment(position_x, LARGEUR_DESSIN / 2 - position_x, randint(1, 4))
    
"""
while (position_x + largeur_case) < LARGEUR_DESSIN / 2: # Tant qu'il est possible d'ajouter 
    batiment(position_x, largeur_case, randint(1, 4))
    position_x += largeur_case
    largeur_case = randint(100, 250)
batiment(position_x, LARGEUR_DESSIN / 2 - position_x, randint(1, 4)) # dernière case
"""
t.hideturtle()
t.done()

















