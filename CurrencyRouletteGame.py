from currency_converter import CurrencyConverter
import Score

def crg_game(crg_dif):
    c = CurrencyConverter()
    #   print(c.convert(10, 'ILS', 'USD'))
    current_con = float(c.convert(10, 'ILS', 'USD'))

    if 0 < crg_dif <= 5:
        user_inp = float(input("\nplease enter your number: "))
        print(user_inp)
        if (current_con - (5 - crg_dif)) < user_inp < (current_con + (5 - crg_dif)):
            print("you win!")
            Score.add_score(crg_dif)
        else:
            print("you loss!")
