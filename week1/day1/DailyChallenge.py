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
current_character=sentence[0]
next_character=sentence[0+1]
string=""

for i in range(len(sentence)):
    sentence=input("Write a sentence of 10 characteres ")
    current_character=sentence[0]
    next_character=sentence[0+1]
    string=""

    print((current_character)+(next_character))


    


