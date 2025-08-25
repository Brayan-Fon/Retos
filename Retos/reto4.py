class Cat:
    def __init__(self):
        self.name = input("Escribe el nombre del gato: ")
        self.age = input("Edad del gato: ")
        self.species = input("Especie: ")

    def describe(self):
        print(f"{self.name} tiene {self.age} años y pertenece a la especie {self.species}")

    def sleep(self):
        print(f"{self.name} está durmiendo plácidamente.")


if __name__ == "__main__":
    cat = Cat()
    cat.describe()
    cat.sleep()
