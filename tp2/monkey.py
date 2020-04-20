class Monkey:
    def __init__(self, name):
        self.name = name

    def eat(self, banana):
        print(self.name, 'a mangé une banane', banana.color)

    def sex(self, monkey):
        print(self.name, ' et ', monkey.name, 'ont copulé')
        robert = Monkey('robert')
        print(f'{robert} est né')
        return robert

class Banana:
    def __init__(self, color):
        self.color = color


banana_green = Banana('verte')
banana_yellow = Banana('jaune')
pierre = Monkey("pierre")
marie = Monkey("marie")
robert = Monkey("robert")

pierre.eat(banana_yellow)
marie.eat(banana_green)
robert.eat(banana_green)

robert = pierre.sex(marie)

robert.eat(banana_green)