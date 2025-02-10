import random

# # 🌟 Exercise 1 : Pets
# # Instructions
# # Using this code:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds,walk): 
#         super().__init__(type, walk)  
#         return f'{sounds}'

    
# # Create another cat breed named Siamese which inherits from the Cat class.
# # Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.

# cat1= Siamese("Michi", 3)
# cat2= Chartreux("Pepa", 5)
# cat3= Bengal("Beni", 7)

# all_cats=[cat1,cat2,cat3]

# # print(cat1.walk())
# # Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, 
# # and pass the variable all_cats to the new instance.
# # Take all the cats for a walk, use the walk method.

# sara_pets=Pets(all_cats)

# sara_pets.walk()


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. 
# This method returns a string stating which dog won the fight. The winner should be the dog with 
# the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog:
    list=[]
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        Dog.list.append(self) #It will be list with all instances of the class. Useful for def fight
      
        
    def bark(self):
        print(f'{self.name} is barking')


    def run_speed(self):
        return self.weight/self.age*10


    def fight(self, other_dog):
        dog_dictionary = {x.name: x.run_speed() * x.weight for x in Dog.list}
        maxim=max(dog_dictionary.values())
        for k,v in dog_dictionary.items():
            if v== max(dog_dictionary.values()):
                print(k)
        
               



other_dog=Dog('Pepi',10,15)

laris=Dog('Lara', 8,6)
Leucs=Dog("Leuco", 11, 16)
Fler=Dog("Flore", 5, 17)
pips=Dog("Pipino", 2, 80)



# laris.fight(other_dog)
# Fler.fight(other_dog)

# print(Leucs.run_speed())  #14
# print(laris.run_speed())  #7.5
# print(Fler.run_speed())  #34


# print(other_dog.run_speed()) #15

# Leucs.fight(other_dog)



# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


## We didnt see how to proceed with an imported file in the class. So starting from second point:


class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):  
        super().__init__(name,age,weight)   
        self.trained=trained
        
    def train(self):
        self.bark()
        self.trained=True

    def play(self, *dog_names):
        dog_list=[]
        for x in dog_names:
            dog_list.append(x.name)
        print(f"{', '.join(dog_list)} play together")
        #if dog_names.trained==True:
        #    print(random.choice([
             

Pepinky=PetDog("Leo", 12, 15)

print(Pepinky.trained)
Pepinky.train()
print(Pepinky.trained)


dog1=PetDog("leia",5,6)
cat1=PetDog("franca",9,5)
turtle1=PetDog('enrica',7,10)



dog_names=dog1,cat1,turtle1

Pepinky.play(dog1,cat1,turtle1)

##Couldnt do random with a list 


# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]


class Family:
    def __init__(self, members:list, last_name:str):
        self.members=members
        self.last_name=last_name
        
    def born(self,**child):
        self.members.append(child)
        print(f"congratulations and welcome to {child['name']} to the family!")

    def family_presentation(self):
        print(self.members, self.last_name)

    def is_18(self, name):
        for dictionaries in self.members:
            if dictionaries['name']==name and dictionaries['age']>=18:
                print(True)
                return
            else:
                print(False)
                return
                

        


family1 = Family(
        [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ], 
    "Ogo"
)

family1.born(name='Michael', age=0, gender='Male', is_child=True)

family1.family_presentation()

family1.is_18('Michael')


# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]


# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.


class TheIncredibles(Family):
    def __init__(self, members:list, last_name:str , power=None, incredible_name=None):  
        super().__init__(members, last_name)
        self.power=power
        self.incredible_name=incredible_name


    def use_power(self,name):
        for dictionaries in self.members:

            if dictionaries['name']==name and dictionaries['age']>=18:
                print(dictionaries['power'])
                return
            elif dictionaries['name']==name and dictionaries['age']<18:
                print("This member doesnt have powers")
                return
            else:
                raise Exception('this member is not in the list of members')
            
    def incredible_presentation(self):
        print("This is our amazing and powerful family")
        self.family_presentation()


            



family2=TheIncredibles(    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ], 'Ogorin')

family2.use_power('Michael')

family2.incredible_presentation()



family2.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknow power', incredible_name='Incredible Jack')

family2.incredible_presentation()

