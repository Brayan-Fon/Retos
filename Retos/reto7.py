from reto2 import Dog
from reto3 import Cat, Bird

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, animal):
        self.pets.append(animal)
        print(f"{self.name} adoptó a {animal.name}.")

    def feed(self):
        print(f"\n{self.name} está alimentando a sus mascotas:")
        for pet in self.pets:
            print(f"- {pet.name} está comiendo.")


if __name__ == "__main__":
    owner = Owner("Carlos")

    perro = Dog()
    perro.bring()

    gato = Cat()
    gato.info()

    pajaro = Bird()
    pajaro.info()

    owner.add_pet(perro)
    owner.add_pet(gato)
    owner.add_pet(pajaro)

    owner.feed()
