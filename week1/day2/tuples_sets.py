# #Tuples
# #immutable and ordered 

# numbers= (10,20,30,40,20,50,20)
# print(type(numbers))

# #numbers[1]= 25 #error. Not possible to change a tuple

# print(numbers[1])

# #methods 
# print(numbers.count(20))
# print(numbers.index(30))

# #Concatenate tuples 
# numbers2 = (2,3,5,7)
# mixed_tupples = numbers + numbers2
# print(mixed_tupples)

# #list can have only 1 element. Tuple is always more than 1 

# #Unpacking tuples:
# a,b,c,d= (5,10,15,20)  #if i write () then i mean is a tuple and i cant change the values
# print(a)
# print(b)
# print(c)
# print(d)

# name, age, email= 'Juliana', 27, 'ju@gmail.com' #this is not a tuple cause doesnt have ()
# print(name)

#unpack de tuple into 4 variables= 
a_tuple= (10,20,30,40)

a,b,c,d = a_tuple

print(b)



#Sets
#data structure. Sequence. NOT ORDERED. We cant access by index. When we add it can be added in any position. 
#THEY DONT ALLOW DUPLICATES
#Ex= list of teudat zeut that cant be repeated

my_set={1,4,8,9}
# my_set= set()

my_set.add(12)
my_set.add(55)
print(my_set)

# print(my_set[1]) type error because is not organized, we cant access by index

id_numbers=[123, 56, 75634, 235, 123, 5678, 567, 123]
unique_ids = set(id_numbers)
print(unique_ids)

names= {'Juliana', "Israel", 'Dina'}
countries= {'USA', 'Brazil', 'Israel'}
print(names.intersection(countries))


names_and_countries= names.union(countries)
print(names_and_countries)

print(names.difference(countries))
print(countries.difference(names))

names.clear()
print(names)


#Create a set of your 5 fav numbers.
#Add a new number to the set 
#find the common elements between the 2 sets (with set of prime numbers)
#removes all elements from the set 

set_fav_num= {1,2,8,16,26}
set_fav_num.add(77)
set_prime={2, 3, 5, 7, 11}
print(set_fav_num.intersection(set_prime))

set_fav_num.clear()
print(set_fav_num)





