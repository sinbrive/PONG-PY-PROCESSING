'''
OOP
- v1
    - objet rec, ball
- v2 : 
    - setmiddle
    - resetSpeed
    - bug : vx=-vx out of collideRec in Ball() ?
- v3 : 
    - class game
- v3.1 : 
    - onkey
    - gamme, Raquette, ball independent
- v4
    - onkey revwed
    - font changed for scores
    - fr for game and en for classes
    - col = yellow by default in classes methods
    - https://stackoverflow.com/a/62864206 issue
    
'''

from items import Paddlet, Ball, Game


# raquettes
largeur=15
hauteur=100

VITESSE=5

BORD=5

def setup():
    global game, raq1, raq2, balle
    
    size(800, 600)
        
    raq1 = Paddlet(BORD, height/2, largeur, hauteur)
    raq2 = Paddlet(width-5-largeur, height/2, largeur, hauteur)
    balle = Ball(100, 100, 20, VITESSE)
    
    game = Game(raq1, raq2, balle)
    

    
    
def draw(): 
   
    background(90)

    # movements
    raq2.move()
    raq1.moveMouse() 
    balle.move()
    
    # detection collision joueur gauche       
    if balle.collideRec(raq1):
            balle.changeDirection()
            balle.x = raq1.x+raq1.w+balle.r  # see issue : https://stackoverflow.com/a/62864206
    else:
        if balle.isOut(raq1):
            balle.resetSpeed(+1)
            balle.setMiddle(raq1)
            game.setScore(raq2)
            game.waitAction()

    # detection collision joueur droit       
    if balle.collideRec(raq2):
        balle.changeDirection()
        balle.x = raq2.x-balle.r  # see issue : https://stackoverflow.com/a/62864206
    else:
        if balle.isOut(raq2):
            balle.resetSpeed(-1)
            balle.setMiddle(raq2)
            game.setScore(raq1)
            game.waitAction()
            
    # affichage
    game.display()

def mouseClicked():
    game.restart()
    
def keyPressed():
    raq2.onKey(True)

def keyReleased():
    raq2.onKey(False)
