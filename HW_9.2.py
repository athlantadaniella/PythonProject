def difference (*args):
    if (len(args) == 0):
        return 0
    else:
        max_value = max(args)
        min_value = min(args)
        difference = round((max_value - min_value),2)
    return difference

args = (1,2,3,4,5)
result = difference(*args)
print(result)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
