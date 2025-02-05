#Matrix:
#Array with another array inside

#Example:
# matrix=[
#     [1,2,3],
#     [2,4,6],
#     [7,8,9]
# ]


# print(matrix[0][1])


# #Daily Challenge Exercise:
matrix=[
['7','i','i'],
['T','s','x'],
['h','%','?'],
['i',' ','#'],
['s','M',' '],
['$','a',' '],
['#','t','%'],
['^','r','!']
]

# print(matrix[0][1])
new_list=[]
list_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x in list_char:
    new_list.append(x.upper())
print(new_list)

list6=new_list + list_char
print(list6)

empty_list=[]
for x in range(0,len(matrix)):
    if matrix[x][0] in list6:
        empty_list.append(matrix[x][0])
print(empty_list)



empty_list2=[]
for x in range(0,len(matrix)):
    if matrix[x][1] in list6:
        empty_list2.append(matrix[x][1])
print(empty_list2)



empty_list3=[]
for x in range(0,len(matrix)):
    if matrix[x][2] in list6:
        empty_list3.append(matrix[x][2])
print(empty_list3)


hide_message= empty_list+[" "]+empty_list2+empty_list3

print(hide_message)

empty_string=""
for x in hide_message:
    empty_string+=x
print(empty_string)

