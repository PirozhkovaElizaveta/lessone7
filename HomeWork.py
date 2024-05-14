class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
    def make_sound(self):
        print(f"{self.name} чирикает")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color
    def make_sound(self):
        print(f"{self.name} мычит")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type
    def make_sound(self):
        print(f"{self.name} шипит")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

Попугай = Bird(name="Попугай", age=2, wing_span=25)
Корова = Mammal(name="Корова", age=5, fur_color="Golden")
Змея = Reptile(name="Змея", age=3, scale_type="Smooth")

animals = [Попугай, Корова, Змея]
animal_sound(animals)