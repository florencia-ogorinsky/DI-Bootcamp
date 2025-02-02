#Exercise 1:Hello World 
print("Hello World "*4)

#Exercise 2: Some Math 
print(99**3*8)

#Exercise 3: What is the output
# False 
# True
# False
# Error 
# False 

#Exercise 4: Your Computer Brand
computer_brand= "Lenovo"
print(f"I have a {computer_brand} computer")

#Exercise 5: Your information
name= "Florencia"
age=29
shoe_size= 40
info=f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}"
print(info)

#Exercise 6: A & B
a=10
b=8
if a>b:
    print("Hello World")

#Exercise 7 : Odd or Even
if int(input("Please provide a number"))%2==0:
    print("the number is even")
else:
    print("the number is odd")

#Exercise 8:
user_name=input("Provide your name")
if user_name.lower()=="florencia":
    print("This is fun we have the same name!")
else:
    print("Oh we dont have the same name :( ")

# Exercise 9 : Tall enough to ride a roller coaster
height=float(input("Insert your height in centimiters"))
if height>145:
    print("You are tall enough to ride")
else: 
    print("You need to grow more so you can ride")
