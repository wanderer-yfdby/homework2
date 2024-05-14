print("Тестовая проверка объединения веток")

print("Информация из главного файла")

class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f"{self.name} летает")
    def eat(self):
        print(f"{self.name} кушает")
    def sing(self):
        print(f"{self.name} поет - чирик")
    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food
    def sing(self):
        print(f"{self.name} поет - курлык курлык")
    def walk(self):
        print(f"{self.name} гуляет")

bird1 = Pigeon("Гоша", "курлык", "серый", "хлебные крошки")
bird2 = Bird("Маша", "чирик чикчик", "коричневый")
bird1.info()
bird1.sing()
bird1.info()
bird1.walk()
bird2.info()
bird2.sing()
