from employee import ZooKeeper, Veterinarian
from bird import Bird
from mammal import Mammal
from reptile import Reptile


class Zoo:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        self.employees = []

    def hire_zookeeper(self, name, age):
        """Нанимаем смотрителя зоопарка."""
        zookeeper = ZooKeeper(name, age)
        self.employees.append(zookeeper)
        print(f"Сотрудник {zookeeper.name} принят на должность {zookeeper.position}.")

    def hire_veterinarian(self, name, age):
        """Нанимаем ветеринара."""
        veterinarian = Veterinarian(name, age)
        self.employees.append(veterinarian)
        print(f"Сотрудник {veterinarian.name} принят на должность {veterinarian.position}.")

    def add_bird(self, name, age, color, can_fly, can_swim, sound, food):
        """Добавляем птицу в зоопарк."""
        bird = Bird(name, age, color, can_fly, can_swim, sound, food)
        self.animals.append(bird)
        print(f"Животное {bird.name} добавлено в зоопарк.")

    def add_mammal(self, name, age, color, can_swim, sound, food):
        """Добавляем млекопитающее в зоопарк."""
        mammal = Mammal(name, age, color, can_swim, sound, food)
        self.animals.append(mammal)
        print(f"Животное {mammal.name} добавлено в зоопарк.")

    def add_reptile(self, name, age, color, can_swim, sound, food):
        """Добавляем рептилию в зоопарк."""
        reptile = Reptile(name, age, color, can_swim, sound, food)
        self.animals.append(reptile)
        print(f"Животное {reptile.name} добавлено в зоопарк.")

    def get_animal(self, name):
        """Ищем животное по имени."""
        for animal in self.animals:
            if animal.name == name:
                return animal

    def remove_animal(self, name):
        """Удаляем животное из зоопарка по имени."""
        animal = self.get_animal(name)
        if animal:
            self.animals.remove(animal)
            print(f"Животное {animal.name} удалено из зоопарка.")

