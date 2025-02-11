# #Class Atributes

# class Dog():
#     dogs_king = "Bernie IV"

#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print(f"{self.name} barks ! WAF")

#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")

#     def rename(self, new_name):
#         self.name = new_name

# my_dog = Dog("Rex")
# my_dog.rename("Paul")
# print(my_dog.name)

# print(Dog.dogs_king)   #Belongs to the class more than the instance
# print(my_dog.dogs_king)







class Dog():
    number_of_dogs = 0
    dogs_king = "Bernie IV"

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        # Increment the number of dogs
        Dog.number_of_dogs += 1

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name


    @staticmethod
    def bark():
        print('woof')
#dont need self if i use staticmethod


# my_dog = Dog("Rex")
# my_dog2 = Dog("Bernie V")
# print(f"Curently, there are {Dog.number_of_dogs} dogs")


my_dog= Dog('Peanut')
your_dog= Dog('Dingo')

print(your_dog.number_of_dogs)
print(my_dog.number_of_dogs)

print(your_dog.dogs_king)

Dog.dogs_king= 'Henry V'


my_dog.bark()
Dog.bark()
your_dog.bark()

#With staticmethod





# Exercise
# Analyse the code below. What will be the outputs ?

# Explain the goal of the methods

class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)

