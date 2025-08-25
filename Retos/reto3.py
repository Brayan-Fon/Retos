from reto2 import Dog

class Cat:
    def __init__(self):
        self.name = input("Nombre del gato: ")
        self.age = input("Edad del gato: ")
        self.species = input("Especie del gato: ")

    def info(self):
        print(f"El gato {self.name} tiene {self.age} años y es de la especie {self.species}")


class Bird:
    def __init__(self):
        self.name = input("Nombre del pájaro: ")
        self.age = input("Edad del pájaro: ")
        self.species = input("Especie del pájaro: ")

    def info(self):
        print(f"El pájaro {self.name} tiene {self.age} años y es de la especie {self.species}")


class Zoo:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def show(self):
        print("\nLista de animales en el zoológico:")
        for a in self.animals:
            print(f"- {a.__class__.__name__}: {a.name}")


if __name__ == "__main__":
    zoo = Zoo()

    perro = Dog()
    perro.bring()

    gato = Cat()
    gato.info()

    pajaro = Bird()
    pajaro.info()

    zoo.add(perro)
    zoo.add(gato)
    zoo.add(pajaro)

    zoo.show()
