def x(list0):
  summ = 0
  for i in list0:
    summ += i
  return summ**2

def main():
  a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
  print(x(a_list))

main()

