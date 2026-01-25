while True:
    x = int(input('Enter number 1: '))
    op = input('Enter operator (+, -, *, /): ')
    y = int(input('Enter number 2: '))

    if op == '+':
        print('Result:', x + y)

    elif op == '-':
        print('Result:', x - y)

    elif op == '*':
        print('Result:', x * y)

    elif op == '/':
        if y == 0:
            print('Error: division by zero!')
        else:
            print('Result:', x / y)

    else:
        print('Error: invalid operator!')

    choice = input('Continue? (y/yes to continue): ').lower()

    if choice not in ('y', 'yes'):
        print('The End')
        break
