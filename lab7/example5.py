numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]

union = numbers1 + numbers2
union = set(union)
numbers1 = set(numbers1)
numbers2 = set(numbers2)

intersection = set()

for i in numbers1:
  if i in numbers2:
    intersection.add(i)

print("Intersection of two sets:",intersection)
print("Union of two sets:",union)
