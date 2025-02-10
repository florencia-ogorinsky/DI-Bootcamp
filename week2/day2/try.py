# def string_multiplier(thing, num):
#     try: #if error here goes to except
#         print(thing+num)
#     except:
#         print(thing+num)
#     finally:
#         print("all done")


# string_multiplier('asjhddg',7)
# string_multiplier(9,7)



def string_multiplier(thing, num):
    try:
        print(thing + num) 
    except TypeError:
        print(f"Cannot concatenate {type(thing).__name__} and {type(num).__name__}")
    finally:
        print("all done")

string_multiplier('asjhddg', 7)  
string_multiplier(9, 7)  


#if i used type(name) result will be <class str> but i want that it will be "str" thats why i use type(variable).__name__


