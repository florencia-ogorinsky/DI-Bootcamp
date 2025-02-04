# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

word=input("Write a word ")
dicta=dict()
lista=list(dicta)
listb=list()



a=0
b=0
for x in word:
    lista.append(x)
    listb.append(b)
    b+=1
print(lista)
print(listb)


new_dictt=dict(zip(listb,lista))


print(new_dictt)


list_values=list(new_dictt.values())
list_keys=list(new_dictt.keys())

print(list_values)
print(list_keys)



listNew=list(zip(list_values,list_keys))
print(listNew)






# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.



# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

# Examples


# things={"bottle":"$8",
#  "mousse":"$20",
#  "screen":"$89",
#  "dog":"$500",
#  "bed":"$260",
#  "apartment":"$546455"
# }

# print(things["bottle"].removeprefix("$"))
# listf=list()

# for x in things:
#     listf.append(things[x].removeprefix("$"))
# listg=list(things.keys())
# things2=dict(zip(listg,listf))
# print(things2)



# list_with_int=[]
# for v in things2.values():
#     list_with_int.append((int(v)))
# print(list_with_int)


# new_dict=dict(zip(things2.keys(),list_with_int))
# print(new_dict)

# import random

# budget=int(input("Write in numbers your budget with no dollar sign, just number "))

# affordable_items = {}

# for k, v in new_dict.items():
#     if v < budget:
#         affordable_items[k] = v

# keys_within_budget = list(affordable_items.keys())
# random.shuffle(keys_within_budget)

# print(keys_within_budget)

