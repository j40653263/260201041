def sum_list(x):
  if len(x) == 0:
    return 0
  elif isinstance(x[0], list):
    return sum_list(x[0]) + sum_list(x[1:])
  else:
    return x[0] + sum_list(x[1:])

print(sum_list([3,12,76,[4,56,43],[2,8],81,75]))

"""
def sum_of_a_nested_list(x):
  if not isinstance(x, list):
    return x
  else:
    sum = 0
    for a in x:
      sum += sum_of_a_nested_list(a)
    return sum

print(sum_of_a_nested_list([3, 12, 76, [4, 56, 43], [2, 8], 81, 75]))
"""