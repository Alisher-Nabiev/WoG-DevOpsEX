# This is a start of the WoG project of Alisher Nabiev

# define function:
def welcome(name):
    print(f"\nHello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play")
    return name


def load_game():
    print(
        "\nPlease choose a game to play:\n      "
        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n      "
        "2. Guess Game - guess a number and see if you chose like the computer.\n      "
        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n"
          )
    game_number = int(input("Please chose your game by typing a number of the game: "))
    game_difficulty = 0

    if 3 >= game_number >= 1:
        game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        if 5 >= game_difficulty >= 1:
            game_dif_type = [game_number, game_difficulty]
            return game_dif_type
        else:
            print("\n\nThe game difficulty is incorrect please enter valid number\n")
            load_game()
    else:
        print("\n\nThe game number is incorrect please enter valid number\n")
        load_game()




