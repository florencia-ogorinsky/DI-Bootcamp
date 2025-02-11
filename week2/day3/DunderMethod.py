#__str__ method and __repr__ method: str takes presidence over repr

class Person:
    def __init__(self, name, last_name, age, hair_color):
        self.name=name 
        self.age= age
        self.hair_color=hair_color
        self.last_name = last_name

    def __str__(self):
        return self.name, self.last_name # if i use this i dont need to print(aaron.name) i can only print (aaron)

    def __str__(self):
        return f"{self.name} {self.last_name} is a {self.age} years old person with {self.hair_color} hair STR"
    
    def __repr__(self):
        return f"{self.name} is a {self.age} years old person with {self.hair_color} hair REPR"
    
    def get_info(self):
        print(self)
    

    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        print(f"{self.name} acts like a function")        #aaron()

    def __add__(self, other):
        return Person(self.name, other.last_name, other.age, other.hair_color)

        
    

    

aaron=Person('aaron','wolf', 61,'blue')

print(aaron) #for repr and str

aaron.get_info()

print(len(aaron))


aaron()  #for call


# for add:

the_rock= Person('dekh', 'Jonson', 25,'red')

the_rock()
aaron_rock= aaron + the_rock

print(aaron_rock)