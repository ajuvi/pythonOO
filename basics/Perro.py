class Perro():

    def __init__(self, xip=-1):
        self.xip = xip

    def ladrar(self):
        return "Perro Ladrando"
    
    def dormir(self):
        return "Perro Durmiendo"

class Chihuahua(Perro):
    def ladrar(self):
        return "Chihuahua Ladrando"
    
    def dormir(self):
        return "Chihuahua Durmiendo"

class Bulldog(Perro):
    def ladrar(self):
        return "Bulldog Ladrando"
    
    def dormir(self):
        return "Bulldog Durmiendo"

#main
gos1 = Perro()
gos2 = Chihuahua()
gos3 = Bulldog()

print(gos1.ladrar())
print(gos2.ladrar())
print(gos3.ladrar())

print(gos1.dormir())
print(gos2.dormir())
print(gos3.dormir())

