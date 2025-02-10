class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}") 

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):    #the attribute is not private 
        self.__max_price = price
        print(self.__max_price)

c = Computer()

c.sell() # i can still access because sell is public 

print(c.name)
#print(c.__max_price) error 
c.sell()
c.set_max_price(5000)  
c.sell()



c.__max_price=6000
print(c.__max_price)
#but if i comment c.__max_price=6000 then the next one wont work
