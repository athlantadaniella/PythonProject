def common_elements():
    lst_1 = [x for x in range(100) if x % 3 == 0]
    lst_2 = [x for x in range(100) if x % 5 == 0]
    result = set(lst_1).intersection(lst_2)
    return result

common = common_elements()

print(common)


# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
