class Persom:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ', self.name)
    pass

p = Persom('dsds')
p.__init__('ds')
print(p)
p.say_hi()