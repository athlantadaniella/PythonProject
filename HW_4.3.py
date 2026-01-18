import random

lst = [random.randint(3,10) for i in range(10)]
print(lst)
lst_new = [lst[i] for i in (0, 2, -2)]
print(lst_new)