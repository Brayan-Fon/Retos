class Dog:
    name = input("Digite el nombre de su perro " ) 
    objeto = input("Que trae el perro?") 
    
    def fetch (self):
        print(f"{self.name}, trajo {self.objeto}")

name = Dog() 
name.fetch()
