# Dictionaries:
# Data structure (more complex because it holds key:value pair). They are ordered from python 3.7
# Ordered and mutable 

user_info={'name':'Ron',
           'last_name':'Weasley',
           'age':17,
           'address': 'Ottery Village -England',
           'family': [('Arthur', 'Father', 50), ('Molly','Mother', 48)],
           'hobbies': {'Quidditch', 'Swimming'}
           }


#Accessing values:
print(user_info['name'])
print(user_info['family'][0]) #Only the first index of Family key (the first tupple)
print(type(user_info['family']))

user_info_2= {'name':'Harry',
           'last_name':'Potter',
           'age':17,
            }

user=[{'name':'Ron',
           'last_name':'Weasley',
           'age':17,
           'address': 'Ottery Village -England',
           'family': [('Arthur', 'Father', 50), ('Molly','Mother', 48)],
           'hobbies': {'Quidditch', 'Swimming'}
           },
           {'name':'Harry',
           'last_name':'Potter',
           'age':17,
            }
            ]

#Accessing values
print(user_info['name'])
print(user_info)


#Exercise:
#Access the value of key history

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict.keys())

a=(sample_dict['class'])

print(a)

print(sample_dict['class']['student']['marks']['history'])

# print(sample_dict[0]) Key Error not with index, but with key values

#Modify an entry:
user_info['age']=18
print(user_info)

#Adding a new entry:
user_info['School']='Hogwarts'
print(user_info)

#Deleting an entry:
del user_info['School']
print(user_info)

#Keys must be unique 


#The in Keyword

print('hobbies' in user_info) #it will give me true cause it is in the dictionary
print('birthday' in user_info)

if 'birthday' in user_info:
    print(user_info['birthday'])
else:
    print('this key doesnt exist')


for relative in user_info['family']:
    print(relative)




#Exercise:
student_info = {
    'name': 'John',
    'age': 25,
    'hobbies': ['reading', 'gaming', 'cycling'],
    'city': 'New York'
}

# Tasks:
# 1 - Change the value of 'age' from 25 to 30.
# 2 - Add a new entry with the key 'occupation' and the value 'Engineer'.
# 3 - Remove the entry with the key 'city'.
# 4 - check if the key 'email' is on the dictionary, if not, add it with value 'name@gmail.com'
# 5 -Loop through the values in the 'hobbies' list and print each hobby on a new line.

#1:
student_info['age']=30  

#2:
student_info['occupation']='Engineer'
print(student_info)

#3:
del student_info['city']
print(student_info)

#4:
while 'email' not in student_info:
    student_info['email']='name@gmail.com'
    break
print(student_info)


if 'email' not in student_info:
    student_info['email']='name@gmail.com'

#5:
for v in student_info['hobbies']:
    print(v)


student_info['hobbies'].append('soccer')
print(student_info)

# student_info['age']+=1
# print(student_info)

#Built-In Methods:
print(user_info.keys())
print(user_info.values())

for value in user_info.values():
    print(value)

print(user_info.items())


for key, value in user_info.items():
    if key=='age':
        user_info['age']+=5
    print(key,value)
print(user_info)

#Exercise
# Delete set of keys from Python Dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key_remove in keys_to_remove:
    if key_remove in sample_dict.keys():
        del sample_dict[key_remove]
print(sample_dict)


#update method:

car={"brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.update({"color": "white"})

car.update({"model": "Mazda",
            "another_Color": "red"})
print(car)

#ZIP= very useful in built-in method 
names=['Lea','Darth Vaider', 'Luke', 'Chuwbacca']
power=[150,500,489,100]

star_wars=dict(zip(names,power))
print(star_wars)



for char_name in names:
    if char_name=='Darth Vaider':
        continue
    print(char_name)


#Read list comprehension
