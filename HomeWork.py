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

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} добавлен в зоопарк")

popugai = Bird(name="Попугай", age=2, wing_span=25)
korova = Mammal(name="Корова", age=5, fur_color="Golden")
zmeya = Reptile(name="Змея", age=3, scale_type="Smooth")

zoo = Zoo()
zoo.add_animal(popugai)
zoo.add_animal(korova)
zoo.add_animal(zmeya)

zoo_keeper = ZooKeeper(name="Иван")
veterinarian = Veterinarian(name="Анна")

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

zoo_keeper.feed_animal(popugai)
veterinarian.heal_animal(korova)