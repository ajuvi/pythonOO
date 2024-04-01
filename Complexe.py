#importar una bilbioteca
import math

#declarar la classe
class Complexe:
    
    #contructor de la classe
    def __init__(self, real, imaginari):
        #atributs d'objecte
        self.real = real
        self.imaginari = imaginari

    #mètode d'objecte    
    def abs(self):
        return math.sqrt(self.real*self.real+self.imaginari*self.imaginari)
    
    #mètode de classe
    @staticmethod
    def suma(c1,c2):
        return Complexe(c1.real+c2.real,c1.imaginari+c2.imaginari)

    #mètode que converteix l'objecte a str
    def __str__(self):
        return '[' + str(self.real) + ',' + str(self.imaginari) + 'i]'

#main
if __name__ == "__main__":
    #crear dos objectes
    com1 = Complexe(2,3)
    com2 = Complexe(1,2)

    #excutar un mètode de classe
    com3 = Complexe.suma(com1,com2)

    #printar els objectes, executant de manera implícita el mètode __str__
    print(com1)
    print(com2)
    print(com3)
