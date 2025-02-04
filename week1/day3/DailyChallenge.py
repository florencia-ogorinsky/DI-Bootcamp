# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# word=input("Write a word ")
# dicta=dict()
# lista=list(dicta)
# listb=list()

# a=0
# b=-1
# for x in word:
#     lista.append(x)
#     b+=1
#     listb.append(b)
#     print(lista[a],listb[a])
#     a+=1
# print(lista)
# print(listb)


# for x in lista:
#     g=lista.index(x)
#     print(x,g)


# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.



# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

# Examples


things={"bottle":"$8",
 "mousse":"$20",
 "screen":"$89",
 "dog":"$500",
 "bed":"$260",
 "apartment":"$546455"
}

print(things["bottle"].removeprefix("$"))
listf=list()

for x in things:
    listf.append(things[x].removeprefix("$"))
listg=list(things.keys())
things2=dict(zip(listg,listf))
print(things2)



list_with_int=[]
for v in things2.values():
    list_with_int.append((int(v)))
print(list_with_int)


new_dict=dict(zip(things2.keys(),list_with_int))
print(new_dict)

import random

budget=int(input("Write in numbers your budget with no dollar sign, just number "))

affordable_items = {}

for k, v in new_dict.items():
    if v < budget:
        affordable_items[k] = v

keys_within_budget = list(affordable_items.keys())
random.shuffle(keys_within_budget)

print(keys_within_budget)

