x = int(input('Enter number 1: '))
op = input('Enter operator (+, -, *, /): ')
y = int(input('Enter number 2: '))

if op == '+':
    print(x + y)

elif op == '-':
    print(x - y)

elif op == '*':
    print(x * y)

elif op == '/':
    if y == 0:
        print('Error: division by zero!')
    else:
        print(x / y)

else:
    print('Error: invalid operator!')
