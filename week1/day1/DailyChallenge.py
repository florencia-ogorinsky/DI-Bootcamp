# #1 
# sentence=input("Write a sentence of 10 characteres ")
# if len(sentence)<10:
#     print("string is not long enough ")
# elif len(sentence)>10:
#     print("String too long ")
# else:
#     print("great job the string is perfect length ")

# #2
# print(sentence[0])
# print(sentence[-1])

#3
sentence=input("Write a sentence of 10 characteres ")

new_string = ""

for x in sentence:
    new_string += x
    print(new_string)



