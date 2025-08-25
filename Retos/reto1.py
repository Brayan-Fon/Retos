class Fish:
    def __init__(self):
        self.name = input("Ingresa el nombre del pez: ")
        self.age = input("¿Qué edad tiene el pez? ")
        self.species = input("¿De qué especie es el pez? ")
        self.action = "está nadando en la pecera."

    def details(self):
        print(f"{self.name} tiene {self.age} años, es de la especie {self.species} y {self.action}")

if __name__ == "__main__":
    pez = Fish()
    pez.details()
