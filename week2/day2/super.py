class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):  
        super().__init__(type, number_legs, sound)   #it sends back to to the Animal class
        # Or : Animal.__init__(self,type, number_legs, sound)
        self.fetch_ball = fetch_ball


# is a different way of writing:
# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         self.type = type  # Inicializas manualmente los atributos heredados
#         self.number_legs = number_legs
#         self.sound = sound
#         self.fetch_ball = fetch_ball


rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs , ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

print('Does this dog fetchs balls ? ', rex.fetch_ball)
# >> Does this dog fetchs balls ? True




# Exercise
# What is the difference between these 2 pieces of code ?

# class A(B):
#     def __init__(self, *args, **kwargs)
#         B.__init__(self, *args, **kwargs)
#         pass

# class A(B):
#     def __init__(self, *args, **kwargs)
#         super().__init__(*args, **kwargs)
#         pass


# Exercise on Inheritance and Composition: Door class
# Try to recreate the class explained below:

# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

# We can create a class called BlockedDoor that inherits from the base class Door.

# We just override the parent class's functions of open_door() and close_door() with our own 
# BlockedDoor version of those functions, 
# which simply raises an Error that a blocked door cannot be opened or closed.

class Door:
    def __init__(self, is_opened= True):
        self.is_opened= True


    def open_door(self):
        self.is_opened= True

    def close_door(self):
        self.is_opened= False


class BlockedDoor(Door):
    def __init__(self, is_opened= False):
        super().__init__(is_opened= False)
       

    def open_door(self):
        print("a blocked door cannot be opened")
        print(f"The door is open? {self.is_opened}")

    def close_door(self):
        print("a blocked door cannot be closed")
        print(f"the door is closed? {not self.is_opened}")

blocked= BlockedDoor()
blocked.open_door()
blocked.close_door()






 