#def memory_game:
#def currency_roulette:
import random
from Live import load_game
def guess_game(gg_dif):

    if gg_dif == 1:
        secret_number = int(random.randint(1,20))
        user_gg_number = int(input("please enter number betwin 1-20: "))
        if secret_number == user_gg_number:
            print("\ncorrect you guess the number!!")
        elif user_gg_number < 1 or user_gg_number > 20:
            print("\nplease enter number bettwin 1-20: ", guess_game(1))
        else:
            print("\nincorrect maybe next time...")

    elif gg_dif == 2:
        secret_number = int(random.randint(1, 40))
        user_gg_number = int(input("please enter number betwin 1-40: "))
        if secret_number == user_gg_number:
            print("\ncorrect you guess the number!!")
        elif user_gg_number < 1 or user_gg_number > 40:
            print("\nplease enter number bettwin 1-40: ", guess_game(2))
        else:
            print("\nincorrect maybe next time...")

    elif gg_dif == 3:
        secret_number = int(random.randint(1, 60))
        user_gg_number = int(input("please enter number betwin 1-60: "))
        if secret_number == user_gg_number:
            print("\ncorrect you guess the number!!")
        elif user_gg_number < 1 or user_gg_number > 60:
            print("\nplease enter number bettwin 1-60: ", guess_game(3))
        else:
            print("\nincorrect maybe next time...")

    elif gg_dif == 4:
        secret_number = int(random.randint(1, 80))
        user_gg_number = int(input("please enter number betwin 1-80: "))
        if secret_number == user_gg_number:
            print("\ncorrect you guess the number!!")
        elif user_gg_number < 1 or user_gg_number > 80:
            print("\nplease enter number bettwin 1-80: ", guess_game(4))
        else:
            print("\nincorrect maybe next time...")

    elif gg_dif == 5:
        secret_number = int(random.randint(1, 100))
        user_gg_number = int(input("please enter number betwin 1-100: "))
        if secret_number == user_gg_number:
            print("\ncorrect you guess the number!!")
        elif user_gg_number < 1 or user_gg_number > 100:
            print("\nplease enter number bettwin 1-100: ", guess_game(5))
        else:
            print("\nincorrect maybe next time...")












