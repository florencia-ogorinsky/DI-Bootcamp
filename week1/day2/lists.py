my_name= "Jack"
hello= "Hello World"
my_age= 27

my_list= [my_name, hello, my_age]

#List syntax 
numbers= [1,2,3,47,9]
print(numbers)

#ordered data structure = we can use index 
print(numbers[3])

#mutable = I can change it 

numbers[3]= 55

print(numbers)

#list methods
students = ['Harry', 'Ron', 'Hermione']
students.append('Luna')
print(students)

students.insert(1,'Ginny')
print(students)

students.remove('Ron')
print(students)

students.append('Ginny')
print(students)

students.remove('Ginny')
print(students)


students.pop()
print(students)

students.pop(-1)
print(students)


#pop by default removes the last one. if not i need to specify the index 

#remove is with value
#pop is with index 
#insert: index, value 


#Exercise: Given this list
list1= [5,10,15,20,25,50,20]
#1 print index 3
#2 change 50 to 70
#3 delete number 20
#4 add a new number to the end of the list

#1
print(list1[3])

#2
print(list1.index(50))
list1[5]=70

#3
list1.remove(20)

#4
list1.append(9)

#check following methods alone:
#copy()
#extend()
#clear()
#sort()
#sorted()








