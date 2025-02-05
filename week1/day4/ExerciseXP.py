# Exercise 1 : What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly. -->


# def display_message():
#     print("I am learning python!")

# display_message()

# Exercise 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

# def favorite_book(title):
#     print(f"One of my favorites books is {title}")

# favorite_book("Manuelita")

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

# def describe_city(city:str,country:str):
#     print(city, "is in", country)

# describe_city('Cordoba','Argentina')


# #Country as default
# def describe_city(city:str, country:str='Brazil'):
#     print(city, "is in", country)

# describe_city('Rio de Janeiro')


# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

# import random


# def my_function():
#     user_number=int(input("Write a number between 1 and 100: "))
#     random_number=random.randint(1,100)
#     if user_number==random_number:
#         print("You succeed! the numbers are the same! Congratulations")
#     else:
#         print("Sorry, the numbers are not the same: ")
#         print("your number is:",user_number)
#         print("random number:",random_number)

# my_function()


#  Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

# size=input("Write your tshirt size: S , M , L , XL and press enter ")
# message= input("Write the message you want to see in your tshirt and press enter ")
# def make_shirt():
#     print(f"The size of the shirt is {size} and the text is {message}")

# make_shirt()

#With defaults:

# size=input("Write your tshirt size: S , M , L , XL and press enter ")
# message= input("Write the message you want to see in your tshirt and press enter ")

# def make_shirt(size='Large', message='I love Python'):
#     print(f"The size of the shirt is {size} and the text is {message}")

# make_shirt(size='S',message='Hey there Im a data analyst!')




# Exercise 6 : Magicians …
# Instructions
# Using the list of magician’s names

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians():
#     for x in magician_names:
#         print(x)

# show_magicians()



# def make_great(magician_names):
#     for x in range(len(magician_names)):
#         magician_names[x]=magician_names[x]+" The great"
#         if x==len(magician_names)-1:
#             print(magician_names)

# make_great(magician_names)
# show_magicians()


# Exercise 7 : Temperature Advice

# import random
# def get_random_temp():
#     global temp
#     temp=random.randint(-10,40)
#     return temp
    

# print(get_random_temp())
# print(type(get_random_temp()))


# def main():
#     value=get_random_temp()
#     print(f"the temperature is now {value} degrees Celsius")

# main()



# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# def main():
#     value=get_random_temp()
#     print(f"the temperature is now {value} degrees Celsius")
#     if value<0:
#         print('Brrr, that’s freezing! Wear some extra layers today')
#     elif value>=0 and value<16:
#         print('Quite chilly! Don’t forget your coat')
#     elif value>=16 and value<23:
#         print("you dont need a coat")
#     elif value >=23 and value<32:
#         print("you should put some sunscreen!😊")
#     else:
#         print('very hot!')

# main()



# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.

# import random
# def get_random_temp(season):
#     if season=='winter':
#         temp=round(random.uniform(-10,0),2)
#     elif season=='autumn' or season=='spring':
#         temp=round(random.uniform(0,20),2)
#     else:
#         temp=round(random.uniform(20,40),2)
#     return(temp)

# print(get_random_temp('summer'))
    

# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.

# season=input("Write the season:'summer','spring','autumn','winter' ")


# def main():
#     global season
#     value=get_random_temp(season)
#     print(f"the temperature is now {value} degrees Celsius")
#     if value<0:
#         return 'Brrr, that’s freezing! Wear some extra layers today'
#     elif value>=0 and value<16:
#         return 'Quite chilly! Don’t forget your coat'
#     elif value>=16 and value<23:
#         return "you dont need a coat"
#     elif value >=23 and value<32:
#         return "you should put some sunscreen!" 
#     else:
#         return 'very hot!'

# print(main())





# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

# a=[1,2,3]
# b=[4,5,6]
# c=[7,8,9]
# d=[10,11,12]


# month=int(input("Write the month in numbers (1 for January,etc) "))


# if month in a:
#     season="winter"

# if month in b:
#     season="spring"

# if month in c:
#     season="summer"

# if month in d:
#     season="autumn"


# import random
# def get_random_temp(season):
#     if season=='winter':
#         temp=random.uniform(-10,0)
#     elif season=='autumn' or season=='spring':
#         temp=random.uniform(0,20)
#     else:
#         temp=random.uniform(20,40)
#     return(temp)

# print(get_random_temp('summer'))




# Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

#Create a function that asks the questions to the user, and check his answers. 
# Track the number of correct, incorrect answers. Create a list of wrong_answers
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.

# (data[0])  =  {'question': "What is Baby Yoda's real name?", 'answer': 'Grogu'}
# If he had more then 3 wrong answers, ask him to play again.


wrong_answers=[]
good_answers=[]

for x in range(len(data)):
    user_answer=input((data[x]['question']))
    if data[x]['answer']!=user_answer:
        wrong_answers.append(user_answer)
        print("You are wrong! the correct answer is", data[x]['answer'])
        if len(wrong_answers)>3:
            print("you had more than 3 incorrect answers, lets play again!")
            break

            # for x in range(len(data)):
            #     user_answer=input((data[x]['question']))
            #     if data[x]['answer']!=user_answer:
            #         wrong_answers.append(user_answer)
            #         print("You are wrong! the correct answer is", data[x]['answer'])

            #     else:
            #         good_answers.append(user_answer)
            #     x+=1    
                
    else:
        good_answers.append(user_answer)
    x+=1

print('wrong answers:', wrong_answers)
print('correct answers:', good_answers)



# Create a function that informs the user of his number of correct/incorrect answers.

print("your amount of wrong answers is: ",len(wrong_answers))
print("your amount of correct answers is: ", len(good_answers))










