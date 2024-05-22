class Persona:

    def __init__(self,nom,cognoms):
        self.nom=nom
        self.cognoms=cognoms

    def mostrar(self):
        print(self)

    def __str__(self):
        return f"Persona: {self.nom} {self.cognoms}"        

class Futbolista(Persona):

    def __init__(self,nom,cognoms,equip):
        super().__init__(nom,cognoms)
        self.equip=equip
        self.lesionat=False

    def mostrar(self):
        print(f"Futbolista: {self.nom} {self.cognoms}")

class Entrenador(Persona):
    def __init__(self,nom,cognoms,equip):
        super().__init__(nom,cognoms)
        self.equip=equip

    def mostrar_entrenador(self):
        print(self)

    def __str__(self):
        return f"Entrenador {self.equip}: {self.nom} {self.cognoms}"


#main
if __name__ == "__main__":
    p1=Entrenador("Xavi","Hernandez","Girona Fc")
    p1.mostrar()
    print(p1)