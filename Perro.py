#declaració de la classe Perro
class Perro():

    #constructor per defecte de la classe Perro
    def __init__(self, xip):
        self.xip = xip

    #mètode d'instància
    def ladrar(self):
        print("Perro Ladrando")

    #mètode d'instància
    def dormir(self):
        print("Perro Durmiendo")

#herència de la classe Perro
class Chihuahua(Perro):

    #sobreescriure el mètode ladrar de Perro
    def ladrar(self):
        print("Chihuahua Ladrando")

    def __str__(self):
        return f"Chihuahua: {self.xip}"

#herència de la classe Perro
class Bulldog(Perro):

    #sobreescriure el mètode ladrar de Perro
    def ladrar(self):
        print("Bulldog Ladrando")

    #sobreescriure el mètode dormir de Perro    
    def dormir(self):
        print("Bulldog Durmiendo")

    def __str__(self):
        return f"Bulldog: {self.xip}"

#main
if __name__ == "__main__":
    
    #crear tres Perro
    gos1 = Perro(20)
    gos2 = Chihuahua(30)
    gos3 = Bulldog(40)

    #afegir el objectes en un array de Perro
    gossos = [gos1,gos2]
    gossos.append(gos3)

    #lladrar a tots els gossos
    for gos in gossos:
        gos.ladrar()

    #dormir a tots els gossos
    for gos in gossos:
        gos.dormir()
    
    #mostrar a tots els gossos
    for gos in gossos:
        print(gos)
    
