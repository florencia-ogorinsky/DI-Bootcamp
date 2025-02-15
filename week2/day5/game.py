import random 

global list_results
list_results=[]

class Game:
    def __init__(self):
        pass
    def get_user_item(self):
        global user_item
        user_item=input('select an item, rock "r", paper "p" or scissors "s" . If you want to exit write "exit" ').lower()
        if user_item=='exit':
            exit()
        elif user_item!="r" and user_item!="p" and user_item!="s":
            print(False, "Invalid data inserted. Try again with 'r', 'p' or 's' ")
            self.get_user_item()
        else:
            return user_item
        
    def get_computer_item(self):
        global computer_item
        computer_item=random.choice(['r','p','s'])
        return computer_item
    
    def get_game_result(self, user_item, computer_item):
        global result
        if user_item=='r' and computer_item=='r' or user_item=='p' and computer_item=='p' or user_item=='s' and computer_item=='s':
            result= 'draw'
            list_results.append(result)
        elif user_item=='r' and computer_item=='p' or user_item=='p' and computer_item=='s' or user_item=='s' and computer_item=='r':
            result= 'loss'
            list_results.append(result)
        else:
            result='win'
            list_results.append(result)
        return result
    
    def list_results(self):
        return list_results


    def play(self):
        while True:
            self.get_user_item()
            print(f"Your choice is: {user_item}")

            self.get_computer_item()
            print(f"The computer choice is: {computer_item}")

            self.get_game_result(user_item,computer_item)
            if result=='draw':
                print(f'is a {result}! ')
                break
            elif result=='win':
                print('Congratulations!!! You won! 🏆')
                break
            else:
                print('''You lost 😕
Keep trying!''')
                break

      

