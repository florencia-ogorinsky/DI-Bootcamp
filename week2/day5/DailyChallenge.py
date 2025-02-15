# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class? is the blueprint
# What is an instance? a copy of the class with actual values that belongs to the class
# What is encapsulation? restricting access to variables making them private __variable
# What is abstraction?
# What is inheritance? when a class gets the atributes of another class
# What is multiple inheritance? a class gets the atributes of more than one other class. 
# What is polymorphism? different or related classes that use the same names for their functions
# What is method resolution order or MRO? the functions last to be inherited can override functions from the parent class.



# deck of cards 

import random 
class Card:
    def __init__(self):        
        striing='Hearts, Diamonds, Clubs, Spades'
        suit=striing.split(', ')
        print(suit)

        valuestr='A,2,3,4,5,6,7,8,9,10,J,Q,K'
        value=valuestr.split(',')
        print(value)



class Deck:
    def __init__(self):
        list=[]
        for x in self.suit:
            for b in self.value:
                list.append((b,x))
        list

    def shuffle(self):
        random.shuffle(list)
        print(list)

    def deal(self):
        card= random.choice(list)
        list.remove(card)
    

    

