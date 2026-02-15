def add_one(lst):
    digit = 1
    for i in range(len(lst)-1, -1, -1):
        lst[i] += digit
        if lst[i] < 10:
            digit = 0
            break
        lst[i] = 0
    if digit:
        lst = [1] + lst
    return lst

x = [1, 2, 3, 4]
print(add_one(x))


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
