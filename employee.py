class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Сотрудник {self.name}, {self.age} лет, должность - {self.position}"


class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, "смотритель зоопарка")

    def feed_animal(self, animal):
        print(f"Смотритель {self.name} кормит животное {animal.name}.")
        animal.eat()


class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, "ветеринар")

    def treat_animal(self, animal):
        print(f"Ветеринар {self.name} лечит животное {animal.name}.")
        animal.make_sound()
