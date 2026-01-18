lst = [5, 1, 0, 12, 3, 7, 5, 0, 6]

i = 0
n = len(lst)
while i < n:
    if lst[i] == 0:
        lst.pop(i)
        lst.append(0)
        n -= 1
    else:
        i += 1

print(lst)
