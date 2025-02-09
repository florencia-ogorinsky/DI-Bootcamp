# Instructions : Old MacDonald’s Farm

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# Output
# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!

class Farm:
    def __init__(self,name):
        self.name=name
        print(f"{name}'s farm")
        self.dicta={}

        
        
    def add_animal(self,new_animal,quantity:int=1):
        if new_animal in self.dicta:
            self.dicta[new_animal]+=quantity
        else:
            self.dicta[new_animal]=quantity
        print(self.dicta)
        
        
    def get_info(self):
        for animal, quantity in self.dicta.items():
            string=(f"{animal} : {quantity}")
            print(string)
    
    def get_animal_types(self):
        list=[]
        for animal in self.dicta.keys():
            list.append(animal)
        return sorted(list)

    def get_short_info(self):
        animal_types = self.get_animal_types() #list with cow sheep goat

        if len(animal_types) > 0:
            animals_str = f"{self.name}'s farm has "
            
            animals_part = []
            for animal in animal_types[:-1]:
                if self.dicta[animal] > 1:
                    animals_part.append(f"{animal}s")
                else:
                    animals_part.append(animal)
            animals_str += ", ".join(animals_part)

            if len(animal_types) > 1:
                animals_str += " and " + (f"{animal_types[-1]}s" if self.dicta[animal_types[-1]] > 1 else animal_types[-1]) + "."
            else:
                animals_str += "."
                
            print(animals_str)



           

        
       
      

macdonald = Farm("McDonald")
# print(f"{macdonald.name}'s farm")

macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.get_short_info()



