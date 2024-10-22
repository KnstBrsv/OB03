from animal import Animal
from employee import ZooKeeper, Veterinarian
from reptile import Reptile
from mammal import Mammal
from bird import Bird
from zoo import Zoo

# animals = []
# animals.append(Mammal("Тигр", 5, "Белый", True, "рычит", "мясо"))
# animals.append(Bird("Утка", 2, "Серый", True, True, "крякает", "зерно"))
# animals.append(Reptile("Лягушка", 1, "Зеленый", True, "квакает", "комаров"))


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

def animal_eat(animals):
    for animal in animals:
        animal.eat()

def animal_swim(animals):
    for animal in animals:
        animal.swim()

def animal_fly(animals):
    for animal in animals:
        animal.fly()

# animal_sound(animals)
# animal_eat(animals)
# animal_swim(animals)
# animal_fly(animals)

# emp1 = ZooKeeper("Иван",  25)
# print(emp1)
# emp1.feed_animal(animals[0])
#
# emp2 = Veterinarian("Петр", 30)
# print(emp2)
# emp2.treat_animal(animals[1])

zoo1 = Zoo("Зоопарк", "Москва")
zoo1.hire_employee("Иван", 25, "смотритель зоопарка")
zoo1.hire_employee("Петр", 30, "ветеринар")
zoo1.add_animal(Mammal("Тигр", 5, "Белый", True, "рычит", "мясо"))
zoo1.add_animal(Bird("Утка", 2, "Серый", True, True, "крякает", "зерно"))
zoo1.add_animal(Reptile("Лягушка", 1, "Зеленый", True, "квакает", "комаров"))
zoo1.employees[0].feed_animal(zoo1.animals[0])
zoo1.employees[1].treat_animal(zoo1.animals[1])
zoo1.remove_animal("Лягушка")
zoo1.remove_animal("Утка")