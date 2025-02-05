#Functions 
#Syntax 

# def say_hello():
#     print('Hello there')


# say_hello()

#Doc strings: explain the functions 

# def say_hello():
#     '''prints a str 'Hello there!'''
#     print('Hello there')

# say_hello()

#Passing information (arguments, parameters)

def say_hello(username):
    print(f'Hello {username}')

say_hello('Harry')

#passing more arguments

def say_hello(username,language):
    if language=="HE":
        print(f'שלום {username}')
    elif language=='Ru':
        print(f'Private {username}')
    elif language=='PT':
        print(f'Oi, {username}')
    else:
        print(f'Hello, {username}')

say_hello('Harry', 'Ru')

#Positional and keyword arguments:

# def say_hello(username:str,language:str)-> None:
#     if language=="HE":
#         print(f'שלום {username}')
#     elif language=='Ru':
#         print(f'Private {username}')
#     elif language=='PT':
#         print(f'Oi, {username}')
#     else:
#         print(f'Hello, {username}')



say_hello('Ru','Harry') #positional 

#Keyword arguments:
say_hello(username= 'Luna', language= 'PT')

say_hello(language= 'PT',username= 'Luna')


#exercise 
#write function called calculate_total that takes 2 arguments 
#price:(a number). the price of a single item
#quantity (a number) the numner of items 
# print the total 

def calculate_total(price:float, quantity:float):
    print('total:',price*quantity)

calculate_total(2,5)


#Default values for arguments: 

# def say_hello(username:str,language:str = 'EN')-> None:
#     if language=="HE":
#         print(f'שלום {username}')
#     elif language=='Ru':
#         print(f'Private {username}')
#     elif language=='PT':
#         print(f'Oi, {username}')
#     elif language=='EN':
#         print(f'Hello, {username}')
#     else:
#         print(f'I dont know your language')

    
# say_hello('George')


# def calculate_total(price, quantity):
#     print(price*quantity)

print(type(calculate_total(5,12))) # this is still a NoneType and not a int 

def calculate_total(price, quantity):
    return(price*quantity)

print(type(calculate_total(5,12))) # this is int because of the return. But here besides calling the function we also need to print 


#return breaks the function and give you an output 

def fav_colors():
    fav_colors= ['blue', 'red', 'yellow']
    for color in fav_colors:
        print(f'I love {color}')

fav_colors()

def fav_colors():
    fav_colors= ['blue', 'red', 'yellow']
    for color in fav_colors:
        return(f'I love {color}')

fav_colors() # this will give me only blue cause return breaks the loop

def fav_colors():
    fav_colors= ['blue', 'red', 'yellow']
    for color in fav_colors:
        print(f'I love {color}')
    return f'Those are my fav colors'

print(fav_colors())


def get_country_info(country:str):
    if country=='Israel':
        official_name= 'State of Israel'
        capital= 'Jerusalem'
        population= 10000000
    elif country=='Brazil':
        official_name= 'Federative Republic of Brazil'
        capital= 'Brazilia'
        population= 216400000
    else:
        print('invalid country')
    
    return official_name, capital, population

print(get_country_info('Brazil'))

official_name,capital,population= get_country_info('Brazil')

print(f'''the official name of Brazil is {official_name}
      the capital is {capital} and the population is {population}''')   #if i dont do variables global python dont recognize


#Global and Local Scope:

# count_calculation = 100 #global scope 

# def calculation(a,b):
#     addition= a+b
#     substraction= a-b
#     count_calculation+=1
#     return addition, substraction

# print(calculation(8,5)) #i get an error because count_calculation is a global variable:

count_calculation = 100 #global scope 

def calculation(a,b):
    global count_calculation
    addition= a+b
    substraction= a-b
    count_calculation +=1
    return addition, substraction

print(calculation(8,5))
print(count_calculation)

#or:
count_calculation = 100 #global scope 

def calculation(a,b, count_calculation):
   # global count_calculation
    addition= a+b
    substraction= a-b
    count_calculation +=1
    return addition, substraction

print(calculation(8,5, count_calculation))
print(count_calculation)

# the count calc increasing not working. But we can use it for list like below:

clients= ['George', 'John', 'Lisa']

def welcome(clients: list):
    for client in clients:
        print(f'Welcome {client}')
        clients[0] = 'Dave'
    # client.append('Maria')  # it changes the original list

welcome(clients)

print(clients)

#Here I use the global vble in the parameter or argument so i can change the original list by index 







