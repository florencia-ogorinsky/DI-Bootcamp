matrix_string='''7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!'''

# x=0
# v=x+0
# b=x+1
# f=x+2
# for x in matrix:
#     a=list(matrix[v]+matrix[b]+matrix[f])
#     print(a)


# Steps:
#1 to create a 2D list
#2 decrypt the matrix: for loop to check characters
#3 replace every group of symbols between two alpha characters by a space
#4 output a string with the message


matrix=[]
# for i in range(len(matrix_string)):
#     row= list(matrix_string[i:i+3])
#     print(row)
#     matrix.append(row)
# print(matrix)


rows= matrix_string.split('\n')
print(rows)

for row in rows:
    matrix.append(list(row))
print(matrix)

for column in matrix:
    column_0=[column[0] for column in matrix]
    column_1=[column[1] for column in matrix]
    column_2=[column[2] for column in matrix]
column_matrix=[]
column_matrix.append(column_0)
column_matrix.append(column_1)
column_matrix.append(column_2)
print(column_matrix)


output_string= ""
for col_list in column_matrix:
    # print(sub_list)
    for i in range(len(col_list)):
        # print(char)
        if col_list[i].isalpha():
            output_string+= col_list[i]
        else:
            if len(output_string)!= 0 and output_string[-1]!=' ':
                output_string+= ' '
print(output_string)

