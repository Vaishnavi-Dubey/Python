class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


Rodger = Dog()

# Accessing class attributes and method through objects
print(Rodger.attr1)
Rodger.fun()
