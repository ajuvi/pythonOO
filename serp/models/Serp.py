from models.Avatar import Avatar

class Serp(Avatar):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        super
    
    def translate(self,x,y):
        pass

    def pintar(self,panell):
        pass     

    def __str__(self):
        return f"Serp x:{self.x} y:{self.y} w:{self.w} h:{self.y}"
