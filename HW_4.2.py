lst = [0, 1, 7, 2, 4, 8]

lst_new = sum(lst[::2]) * lst[-1] if lst else 0
print(lst_new)