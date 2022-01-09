# This is a start of the WoG project of Alisher Nabiev
# main program:
from Live import load_game, welcome
import GuessGame
username = welcome(input("Hello user please enter your name here: "))

numbers = load_game()

print(numbers)

game_number = numbers[0]
game_diff = numbers[1]
if game_number == 2:
    GuessGame.guess_game(game_diff)
else:
    print("enterasd")


