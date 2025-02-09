#--------------------------------------------------------------------------------------

# class Dog():        #Class.Capitalized every initial letter from the name of the class
#     def __init__(self):   #looks like a func but we cant use it outside the class
#         print("You created a dog!!")
    

# bobby=Dog()
# bobby.color="green"

# print(bobby.color)

# class Dog():      #Class.Capitalized every initial letter from the name of the class. Class define an object
#     def __init__(self,name):   #looks like a func but we cant use it outside the class
#         print("You created a dog!!")
#         self.name= name
    

# bobby=Dog("Robert")
# bobby.color="green"

# print(bobby.color)
# print(bobby.name)

# #instance is the object itself 


class Dog:
    def __init__(self, name, color, breed, floppy_ears):   #class method
        print("a new dog has been initialized! ")
        self.name=name
        self.color= color
        self.breed= breed
        self.floppy_ears= floppy_ears
    # pass

    def __str__(self):
        return f"{self.name} is a {self.color},{self.breed}"
     
    def bark(self):
        return f"{self.name} goes WOOF!!!!"
    
    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def fetch(self,object):
        print(f"{self.name} fetched a {object}")

    def eat(self, food):
        print(f"{self.name} ate {food}")
    
    def sit(self):
        print("he sat down")

    def rename(self, new_name):
        self.name= new_name


peanut= Dog('peanut','brown','mutt',True) # create a real dog 

print(peanut.breed,peanut.color)
print(peanut.color)
print(peanut.floppy_ears)


print(peanut.bark())



#init is called automaticaly

print(peanut)  #str when i print the object instance it returns what i have in the str.


peanut.color= 'grey' #we updated the color. we can change the attributes

print(peanut)

dingo= Dog('dingo','white','cnaanni', False)

print(dingo)

dingo.fetch('ball')
dingo.sit()

peanut.eat('peanut butter')



# # Exercise
# # Analyse the code below. What will be the ouput ?
# # Explain the goal of the __init__() method
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)


print(peanut.name)
peanut.rename("peanut butter")
print(peanut.name)





