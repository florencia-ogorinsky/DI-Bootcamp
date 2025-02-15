
import random
import time 

class AnagramChecker:
    def __init__(self):
        with open("C:/Users/flore/OneDrive/Escritorio/DI-Bootcamp/week2/day5/sowpods.txt", 'r') as f: #read
            list1=f.readlines()
            list2=[]
            for x in list1:
                list2.append(x.strip('\n'))

            self.anagram= list2

    def is_valid_word(self):
        self.word= input("Write a word ").strip()
        if self.word.isalpha() and len(self.word.split()) == 1:
            if self.word.upper() in self.anagram:
                print('this is valid')
                self.get_anagrams()
                return lista   
        else:
            print("this is not a valid word ")
            self.is_valid_word()
    def get_anagrams(self):   
        list_of_strin_elem=list(self.word)
        random.shuffle(list_of_strin_elem)
     


        self.factorial=1
        def fact():
            for x in range(1,len(self.word)+1):
                self.factorial*=x
            return self.factorial
            
        random.seed(time.time())

        self.list3=[]
        for i in range(fact()):
            random.shuffle(list_of_strin_elem) 
            new_string=('').join(list_of_strin_elem)
            self.list3.append(new_string)
        self.list3=set(self.list3)
        
        global lista 
        lista=[]
        for x in self.list3:
            if x.upper() in self.anagram:
                lista.append(x)
            lista





#TO TEST:

# pep=AnagramChecker()

# pep.is_valid_word()

