def fibo(num) -> int:
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


def ameba(hours) -> int:
    res = 1
    for i in range(1, int(hours / 3) + 1):
        res *= 2
    return res


def bank() -> tuple:
    money = 1000
    growth = 0
    for i in range(10):
        growth += 1000 * 0.02
    profit = money
    for i in range(12):
        profit += money * 0.02
    return growth, profit


if __name__ == "__main__":
    # num = int(input('Input '))
    # print(fibo(num))
    # count_hours = int(input('Input hours '))
    # print(ameba(12))
    print(bank())
