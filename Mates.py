#atributs i mètodes estàtics
class Mates:
    #atribut estàtic
    PI = 3.1416

    #mètode estàtic
    @staticmethod
    def perimetre_cercle(radi):
        return 2*Mates.PI*radi

#main
if __name__ == "__main__":
    print('El número Pi és: ', Mates.PI)

    for r in range(10):
        p = Mates.perimetre_cercle(r)
        print('El perímetre d\'un cercre de radi',r,'és',p)
