# BASIC VALUE TYPES

#cd wee1    
#cd day1
#cd basic-values.py
#py   
#exit()
#clear


#check type:   print(type(5.35))

# print(type(5.35))


# discover the type of the following values:

# 5
# 2.54
# 'Good Morning'

# print(type(5))
# print(type(2.54))
# print(type("Good Morning"))

# print(type(False))
# print(False)
# print(False+6)
# print(type(5<7))
# print(5<7)
# print('5'==5)

#value types: Integers, Floats, Strings and Booleans 

#string= sequence of chars. So I can use indexing

# name= 'Juliana'
# # print(name)
# # print(name[3])
# # print(name[3:7])

# # #len() = discover the length of the string 
# # print(len('Harry Potter'))
# # print(name[4:len(name)])

# # print(name[4:])
# # print(name[:])
# print(name[-7:])

#create a vble called my_name asign to your name as a string 
# print middle letter
# print just the second letter
# print just the 3 or 2 letters of your name



# my_name="Florencia"
# middle=int((len(my_name))/2)
# print(my_name[middle])
# print(my_name[1])
# print(my_name[-2:])



# name= 'juliana'

# print(name.capitalize())

# print(name.title())
# name="JULIANA schmidt"

# print(name.lower())

# my_hp_name=name.replace('schmidt','Granger')

# print(my_hp_name)

# user_name= '    John Doe'
# cleaned_user_name= user_name.strip()
# print(cleaned_user_name)
# print(user_name)

# user_name='!John Doe'
# cleaned_user_name=user_name.strip('!')
# print(cleaned_user_name)

# price='$100'
# cleaned_price= price.strip('$')
# print(cleaned_price)


#Numbers
# print(4+3)
# print(4-2)
# print(4*2)
# print(4**2)
# print(4/2)
# print(5%2)

# score=0
# score+=1
# print(score)

# name= "Ju"
# name+="u"
# print(name)

#Type casting (changing data type)
# user_age=input('What is your age?')
# user_age=int(user_age)
# print(user_age+7)

# print(float(1))

#The input function gives a string by default 

# print('hello world \n' *4)

# print('Hello' + ' World')

# first_name= "Florencia"
# last_name= "Ogorinsky"
# print(first_name, last_name)

# print(f"Hello my name is {first_name} {last_name}")

#Naming a variable in python:

#Conditionals 
#if statement is flow control, 


#Take the name of the user using an input() and check if the name is the same as yours, and if so print "we have the same name!"

# my_name="Florencia"
# user_name=input("What is your name?")
# if user_name.lower()==my_name:
#     print("We have the same name!")
# elif user_name=="Daniel":
#     print("You have a beautiful name!")
# else:
#     print("Oh we dont have the same name")




# number=float(input("Provide me a number from 1 to 100 "))

# if number%3==0 and number%5==0:
#     print("FizzBuzz")
# elif number%3==0:
#     print("Fizz")
# elif number%5==0:
#     print("Buzz")


# #Exercise 1:Hello World 
# print("Hello World "*4)

# #Exercise 2: Some Math 
# print(99**3*8)

# #Exercise 3: What is the output
# False 
# True
# False
# #Error 
# False 

# #Exercise 4: Your Computer Brand
# computer_brand= "Lenovo"
# print(f"I have a {computer_brand} computer")

# #Exercise 5: Your information
# name= "Florencia"
# age=29
# shoe_size= 40
# info=f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}"
# print(info)

# #Exercise 6: A & B
# a=10
# b=8
# if a>b:
#     print("Hello World")

# #Exercise 7 : Odd or Even
# if int(input("Please provide a number"))%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# #Exercise 8:
# user_name=input("Provide your name")
# if user_name.lower()=="florencia":
#     print("This is fun we have the same name!")
# else:
#     print("Oh we dont have the same name :( ")

# # Exercise 9 : Tall enough to ride a roller coaster
# height=float(input("Insert your height in centimiters"))
# if height>145:
#     print("You are tall enough to ride")
# else: 
#     print("You need to grow more so you can ride")




# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x)






# sentence="Florencia como te va "
# string=""


# for x in sentence:
#     string+=x
#     print(string)






















# sentence="Hola bienvenido"
# string=""

# for x in sentence:
#     string+=x
#     print(string)

# exercise gold:
print(("Hello world\n"*4) +("I love python\n"*4), end="")
