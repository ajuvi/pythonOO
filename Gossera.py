from Perro import *

#main
if __name__ == "__main__":
    
    gossera = []
    gossera.append(Perro(1))
    gossera.append(Bulldog(2))
    gossera.append(Bulldog(3))
    gossera.append(Chihuahua(4))
    gossera.append(Chihuahua(5))

    for p in gossera:
        p.ladrar();  


