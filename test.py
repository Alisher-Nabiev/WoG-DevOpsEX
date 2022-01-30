# import call method from subprocess module
from subprocess import call

# import sleep to show output for some time period
from time import sleep
from os import system, name

# import sleep to show output for some time period

# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')


print('hello geeks\n' * 10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()