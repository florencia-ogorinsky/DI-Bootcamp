#Args: not defined quantity of arguments

def calculation(*nums):
    return sum(nums)

print(calculation(1,5,6,9,8))


#kwargs: ** key word arguments 

def get_user_info(**kwargs):
    print(kwargs)

get_user_info(name='John' , lastname= 'Doe' , age= 45, ocupation=' Engineer')


def check(greeting,*numbers,**person):
    print('Greetings:', greeting)
    # for num in numbers:
    #     print('num - ',num)
    print(numbers)
    print(person)
    # for key, value in person.items():
    #     print(key+':' , value)
    
