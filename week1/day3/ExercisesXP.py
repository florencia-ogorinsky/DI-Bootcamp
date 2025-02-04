# # Exercise 1 : Convert lists into dictionaries
# # Instructions
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method

# # keys = ['Ten', 'Twenty', 'Thirty']
# # values = [10, 20, 30]



# # keys_and_values= zip(keys,values)
# # print(dict(keys_and_values))




# #  Exercise 2 : Cinemax #2
# # Instructions
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.

# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# # price=0
# # for x in family.values():
# #     if  x<3:
# #         price+=0
# #     elif x>=3 and x<12:
# #         price+=10
# #     else:
# #         price+=15
# # print(price)


# #How much does each family member have to pay ?:
# # Print out the family’s total cost for the movies.
# #Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# # price=0
# # for k,v in family.items():
# #     if v<3:
# #         print(k,f"the price is 0")
# #         price+=0
# #     elif v>=3 and v<12:
# #         print(k,f"the price is 10")
# #         price+=10
# #     else:
# #         print(k,f"the price is 15")
# #         price+=15

# # print(f"the total is {price}")





# # Exercise 3: Zara
# # Instructions
# # Here is some information about a brand.
# # name: Zara 
# # creation_date: 1975 
# # creator_name: Amancio Ortega Gaona 
# # type_of_clothes: men, women, children, home 
# # international_competitors: Gap, H&M, Benetton 
# # number_stores: 7000 
# # major_color: 
# #     France: blue, 
# #     Spain: red, 
# #     US: pink, green

# # Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

# brand={'name': 'Zara',
#         'creation_date': 1975,
#         'creator_name': 'Amancio Ortega Gaona',
#         'type_of_clothes': ['men', 'women', 'children', 'home'],
#         'international_competitors': ['Gap','H&M', 'Benetton'], 
#         'number_stores': 7000 ,
#         'major_color': 
#          {'France': 'blue', 
#          'Spain': 'red', 
#          'US': ['pink', 'green']}
#          }

# # Change the number of stores to 2.
# brand['number_stores']=2

# #4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are
# print(f"Zara's clients are", brand['type_of_clothes'][0], ",", brand['type_of_clothes'][1],"," ,brand['type_of_clothes'][2],"and", brand['type_of_clothes'][3])


# #5. Add a key called country_creation with a value of Spain.

# brand['country_creation']='Spain'
# print(brand)


# #6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# print('international_competitors' in brand.keys())


# print(type(brand['international_competitors']))
# if 'international_competitors' in brand.keys():
#     brand['international_competitors'].append('Desigual')
# print(brand)

# #Delete the information about the date of creation.

# del brand['creation_date']
# print(brand)

# #8. Print the last international competitor.
# print(brand['international_competitors'][-1])

# #9. Print the major clothes colors in the US.

# print((brand['major_color'])['US'])

# #10. Print the amount of key value pairs (ie. length of the dictionary).
# print(len(brand))

# #11 Print the keys of the dictionary.

# print(brand.keys())

# #12 Create another dictionary called more_on_zara with the following details:
# more_on_zara={'creation_date': 1975,
#             'number_stores': 10000
#             }

# # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# brand.update(more_on_zara)
# print(brand)

# #14. Print the value of the key number_stores. What just happened ?
# print(brand['number_stores'])
# #Because that key already existed in brand dictionary, the value is just updated with the new value
# #if the key didnt exist it would create the new key. 


# #Exercise 4 : Disney characters
# #Use this list :
#users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# #Analyse these results :
# #1/

# # >>> print(disney_users_A)
# # {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# # #2/

# # >>> print(disney_users_B)
# # {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# # #3/ 

# # >>> print(disney_users_C)
# # {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# #Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

users= ["Mickey","Minnie","Donald","Ariel","Pluto"]

# lista=list()
# for x in users:
#     lista.append([x, users.index(x)])   
# disney_users_a=dict(lista)
# print(disney_users_a)


#Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

# lista=list()
# for x in users:
#     lista.append([users.index(x),x])   
# disney_users_b=dict(lista)
# print(disney_users_b)

#Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.


# users_s = sorted(users)


# lista=list()
# for x in users_s:
#     lista.append([x,users_s.index(x)])   
# disney_users_c=dict(lista)
# print(disney_users_c)


# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.


# lista=list()
# for x in users:
#     if "i" in x:
#         lista.append([x, users.index(x)])   
# disney_users_a=dict(lista)
# print(disney_users_a)


# The characters, which names start with the letter “m” or “p”.






# lista=list()
# for x in users:
#     if ((users[b])[0])=="M" or ((users[b])[0])=="P":
#         lista.append([x, users.index(x)])   
# disney_users_a=dict(lista)
# print(disney_users_a)

users= ["Mickey","Minnie","Donald","Ariel","Pluto"]


lista=list()

x=0
for x in range(len(users)):
    if (users[x][0])=="M" or (users[x][0])=="P":
          lista.append([x,users[x]])
    pass
disney_users_new=dict(lista)
print(disney_users_new)


