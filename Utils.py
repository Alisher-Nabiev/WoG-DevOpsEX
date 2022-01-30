# import only system from os
from os import system, name

SCORES_FILE_NAME = str("Scores.txt")

BAD_RETURN_CODE = "500"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
