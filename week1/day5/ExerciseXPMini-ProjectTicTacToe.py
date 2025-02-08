import random

string_game = '''
            ***************************
            *    _____ _____ _____    *
            *   |__A__|__B__|__C__|   *
            *   |__D__|__E__|__F__|   *
            *   |__G__|__H__|__I__|   *
            *                         *
            ***************************
             '''

winning_combinations = [
    ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], 
    ['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I'],  
    ['A', 'E', 'I'], ['C', 'E', 'G']                   
]

def convert_board_to_matrix():
    rows = string_game.split('\n')
    matrix = []
    for row in rows:
        filter = [char for char in row if char.isalpha()]
        if filter:
            matrix.append(filter)
    return matrix

def check_result(player_choices, computer_choices):
    for combo in winning_combinations:
        if set(combo).issubset(player_choices):
            return "Congratulations, you won!"
        if set(combo).issubset(computer_choices):
            return "Sorry, the computer won!"
    
    return "Game continues"

def display_board():
    print(string_game)

player = input("Write a short username:  ")

def game_turns():
    global string_game
    available_positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    
    player_choices = []
    computer_choices = []
    
    while len(available_positions) > 0:
        print(f"Available positions: {', '.join(available_positions)}")  
        
        choice = input(f"Write a letter ({', '.join(available_positions)}) according to the place you want to play: ").upper()

        
        if choice not in available_positions:
            print("That spot is already taken or invalid. Try again.")
            continue

        
        string_game = string_game.replace(f'__{choice}__', '__❤️___')
        available_positions.remove(choice)
        player_choices.append(choice)
        print(f"{player} played: ❤️")
        display_board()

    
        if len(available_positions) == 0:
            break


        ran = random.choice(available_positions)
        string_game = string_game.replace(f'__{ran}__', '__😊_')
        available_positions.remove(ran)
        computer_choices.append(ran)
        print(f"Computer played: 😊")
        display_board()

    result = check_result(player_choices, computer_choices)
    print(result)


display_board()  
game_turns()    
