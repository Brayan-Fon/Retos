class Bird:
    def __init__(self):
        self.name = input("Nombre del ave: ")
        self.age = input("Edad del ave: ")
        self.species = input("Especie: ")

    def details(self):
        print(f"{self.name} tiene {self.age} años y es de la especie {self.species}")


class Parrot(Bird):
    def __init__(self):
        super().__init__()
        self.phrase = input(f"¿Qué quieres que repita {self.name}? ")

    def speak(self):
        print(f"{self.name} dice: '{self.phrase}'")


if __name__ == "__main__":
    loro = Parrot()
    loro.details()
    loro.speak()
