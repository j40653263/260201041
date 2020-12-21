def get_reversed(list0):
    if len(list0) == 0:
        return list0
    else:
        return (get_reversed(list0[1:])) + [list0[0]] 

print(get_reversed([1, 2, 3, 4]))