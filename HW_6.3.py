num = int(input('Enter number: '))

while num > 9:
    start = 1
    for digit in str(num):
        start *= int(digit)
    num = start

print(num)