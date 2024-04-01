from Perro import Perro, Bulldog, Chihuahua

#main
if __name__ == "__main__":
    
    perrera = []
    perrera.append(Perro(1))
    perrera.append(Bulldog(2))
    perrera.append(Bulldog(3))
    perrera.append(Chihuahua(4))
    perrera.append(Chihuahua(5))

    for p in perrera:
        p.ladrar();  


