# Copy your Animal class here
class Animal(object):

    def __init__(self,name,favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood

    def sleep(self):
        print(self.name + " hibernates for 4 months")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)

class Bear(Animal):

    def __init__(self, name):
        self.name = name
        self.favoriteFood = "fish"


class Tiger(Animal):

    def __init__(self, name):
        self.name = name
        self.favoriteFood = "meat"

    def sleep(self):
        print(self.name + " sleeps for 8 hours")
# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):

    def __init__(self, name):
        self.name = name
        self.favoriteFood = "marshmallows"

    def sleep(self):
        print(self.name + " sleeps in a cloud")

# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):

    def __init__(self, name):
        self.name = name
        self.favoriteFood = "leaves"

    def sleep(self):
        print(self.name + " sleeps for 8 hours")


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    ...
