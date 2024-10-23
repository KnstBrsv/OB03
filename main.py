from zoo import Zoo

# Функция для звуков животных
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Функция для еды животных
def animal_eat(animals):
    for animal in animals:
        animal.eat()

# Функция для плавания животных
def animal_swim(animals):
    for animal in animals:
        animal.swim()

# Функция для полёта животных
def animal_fly(animals):
    for animal in animals:
        animal.fly()

# Создаем зоопарк
zoo = Zoo("Большой Зоопарк", "Главная улица, 1")

# Нанимаем сотрудников
zoo.hire_zookeeper("Иван", 35)
zoo.hire_zookeeper("Ольга", 30)
zoo.hire_veterinarian("Анна", 29)

# Увольняем одного сотрудника (удаляем по имени)
employee_to_remove = zoo.employees[1]  # Ольга
zoo.employees.remove(employee_to_remove)
print(f"Сотрудник {employee_to_remove.name} уволен.")

# Добавляем животных
zoo.add_bird("Попугай", 2, "зеленый", can_fly=True, can_swim=False, sound="чирикает", food="семена")
zoo.add_mammal("Лев", 5, "желтый", can_swim=False, sound="рычит", food="мясо")
zoo.add_reptile("Крокодил", 7, "зеленый", can_swim=True, sound="шипит", food="рыбу")
zoo.add_bird("Орёл", 4, "коричневый", can_fly=True, can_swim=False, sound="каркает", food="мясо")

# Удаляем одно животное (по имени)
zoo.remove_animal("Орёл")

# Животные издают звуки
animal_sound(zoo.animals)

# Животные едят
animal_eat(zoo.animals)

# Животные плавают
animal_swim(zoo.animals)

# Животные летают
animal_fly(zoo.animals)

# Смотритель кормит всех животных
zookeeper = zoo.employees[0]  # Иван - смотритель
for animal in zoo.animals:
    zookeeper.feed_animal(animal)

# Ветеринар лечит всех животных
veterinarian = zoo.employees[1]  # Анна - ветеринар
for animal in zoo.animals:
    veterinarian.treat_animal(animal)

