# #  Exercise 1 – Random Sentence Generator

import requests
import os
import random
import sys


# Download:
site = 'https://norvig.com/ngrams/sowpods.txt'
request = requests.get(site)

print(request.status_code)  #if 200 it was download


def get_words_from_file():
   
    with open("C:/Users/flore/OneDrive/Escritorio/DI-Bootcamp/week2/day4/words.txt", "r") as file: #readfile
        words_list = file.readlines()  #createlist
    
    list=[]
    for x in words_list:
        list.append(x.strip())
    return(list)
   

get_words_from_file()


def get_random_sentence(length=5):
    list2=random.sample(get_words_from_file(),length)
    string=' '.join(list2)
    print(string.lower())

get_random_sentence()


def exit_program():
    print("Exiting the program...")
    sys.exit(0)


def main(): 
    print("This program makes a random sentence of the length you will chose ")
    length=int(input("How long you want the length of the sentence to be? between 2 and 20 "))
    if length in range(1,21):
        get_random_sentence(length)
    elif length<1 or length>20:
        raise ValueError("The number is not in the asked range")
        exit_program()

main()



#  Exercise 2: Working with JSON

import json

json_file = 'exercise2.json'
with open(json_file, 'r') as file_obj:
    sampleJson = json.load(file_obj)

print(sampleJson)

#access salary:
print((((sampleJson['company'])['employee'])['payable'])['salary'])

#add key:

(sampleJson['company'])['employee']['birth_date']="08/03/1995"

print(sampleJson)


with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj, indent = 4, sort_keys=True)


