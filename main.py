def odd_numbers(a: int, b: int):
    for i in range(a, b + 1):
        if i % 2 == 1:
            print(i)


def draw(length: int, direction: str, symbol: str):
    if direction == "horizon":
        print(symbol * length)
    else:
        for i in range(length):
            print(symbol)


def func_max(*args) -> int:
    return max(args)


def func_sum(a: int, b: int) -> int:
    return sum(range(a, b + 1))


def prime(number: int) -> bool:
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return True if counter == 2 else False


def happy(number: int) -> bool:
    a, b = 0, 0
    for i in range(3):
        a += number % 10
        number = number // 10
    for i in range(3):
        b += number % 10
        number = number // 10
    return True if a == b else False


def main():
    # a = int(input('A '))
    # b = int(input('B '))
    # odd_numbers(a, b)
    # length = int(input('Input length '))
    # direction = input('Input horizont or vertical ')
    # symbol = input('Input symbol ')
    # draw(length, direction, symbol)
    # print(func_max(1,2,3))
    # print(func_sum(1, 3))
    # print(prime(151))
    print(happy(133331))


if __name__ == "__main__":
    main()
