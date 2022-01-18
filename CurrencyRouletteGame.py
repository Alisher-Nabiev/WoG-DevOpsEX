from currency_converter import CurrencyConverter


def crg_game(crg_dif):
    c = CurrencyConverter()
#   print(c.convert(10, 'ILS', 'USD'))
    current_con = float(c.convert(10, 'ILS', 'USD'))

    while 0 < crg_dif <= 5:
        user_inp = float(input("\nplease enter your number: "))
        print(user_inp)
        if (current_con - (5 - crg_dif)) < user_inp < (current_con + (5 - crg_dif)):
            print("you win!")
        else:
            print("you loss!")
