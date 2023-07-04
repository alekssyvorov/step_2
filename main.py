def task_1():
    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9 or j == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_2():
    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9 or j == 9 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_3():
    for i in range(11):
        for j in range(11):
            if i == 0 or i == 10 or j == 0 or j == 10 or j == 5:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_4():
    for i in range(11):
        for j in range(11):
            if i == 0 or i == 10 or j == 0 or j == 10 or i == 5:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_5():
    # Не понимаю
    for i in range(11):
        for j in range(12):
            if i == 0 or i == 11 or j < 6 or i == j:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_6():
    # Не понимаю
    pass


def task_7():
    for i in range(11):
        for j in range(11):
            if i == 0 or i == 10 or j == 0 or j == 10 or i == j or j == 10 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_8():
    for i in range(11):
        for j in range(11):
            if j == 0 or j == 10 or i == j or j == 10 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_9():
    for i in range(11):
        for j in range(11):
            if i == 0 or i == 10 or i == j or j == 10 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_10():
    for i in range(11):
        for j in range(11):
            if i == 0 or i == 10 or j == 0 or j == 10 or i == 5 or j == 5:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_11():
    for i in range(10):
        for j in range(10):
            if i == 9 or j == 0 or j == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_12():
    for i in range(11):
        for j in range(11):
            if i == 0 or j == 0 or j == 10 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_13():
    for i in range(10):
        for j in range(10):
            if i == 0 or j == 9 or j == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_14():
    for i in range(10):
        for j in range(10):
            if i == 9 or j == 9 or j == 9 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_15():
    for i in range(11):
        for j in range(11):
            if j == 0 or i == j / 2 or i == 10 - j / 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_16():
    for i in range(11):
        for j in range(11):
            if j == 10 or i == 10 - j - i or i == 10 + j - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_17():
    for i in range(6):
        for j in range(11):
            if i == 0 or i == j or i == 10 - j:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_18():
    for i in range(11):
        for j in range(11):
            if i == 5 or i == 5 - j or i == j - 5:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def task_19():
    print('*' * 11)
    for i in range(1, 10):
        print('*' + " " * i + '*' * (10 - i))
    print('*' * 11)


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    task_5()
    task_6()
    # task_7()
    # task_8()
    # task_9()
    # task_10()
    # task_11()
    # task_12()
    # task_13()
    # task_14()
    # task_15()
    # task_16()
    # task_17()
    # task_18()
    # task_19()
