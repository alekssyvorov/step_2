def odd_numbers(a: int, b: int):
    for i in range(a, b+1):
        if i % 2 == 1:
            print(i)


def main():
    a = int(input('A '))
    b = int(input('B '))
    odd_numbers(a, b)


if __name__ == "__main__":
    main()