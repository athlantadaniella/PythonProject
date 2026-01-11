lst = [1,2,3,4,5]

if len(lst) == 0:
    x = [[], []]

elif len(lst) % 2 == 0:
    mid = len(lst) // 2
    x = [lst[:mid], lst[mid:]]

else:
    mid = (len(lst) + 1) // 2
    x = [lst[:mid], lst[mid:]]

print(x)


