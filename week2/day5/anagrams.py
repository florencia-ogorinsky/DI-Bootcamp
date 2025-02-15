from anagram_checker import AnagramChecker

pep = AnagramChecker()

def start():
    while True:
        print("This is a website showing you the possible words with the same letters as your word.")
        user = input("If you would like to play write 'yes'. If you would like to exit type 'exit': ").lower()

        if user == 'yes':
                anagrams = pep.is_valid_word()
                if anagrams:
                    print("Anagrams found:", anagrams)
                    break
                else:
                    print("There are no anagrams for that word")
        elif user == 'exit':
            print("Exiting")
            break

        else:
            print("Please enter a valid single word")

start()


# pep=AnagramChecker()

# print(pep.is_valid_word())



