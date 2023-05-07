#Variables i mètodes estàtics
class Mates:
    #variable de classe
    pi = 3.1416

    #mètode de classe
    @staticmethod
    def perimetre_cercle(radi):
        return 2*Mates.pi*radi

#main
if __name__ == "__main__":
    print('El número Pi és: ', Mates.pi)

    for r in 1..100:
        p = Mates.perimetre_cercle(r)
        print('El perímetre d\'un cercre de radi',r,'és',p)
