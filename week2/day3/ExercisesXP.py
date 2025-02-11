# 🌟 Exercise 1: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):                   #str(c1)
        return f'{self.amount} {self.currency}s'
    
    def __int__(self):           #int(c1)
        return int(self.amount)
    
    def __repr__(self):                 #as str 
        return f'{self.amount} {self.currency}s'
    
    def __add__(self,num, currency=None):   #I call the function with the sign +   c1+5
        if isinstance(num,int) or isinstance(num,float):
            print(self.amount+num)
        elif isinstance(num, Currency):
            if num.currency==self.currency:
                print(num.amount+self.amount)
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {num.currency}")
            
    def __iadd__(self,num):         # += that modified c1
        if isinstance(num,int) or isinstance(num,float):
            self.amount+=num
            
        elif isinstance(num, Currency):
            if num.currency==self.currency:
                self.amount+=num.amount   #esta modificando self amount por eso va antes
                
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {num.currency}")
            
        else:        
            raise TypeError("Invalid type")

        return self                    #returns c1, not the amount of c1 


            
               
          

c1=Currency('dollar',5)
c2=Currency('dollar',10)
c3=Currency('shekel',1)
c4=Currency('shekel',10)

print(c1)
print(c2)
print(c3)
print(c4)

c1+=c2   #c1 will have the value of c2


print(str(c2))
print(int(c2))

c1+=c2  #c1 quedo en 10 pq adquirio el amount de c2



# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn




#SEND HERE LINK TO GITHUB FUNC AND EXERCISE_ONE



# 🌟 Exercise 3: String module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module




