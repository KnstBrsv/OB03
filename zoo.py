from employee import Employee
from animal import Animal


class Zoo:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        self.employees = []

    def hire_employee(self, name, age, position):
        self.employees.append(Employee(name, age, position))
        print(f"Сотрудник {name} принят на должность {position}.")

    def add_animal(self, animal):
        self.animals.append(Animal(animal.name, animal.age, animal.color))
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def get_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
    def remove_animal(self, name):
        for animal in self.animals:
            if self.get_animal(name) == animal:
                self.animals.remove(animal)
                print(f"Животное {animal.name} удалено из зоопарка.")

