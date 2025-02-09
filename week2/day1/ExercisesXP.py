# 🌟 Exercise 1: Cats
# Instructions
# Using this class
# cats=[]
# class Cat:

#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#         cats.append(self)
      
   

# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

# pepito=Cat('Leo',10)
# Michi=Cat('Michelle',5)
# Fri=Cat('Frida',7)

# print(pepito.name)
# print(Fri.age)

# pepito=Cat('Leo',10)
# Michi=Cat('Michelle',5)
# Fri=Cat('Frida',7)
# print(cats)


# def oldest(cats):
#     oldest_cat = cats[0]
#     for cat in cats:
#        if cat.age > oldest_cat.age:
#              oldest_cat = cat
#     print (f'the oldest cat {oldest_cat.name}')
# oldest(cats)


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# dogs_list=[]    #Outside the class


# class Dog:
    
#     def __init__(self,name,height):
#         self.name=name
#         self.height=height
#         dogs_list.append(self)    #inside the class. append with self


#     def bark(self, name):
#         print(f'{name} goes woof' )

#     def jump(self, name):
#         print(name,'jumps', self.height*2)

# davids_dog=Dog("Rex",50)

# print(f'The dogs name is {davids_dog.name} and his height is {davids_dog.height} cm')
# davids_dog.bark("Rex")
# davids_dog.jump("Rex")

# sarahs_dog=Dog("Teacup", 20)
# print(f'The dogs name is {sarahs_dog.name} and his height is {sarahs_dog.height} cm')

# sarahs_dog.bark("Teacup")
# sarahs_dog.jump("Teacup")



# def biggest_dog(dogs_list):
#     biggest_dog= dogs_list[0]
#     for dog in dogs_list:
#         if dog.height > biggest_dog.height:
#             biggest_dog=dog
#     print(biggest_dog.name)
# biggest_dog(dogs_list)



# 🌟 Exercise 3 : Who’s the song producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


# class Song:
#     def __init__(self,lyrics):
#         self.lyrics= lyrics 
#     def sing_me_song(self):
#         for elem in self.lyrics:
#             print(elem)

# perfect=Song(["Baby, I'm dancin' in the dark with you between my arms","Barefoot on the grass while listenin' to our favourite song"])


# perfect.sing_me_song()






# Exercise 4 : Afternoon at the Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     A: "Ape",
#     B: ["Baboon", "Bear"],
#     C: ['Cat', 'Cougar'],
#     E: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)





class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
        self.name=zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)
    

    def sell_animal(self,animal_sold):
        self.animals.remove(animal_sold)
        
    def sort_animals(self):
        self.animals.sort()
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        return sorted_animals


    def get_groups(self,sorted_animals):
        for k,v in sorted_animals.items():
            print('Animals with',k, ':',v)



        


zoo1= Zoo('La Chacra') # create a real giraffe 

zoo1.add_animal('elephant')  

# turtle=Zoo("La Chacra")
# zoo1.get_animals()
# zoo1.add_animal('giraffe')
# zoo1.add_animal('turtle')  
# zoo1.add_animal('tigre')  
# zoo1.add_animal('cat')  
# zoo1.add_animal('cile')  
# zoo1.add_animal('ciut')  
# zoo1.add_animal('couis')  
# zoo1.add_animal('cate')  
# zoo1.get_animals()
# zoo1.sort_animals()
# sorted_animals = zoo1.sort_animals()
# zoo1.get_groups(sorted_animals)

ramat_gan_safari=Zoo("Ramat Gan")
ramat_gan_safari.add_animal('elephant')  

turtle=Zoo("La Chacra")
ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal('giraffe')
ramat_gan_safari.add_animal('turtle')  
ramat_gan_safari.add_animal('tigre')  
ramat_gan_safari.add_animal('cat')  
ramat_gan_safari.add_animal('cile')  
ramat_gan_safari.add_animal('ciut')  
ramat_gan_safari.add_animal('couis')  
ramat_gan_safari.add_animal('cate')  
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
sorted_animals = ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups(sorted_animals)



