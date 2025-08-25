class Bird:
    def __init__(self):
        self.name = input("Nombre del ave: ")
        self.age = input("Edad del ave: ")
        self.species = input("Especie del ave: ")

    def show(self):
        print(f"Ave: {self.name}, {self.age} años, especie {self.species}")


class Eagle(Bird):
    def __init__(self):
        super().__init__()
        self.altitude = int(input("Altura de vuelo del águila (m): "))

    def flight(self):
        print(f"El águila {self.name} vuela a {self.altitude} metros de altura.")


if __name__ == "__main__":
    eagle = Eagle()
    eagle.show()
    eagle.flight()
