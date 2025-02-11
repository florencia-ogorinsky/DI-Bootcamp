# Daily Challenge - Circle
# Last Updated: September 22nd, 2023

# What You will learn :
# OOP dunder methods


# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math

class Circle:
    empty_list=[]

    def __init__(self, name, radius):
        self.radius = radius
        self.name= name
        Circle.empty_list.append(self)
        


    def __str__(self):
        return f"This circle {self.name} has a radius of {self.radius}"
    

    def area(self):
        return math.pi*(self.radius**2)
    
    def __add__(self,circle2):
        return Circle(radius=self.radius + circle2.radius)
    
    def __gt__(self,circle2):
        return self.radius>circle2.radius  #if yes is true. if not false(boolean)
    
    def __eq__(self,circle2):
        return self.radius==circle2.radius
    
    def __lt__(self,circle2):
        return self.radius<circle2.radius
    

    


c1= Circle("circle_one",90)
c2= Circle("circle_two",8)


# print(c2)

print(c1<c2)


lista=[]
for x in Circle.empty_list:
    lista.append(x.name)
print(lista)

