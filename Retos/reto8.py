class Dog:
    def __init__(self):
        self.name = input("Nombre del perro: ")
        self.age = int(input(f"Edad de {self.name}: "))
        self.species = "Canino"

    def fetch(self):
        print(f"{self.name} trae la pelota con entusiasmo.")

    def compare(self, other):
        if self.age > other.age:
            print(f"{self.name} es mayor que {other.name}.")
        elif self.age < other.age:
            print(f"{other.name} es mayor que {self.name}.")
        else:
            print(f"{self.name} y {other.name} tienen la misma edad.")


if __name__ == "__main__":
    d1 = Dog()
    d2 = Dog()
    d1.compare(d2)
