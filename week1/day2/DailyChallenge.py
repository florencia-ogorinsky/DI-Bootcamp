# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]



# number=int(input("provide number "))
# length=int(input("provide length "))

# i=0
# x=0
# list_of_num=[]


# while i<length:
#     i+=1
#     x+=1
#     list_of_num.append(number*x)
    
# print(list_of_num)



# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).


word=input("Provide a string")
result=word[0]
new_string=""

for i in range(len(word)):
    if result[-1]!=word[i]:
        result+=word[i]
print(result)

