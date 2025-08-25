class Bird:
    def __init__(self):
        self.name = input("Nombre del ave: ")
        self.age = input("Edad del ave: ")
        self.species = input("Especie: ")

    def show(self):
        print(f"Ave: {self.name}, {self.age} años, especie {self.species}")

    def migrate(self):
        destino = input(f"¿Hacia dónde migra {self.name}? ")
        print(f"{self.name} está migrando a {destino}.")


if __name__ == "__main__":
    ave = Bird()
    ave.show()
    ave.migrate()

