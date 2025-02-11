# 🌟 Exercise 1: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):                   #str(c1)
        return f'{self.amount} {self.currency}s'
    
    def __int__(self):           #int(c1)
        return int(self.amount)
    
    def __repr__(self):                 #as str 
        return f'{self.amount} {self.currency}s'
    
    def __add__(self,num, currency=None):   #I call the function with the sign +   c1+5
        if isinstance(num,int) or isinstance(num,float):
            print(self.amount+num)
        elif isinstance(num, Currency):
            if num.currency==self.currency:
                print(num.amount+self.amount)
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {num.currency}")
            
    def __iadd__(self,num):         # += that modified c1
        if isinstance(num,int) or isinstance(num,float):
            self.amount+=num
            
        elif isinstance(num, Currency):
            if num.currency==self.currency:
                self.amount+=num.amount   #esta modificando self amount por eso va antes
                
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {num.currency}")
            
        else:        
            raise TypeError("Invalid type")

        return self                    #returns c1, not the amount of c1 


            
               
          

c1=Currency('dollar',5)
c2=Currency('dollar',10)
c3=Currency('shekel',1)
c4=Currency('shekel',10)

print(c1)
print(c2)
print(c3)
print(c4)

c1+=c2   #c1 will have the value of c2


print(str(c2))
print(int(c2))

c1+=c2  #c1 quedo en 10 pq adquirio el amount de c2



# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn


#######THIS EXCERCISE IS HERE:  https://github.com/florencia-ogorinsky/DI-Bootcamp/blob/main/week2/day3/func.py  
#      https://github.com/florencia-ogorinsky/DI-Bootcamp/blob/main/week2/day3/exercise_one.py




# 🌟 Exercise 3: String module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module


import string
import random
list=[]
for a in string.ascii_letters:
    list.append(a)
list

string=random.choices(list,k=5)

str=''
for a in string:
    str+=a
print(str)


# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime
today=datetime.datetime.today()

print(today)




# Exercise 5 : Amount of time left until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

diff=today-datetime.datetime(2025,1,1)
print(diff)



# Exercise 6 : Birthday and minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.



# birthday=input("Write your birtday in format YYYYMMAA   ")


# year=(birthday[:4])
# month=(birthday[4:6])
# day=(birthday[6:8])


# if month[0]=='0':
#     month=month[-1]


# if day[0]=='0':
#     day=day[-1]


# month=int(month)
# year=int(year)
# day=int(day)

# birth2=datetime.date(year,month,day)
# today=datetime.date.today()

# diff2= today.year-birth2.year

# diff_days = (today - birth2).days
# diff3=  diff_days*24*60 

# print(f"You have lived {diff2} years or what is equal to {diff3} minutes!")


# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.


from faker import Faker 
fake= Faker()

list=[]

for x in range(1,7):
    name=fake.name()
    address=fake.address()
    language_code=fake.language_code()
    list.append({'name':name,'address':address,'language_code':language_code})
print(list)

