
from currency_converter import CurrencyConverter



def crg_game(crg_dif):
    c = CurrencyConverter()
    print(c.convert(10, 'ILS', 'USD'))

    current_con = int(c.convert(10, 'ILS', 'USD'))

    if crg_dif == 1:
        user_inp = int(input("\nplease enter your number: "))
        if (current_con - (5 - 1) ) and (current_con + (5 -1)) == user_inp:
            print("you win!")
        else:
            print("you loss!")



crg_game(1)

