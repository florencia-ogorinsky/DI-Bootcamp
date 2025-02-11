#  @authenticator 




class MyClass:
  @staticmethod
  def add(a, b): 
    return a + b

print(MyClass.add(3, 6))
# >> 9


#we dont need to use the self


# class Man(Person):
#     sex = "Male"

#     @staticmethod
#     def get_nicknames():
#         return ["Bro", "Dude", "Buddy"]


#@classmethod:

class MyClass:
  __counter = 0  #private

  @classmethod
  def add(cls,a): 
    return cls.__counter + a

#first argument is class itself in the parenthesis

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))
# >> 3

# The output is still three because the method add refers to the class definition, not the counter of the new_class instance




#Property
#private attributes 
#i dont need the opening and closing parenthesis. Is like an attribute 

#i can have birth date. property age and then do current year - birth date and is being calc every single time 

class Person:
  def __init__(self, first_name, birth_year):
    self.first_name = first_name
    self.birth_year = birth_year

  @property
  def age(self):
    current_year = 2025
    return current_year - self.birth_year

me = Person('Aaron', 1995)

print(me.age)
