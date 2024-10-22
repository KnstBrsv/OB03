class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.can_fly = False
        self.can_swim = False

    def make_sound(self):
        print(f"{self.name} makes a sound")

    def eat(self):
        print(f"{self.name} is eating")

    def fly(self):
        if self.can_fly:
            print(f"Животное {self.name} летит!")
        else:
            print(f"Животное {self.name} не умеет летать.")

    def swim(self):
        if self.can_swim:
            print(f"Животное {self.name} плывет!")
        else:
            print(f"Животное {self.name} не умеет плавать.")