class Monkey:
    def __init__(self, name):
        self.name = name

    def eat(self, banana):
        print(self.name, 'a mangé une banane', banana.color)


class Banana:
    def __init__(self, color):
        self.color = color


banana_green = Banana('verte')
banana_yellow = Banana('jaune')
pierre = Monkey("Pierre")
marie = Monkey("bob")

pierre.eat(banana_yellow)
marie.eat(banana_green)