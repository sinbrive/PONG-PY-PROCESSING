

class Game():
    def __init__(self, _left, _right, _ball):
        self.gameOver=False
        self.leftPlayer=0
        self.rightPlayer=0
        self.padLeft = _left
        self.padRight = _right
        self.ball = _ball      
        
    def setScore(self, rec):
        if rec.x < width/2:
            self.leftPlayer += 1
        else:
            self.rightPlayer += 1

    def waitAction(self):
        fill(0,255,255)
        textAlign(CENTER)
        if self.rightPlayer>=11 or self.leftPlayer>=11:
            if self.rightPlayer > self.leftPlayer:
                message = "Le gagnant est Joueur Droit"
            else:
                message = "Le gagnant est Joueur Gauche"
            textSize(30)
            text(message, width/2, height/2-50)
            textSize(25)
            text("Clic droit pour relancer", width/2, height-50)
            self.gameOver = True
        else :
            textSize(25)
            text("Clic pour continuer", width/2, height-50)
        noLoop()

    def restart(self):
        if mouseButton == RIGHT and self.gameOver:
            self.gameOver = False
            self.rightPlayer = 0
            self.leftPlayer = 0        
            loop()  # relancer
        if mouseButton == LEFT and not self.gameOver:
            loop()
    
        
    def display(self, col=color(255,255,0)):
        fill(col)
        textAlign(CENTER)
        font = loadFont('Algerian-48.vlw')
        textFont(font)
        text(str(self.leftPlayer), width/4, 40)
        text(str(self.rightPlayer), 3*width/4, 40)
        font = createFont("Arial",48,True)  # popstyle not working
        textFont(font)
        self.ball.display()
        self.padLeft.display()
        self.padRight.display()
        stroke(255,255,0)
        line(width/2, 0, width/2, height)


class Paddlet():
    def __init__(self,_x, _y, _w, _h):
        self.down=False
        self.up=False
        self.x=_x
        self.y=_y
        self.w=_w
        self.h=_h
        
    def onKey(self, _on):
        if key == 'z':
            self.up=_on
        elif key == 's':
            self.down=_on
    
    def moveUp(self, step=10):
        if self.y > 0:
            self.y = self.y - step 
        
    def moveDown(self, step=10):
        if self.y < height-self.h:
            self.y=self.y+step
            
    def move(self):
        if self.down:
            self.moveDown()
        if self.up:
            self.moveUp()
        
    def moveMouse(self):
        self.y=mouseY
        if self.y>height-self.h: 
            self.y=height-self.h
        
    def display(self, col=color(255,255,0)):
        fill(col)
        rect(self.x, self.y, self.w, self.h) 

#...........    
class Ball():
    def __init__(self,_x, _y, _d, _v):
        self.x=_x
        self.y=_y
        self.r=_d/2
        self.vx=_v
        self.vy=_v
        self.v=_v
        
    def move(self):
        if self.y > height-self.r:
            self.vy = -self.vy
            
        if self.y < 10:
            self.vy = -self.vy
            
        self.x += self.vx
        self.y += self.vy
    
    def setMiddle(self, rec):
        if rec.x<width/2:
            self.x=rec.x+rec.w+self.r
        else:
            self.x=rec.x-self.r    
        self.y=rec.y+rec.h/2
            
    def changeDirection(self):
        self.vx*=-1

    def resetSpeed(self, sign=1):
        self.vx = sign*abs(self.v)
        self.vy = sign*abs(self.v)-random(-1, 1)
            
    def collideRec(self, rec):
        x_b = self.x - self.r
        y_b = self.y - self.r
        w_b = 2*self.r
        h_b = 2*self.r
        # collision of two rectangles
        if (x_b < rec.x + rec.w and x_b + w_b > rec.x and y_b < rec.y + rec.h and h_b + y_b > rec.y):
            return True
        return False  

    def isOut(self, rec):
        if rec.x<width/2:
            return (self.x < 0)
        else:
            return (self.x > width)
        
    def display(self, col=color(255,255,0)):
        fill(col)
        ellipse(self.x, self.y, 2*self.r, 2*self.r)    
        
                   
                                
                                                
