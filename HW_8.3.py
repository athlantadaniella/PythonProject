def find_unique_value(numbers):

    for num in numbers:
        if numbers.count(num) == 1:
             return int(num) if num.is_integer() else num

numbers = input("Enter some numbers: ").replace(',', ' ').split()
numbers = [float(x) for x in numbers]
print(find_unique_value(numbers))

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")