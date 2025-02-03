#Exercise 1
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers={1,3,5,8,9,7}
# my_fav_numbers.update({45,54})
# print(my_fav_numbers)

# my_fav_numbers.pop()
# print(my_fav_numbers)

# friend_fav_numbers={3,1,579,45,354}
# our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#Exercise 2

# my_tuple=(1,6,8)
#Is not possible because tuples are immutable

#Exercise 3
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# fruits=["Banana", "Apples", "Oranges", "Blueberries"]
# fruits.remove("Banana")
# print(fruits)
# fruits.remove("Blueberries")
# print(fruits)
# fruits.insert(-1,"Kiwi")
# fruits.insert(1,"Apples")
# print(fruits)
# print(fruits.count("Apples"))
# fruits.clear()
# print(fruits)


# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

#A float is an object that represents a decimal number that we can use for math operations. 
# [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]


# list3=[]
# num = 1
# for x in range(8):
#     num+=0.5
#     if ".0" in str(num):
#         list3.append(int(num))
#     else:
#         list3.append(num)
# print(list3)

#another way to generate a sequence of floats:
#with for:
# for x in range(1,10):
#     x+=0.5
#     print(float(x))

#with while:
# x=0
# while x<10:
#     x+=0.5
#     print(x)

# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# for x in range(1,21):
#     print(x)



# my_list=[]
# for x in range(1,21):
#     my_list.append(x)
#     if my_list.index(x) %2 == 0:
#          print(x)


#  Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


# user_name=input("Write your name: ")
# while user_name.lower() !="florencia":
#     user_name=input("Write your name: ")
    


# Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.

# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# user_fav_fruit= input("Write your favorite/s fruit/s and separate them with a single space")

# list_of_fruits=(user_fav_fruit.split())

# any_fruit= input("Write any fruit")

# for x in list_of_fruits:
#     if any_fruit in list_of_fruits:
#         print("You chose one of your fav fruits, enjoy")
#         list_of_fruits=(user_fav_fruit.split())
    
       
#     else:
#         print("You chose a new fruit, I hope you enjoy")
#         list_of_fruits=(user_fav_fruit.split())
        
       
#     break



# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).




# top=input("enter a series of pizza toppings")
# amount=0

# while True:
#     print("This topping will be added to your pizza")
#     top=input("enter a series of pizza toppings")
#     amount+=1
    
    
#     if top=="quit":
#         print(top)
#         price= 10 + 2.5*amount
#         print(f"The amount you will pay is ${price}")
#         break

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


# age=input("Enter the age of each person attending and separate them with a space ")

# list_ages=list(map(int,age.split()))
# print(list_ages)

# price=0
# for x in list_ages:
#     if x<3:
#        price+=0
       
#     elif x>=3 and x<12:
#        price+=10
       
#     else:
#         price+=15
# print(f"the cost of your tickets is {price})")



# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list:




# age=input("Enter the age of each person attending and separate them with a space ")

# list_ages=list(age.split())
# print(list_ages)

# movie=input("Enter the number of the movie you will watch, If spiderman enter 1, if Action enter 2")


# for x in list_ages[:]:
#     if int(x)<21 and int(x)>16 and movie=="2":
#         list_ages.remove(x)

# print(list_ages)



# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

#sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# x="Pastrami sandwich"
# while x in sandwich_orders:
#     sandwich_orders.remove(x)
# print(sandwich_orders)


# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# finished_sandwiches= []

# i=0


# for x in sandwich_orders[:]:
#     finished_sandwiches.append(sandwich_orders.pop())
#     print(f"I made your {finished_sandwiches[-1]} sandwich")
# print(finished_sandwiches)









