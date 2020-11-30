list0 = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

for i in list0:
  if i[1]>18:  #i[1] = age > 18
    print(i[0]) #i[0] = name

""""
for name,age in list0:
  if age>18:
    print(name)
"""