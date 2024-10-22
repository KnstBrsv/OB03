from animal import Animal


class Bird(Animal):
    def __init__(self, name, age, color, can_fly, can_swim, sound, food):
        super().__init__(name, age, color)
        self.can_fly = can_fly
        self.can_swim = can_swim
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(f"{self.name} {self.sound}!")

    def eat(self):
        print(f"{self.name} клюет {self.food}.")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} летит!")
        else:
            print(f"{self.name} не умеет летать.")

    def swim(self):
        if self.can_swim:
            print(f"{self.name} плывет!")
        else:
            print(f"{self.name} не умеет плавать.")