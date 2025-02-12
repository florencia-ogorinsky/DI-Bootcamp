# Text Analysis

#Part 1
import string

class Text:
    textt= "A good book would sometimes cost as much as a good house."

    def __init__(self, textt:str):
        self.textt=textt
        self.dict=dict
        list=self.textt.split(' ')
        x=0
        self.dict={}
        list2=[]
        for words in list:
            list2.append(words)
            list2.count(words)
            self.dict[words]=list2.count(words)
            x+=1

            
        print(self.dict)

    def frequency_word(self):

        given_word= input('Write a word and i will tell you if it is in the text ')
        for k,v in self.dict.items():
            if given_word.lower() in self.dict.keys():
                print(f'the word {given_word} is present in the text {self.dict[given_word]} times')
                break
            else:
                print(None)
                break

    def unique_word(self):
        unique_words=[]
        for k,v in self.dict.items():
            if v==1:
                unique_words.append(k)
        print(f'the list of unique words is: {unique_words}')   

    def most_common_word(self):
        list2=[]
        for k,v in self.dict.items():
            list2.append(v)
            if v==max(list2):
                print(k)




textt=Text("A good book would sometimes cost as much as a good house.")
textt.frequency_word()
textt.unique_word()
textt.most_common_word()

   


# Part 2


# class Text:
#     def __init__(self, textt:str):
#         with open("C:/Users/flore/OneDrive/Escritorio/DI-Bootcamp/week2/day4/the_stranger.txt", "r") as file: #readfile
#             textt = file.read()  
#         self.dict=dict
#         list=textt.split(' ')
#         x=0
#         self.dict={}
#         list2=[]
#         for words in list:
#             list2.append(words)
#             list2.count(words)
#             self.dict[words]=list2.count(words)
#             x+=1

            
#         print(self.dict)

#     def frequency_word(self):

#         given_word= input('Write a word and i will tell you if it is in the text ')
#         for k,v in self.dict.items():
#             if given_word.lower() in self.dict.keys():
#                 print(f'the word {given_word} is present in the text {self.dict[given_word]} times')
#                 break
#             else:
#                 print(None)
#                 break

#     def unique_word(self):
#         unique_words=[]
#         for k,v in self.dict.items():
#             if v==1:
#                 unique_words.append(k)
#         print(f'the list of unique words is: {unique_words}')   

#     def most_common_word(self):
#         list2=[]
#         for k,v in self.dict.items():
#             list2.append(v)
#             if v==max(list2):
#                 print(k)


# with open("C:/Users/flore/OneDrive/Escritorio/DI-Bootcamp/week2/day4/the_stranger.txt", "r") as file: #readfile
#     textt = file.read()  

# textt=Text(textt)
# textt.frequency_word()
# textt.unique_word()
# textt.most_common_word()


    
