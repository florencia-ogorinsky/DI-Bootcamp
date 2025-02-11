
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        

class Family:
    def __init__(self, last_name, *args):
        self.last_name= last_name
        self.member= []
        for person in args:
            self.member.append({"name": person.name, "age": person.age})


    def born(self, **kwargs):
        print("Congratulations on a new member of the family")
        self.member.append(kwargs)

    def is_18(self, name):
        for member in self.member:
            if member['name']== name:
                if int(member['age'])>= int(18):
                    print(True)
                else:
                    return False 

    def family_presentation(self):
        print(f"{self.last_name} family details")
        for member in self.member:
            for detail in member.keys():
                print(f"{detail}:{member[detail]}")


me= Person('Aaron',41)
my_fam= Family('Wolf', me)
my_fam.family_presentation()
my_fam.is_18('Aaron')



my_family= Family('Wolf')
my_family.born(name='Aaron', age=41, is_child=False)
my_family.family_presentation()
my_family.is_18('Aaron')
my_family.born(name='Bob',age=10, is_child= True)
my_family.is_18("Bob")




class Incredibles(Family):
    

