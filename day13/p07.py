class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    # override speak()
    def speak(self):
        return "Woof"


class Cat(Animal):
    # override speak()
    def speak(self):
        return "Meow"

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())
print(dog.speak())
print(cat.speak())
