from abc import ABC, abstractmethod
import math

#declaració de interficie pintar
class IPintar(ABC):
    @abstractmethod
    def pintar(self): pass

#implementació de la interfície pintar
class Rectangle(IPintar):

    def __init__(self, amplada, alçada):
        #atributs d'objecte
        self.alçada = amplada
        self.amplada = alçada

    def pintar(self):
        for i in range(self.amplada):
            for j in range(self.alçada):
                if i==0 or i==self.amplada-1 or j==0 or j==self.alçada-1:
                    print('x',end='')
                else:
                    print(' ',end='')
            print("")

#implementació de la interfície pintar
class Quadrat(IPintar):

    def __init__(self, costat):
        #atributs d'objecte
        self.costat = costat

    def pintar(self):
        for i in range(self.costat):
            for j in range(self.costat):
                if i==0 or i==self.costat-1 or j==0 or j==self.costat-1:
                    print('x',end='')
                else:
                    print(' ',end='')
            print("")

#main
if __name__ == "__main__":
    figures = []
    figures.append(Rectangle(10,3))
    figures.append(Quadrat(5))    
    figures.append(Rectangle(20,3))    
    figures.append(Quadrat(10))       

    for f in figures:
        f.pintar()
        print("")