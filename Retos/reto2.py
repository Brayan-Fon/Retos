class Dog:
    def __init__(self):
        self.name = input("Nombre de tu perro: ")
        self.item = input(f"¿Qué objeto quieres que {self.name} busque? ")

    def bring(self):
        print(f"{self.name} corre y trae el/la {self.item}.")

if __name__ == "__main__":
    perro = Dog()
    perro.bring()
