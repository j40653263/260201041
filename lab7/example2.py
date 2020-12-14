books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {}
for i in books:
    book_dict[i] = (len(i),len(set(i)))
for k,v in book_dict.items():
    print(k,"---->",v)

for i in books:
    a = len(i)
    b = len(set(i))
    book_dict[i] = (a,b,float((a+b)/2))
for k,v in book_dict.items():
    print(k,"---->",v)   