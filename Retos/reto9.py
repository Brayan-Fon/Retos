from reto2 import Dog
from reto3 import Cat, Bird

class Veterinarian:
    def examine(self, animal):
        print(f"El veterinario examina a {animal.name}, que es un {animal.__class__.__name__}.")


if __name__ == "__main__":
    perro = Dog()
    perro.bring()

    gato = Cat()
    gato.info()

    pajaro = Bird()
    pajaro.info()

    vet = Veterinarian()
    vet.examine(perro)
    vet.examine(gato)
    vet.examine(pajaro)
