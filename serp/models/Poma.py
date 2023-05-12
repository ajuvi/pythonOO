import random
from models.Avatar import Avatar

class Poma(Avatar):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.puntuacio=random.randint(1, 10)
    
    def translate(self,x,y):
        pass

    def pintar(self,tauler):
        print("pinta")     

    def __str__(self):
        return f"Poma x:{self.x} y:{self.y} w:{self.w} h:{self.y}"
