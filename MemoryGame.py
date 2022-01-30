import time
import random
import Score

def memory_game(mg_dif):
    random_number = []
    user_list = []

    if mg_dif == 1:
        for i in range(0, 3):
            n = random.randint(1, 101)
            random_number.append(n)

        for x in random_number:
            time.sleep(0.70)
            print("\r {}".format(x), end="")
        time.sleep(0.70)
        print("\r0", end="")

        for i in range(0, 3):
            z = int(input("\rplease enter next number that you remember: "))
            user_list.append(z)

        if user_list == random_number:
            print('correct!')
            Score.add_score(mg_dif)
        else:
            print('incorrect!!!, try again.', time.sleep(0.70))
            memory_game(1)

    if mg_dif == 2:
        for i in range(0, 4):
            n = random.randint(1, 101)
            random_number.append(n)

        for x in random_number:
            time.sleep(0.70)
            print("\r {}".format(x), end="")
        time.sleep(0.70)
        print("\r0", end="")

        for i in range(0, 4):
            z = int(input("\rplease enter next number that you remember: "))
            user_list.append(z)

        if user_list == random_number:
            print('correct!')
            Score.add_score(mg_dif)
        else:
            print('incorrect!!!, try again.', time.sleep(0.70))
            memory_game(2)

        if mg_dif == 3:
            for i in range(0, 5):
                n = random.randint(1, 101)
                random_number.append(n)

            for x in random_number:
                time.sleep(0.70)
                print("\r {}".format(x), end="")
            time.sleep(0.70)
            print("\r0", end="")

            for i in range(0, 5):
                z = int(input("\rplease enter next number that you remember: "))
                user_list.append(z)

            if user_list == random_number:
                print('correct!')
                Score.add_score(mg_dif)
            else:
                print('incorrect!!!, try again.', time.sleep(0.70))
                memory_game(3)

            if mg_dif == 4:
                for i in range(0, 6):
                    n = random.randint(1, 101)
                    random_number.append(n)

                for x in random_number:
                    time.sleep(0.70)
                    print("\r {}".format(x), end="")
                time.sleep(0.70)
                print("\r0", end="")

                for i in range(0, 6):
                    z = int(input("\rplease enter next number that you remember: "))
                    user_list.append(z)

                if user_list == random_number:
                    print('correct!')
                    Score.add_score(mg_dif)
                else:
                    print('incorrect!!!, try again.', time.sleep(0.70))
                    memory_game(4)

                if mg_dif == 5:
                    for i in range(0, 7):
                        n = random.randint(1, 101)
                        random_number.append(n)

                    for x in random_number:
                        time.sleep(0.70)
                        print("\r {}".format(x), end="")
                    time.sleep(0.70)
                    print("\r0", end="")

                    for i in range(0, 7):
                        z = int(input("\rplease enter next number that you remember: "))
                        user_list.append(z)

                    if user_list == random_number:
                        print('correct!')
                        Score.add_score(mg_dif)
                    else:
                        print('incorrect!!!, try again.', time.sleep(0.70))
                        memory_game(5)
