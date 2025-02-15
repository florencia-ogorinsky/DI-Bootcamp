from game import Game

def get_user_menu_choice():
    global menu_choice
    if 'message_printed' not in globals():
        input('''Welcome to Rock Paper Scissors game! 
Press enter to start! ''')  
        global message_printed
        message_printed = True  
    
   
    menu_choice = int(input('''Press:
1 to play a new game 
2 for showing scores
3 for Quit '''))

def print_results():
    f = Game()  
    global results
    results={}
    results['loss']=f.list_results().count('loss')
    results['win']=f.list_results().count('win')
    results['draw']=f.list_results().count('draw')
    return results

def main():
    while True:
        get_user_menu_choice()  
        if menu_choice == 3:  
            break
        elif menu_choice == 1:  
            f = Game()
            f.play()  
        elif menu_choice == 2: 
            results = print_results()
            print(f"The result is: {results}")
        else:  
            print("Invalid choice. Please enter 1, 2, or 3.")
main()
