# #For loop

# # for <variable> in <iterable/sequence>:
#       #indented block of code

# #Looping on a sequence(list):
# fruits= ['apple', 'banana', 'kiwi', 'pear']

# for each_fruit in fruits:
#     print(each_fruit)


# # #range(start, stop, step)
# # #Looping on a range of numbers:
# # for i in range(5):
# #     print(i)

# # for i in range(1,6):
# #     print(i)

# # for i in range(2,10,2):
# #     print(i)

# #enumerate()
# fruits= ['apple', 'banana', 'kiwi', 'pear']

# for i, each in enumerate(fruits):
#     if each==fruits[-1]:
#         print("this is the last one")
#     print(i,each)

# for i, each in enumerate(fruits):
#     if each=='kiwi':
#         fruits[i]='Lime'
#     else:
#         print(each)
# print(fruits)


# #Exercise:
# #accept a number from the user and print its multiplication table 

# a=int(input("Please provide a number"))

# for x in range(1,11):
#     print(a,"*",x,"=",a*x)

#While loops 
i= 0
while i < 5:
    print(1)
    i+=1


fruits= ['apple', 'banana', 'kiwi', 'pear']
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

#ctrl c to stop a infinite loop

pizzas_order= []
# max_pizza=5

# while len(pizzas_order)<max_pizza:
#     flavor= input('Which flavor? (If you finished type "done")')

#     if flavor=="done":
#         print('Successfuly added')
#         break
#     pizzas_order.append(flavor)


while True: #always use break in while true 
    flavor= input('Which flavor? (If you finished type "done")')

    if flavor=="done":
        print('Successfuly added')
        print(pizzas_order)
        print("we will deliver your pizza in 30 min")
        break
    pizzas_order.append(flavor)