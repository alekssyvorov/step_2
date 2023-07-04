from random import randint


def rand_lst() -> list:
    return [randint(-50, 50) for i in range(20)]


def task_1() -> int:
    temp = rand_lst()
    return sum([elem for elem in temp if elem < 0])


def task_2() -> int:
    temp = rand_lst()
    return sum([elem for elem in temp if elem % 2 == 0])


def task_3() -> int:
    temp = rand_lst()
    return sum([elem for elem in temp if elem % 2 == 1])


def task_4() -> int:
    res = 1
    temp = rand_lst()
    for i in range(len(temp)):
        if i % 3 == 0:
            res *= temp[i]
    return res


def task_5() -> int:
    temp = rand_lst()
    minimum = temp[0]
    maximum = temp[0]
    for elem in temp:
        if minimum > elem:
            minimum = elem
    for elem in temp:
        if maximum < elem:
            maximum = elem
    return minimum * maximum


def task_6() -> int:
    summa = 0
    temp = rand_lst()
    for elem in temp:
        if elem > 0:
            summa += elem
            break
    for i in range(len(temp) - 1, 0, -1):
        if temp[i] > 0:
            summa += temp[i]
            break
    return summa


def task_7() -> list:
    temp = rand_lst()
    return [i for i in temp if i % 2 == 0]


def task_8() -> list:
    temp = rand_lst()
    return [i for i in temp if i % 2 == 1]


def task_9() -> list:
    temp = rand_lst()
    return [i for i in temp if i < 0]


def task_10() -> list:
    temp = rand_lst()
    return [i for i in temp if i > 0]


if __name__ == "__main__":
    print(task_1())
    print(task_2())
    print(task_3())
    print(task_4())
    print(task_5())
    print(task_6())
    print(task_7())
    print(task_8())
    print(task_9())
    print(task_10())
