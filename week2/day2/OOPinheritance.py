# Inheritance:

class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an {self.type}, and I love saying {self.sound}")


class Dog(Animal):  #is inheriting the attributes from animal
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")
    
    # def bark(self):
    #     print(f"{self.name} barked, WAF")

dingo=Dog('dog', 4 , 'Woof')

dingo.make_sound()


class Giraffe(Animal):
    def eat_leaf(self):
        print("I eat a leaf thats high in the tree")

joshua=Giraffe('Giraffe', 4, 'MREAWEEWWERE')

joshua.make_sound()

joshua.eat_leaf()

# dingo.eat_leaf() will get error. Dingo is not a giraffe.

dingo.fetch_ball()

blob_fish=Animal('fish', 0, 'blub blub')

blob_fish.make_sound()
# blob_fish.eat_leaf() will get error 
# blob_fish.fetch_ball() will get error 


# class Circle:
#     color="red"

# class NewCircle(Circle):
#     color="blue"

# nc= NewCircle
# print(nc.color)  #it will print blue 



class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)


nc = NewCircle(1)
print(nc.diameter)

nc.grow() # 1 * 2 * 2

print(nc.diameter) 
# >> What will be the output  4

