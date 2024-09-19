from tools import Animal

class Dog(Animal):
    def eat(self):
        super(Dog,self).eat()
        print("吃完骨头摇摇头...")

dog = Dog('旺财')
print(dog.eat())