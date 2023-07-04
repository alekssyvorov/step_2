from random import randint

def arr()->list:
    lst = [randint(-10, 30) for i in range(randint(5, 15))]
    return lst

def task_1()->int:
    summa = 0
    lst = arr()
    for i in lst:
        if i > 0:
            summa += i
    return lst

def task_2():
    lst = [randint(-30, 10) for i in range(30)]
    summa = 0
    for i in lst:
        if i > 0:
            break
        else:
            summa += i
    return summa

if __name__ == '__main__':
    print(task_1())
    print(task_2())