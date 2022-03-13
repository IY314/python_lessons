def prime(x):
    for factor in range(1, x // 2):
        if not x % factor and factor != 1:
            print(f'It is composite; can be divided by {factor}')
            return
    print('It is prime')


def main():
    while True:
        try:
            i = int(input('Enter a number\n'))
            break
        except ValueError:
            print('Invalid number')
    prime(i)


if __name__ == '__main__':
    main()
