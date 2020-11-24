square_matrix = int(input("How many columns&rows in your square matrix: "))
print("Okey, you have",square_matrix,"colums&rows in your square matrix!")
print("Please enter your square matrix line by line:")
print()

trace_matrix = []
for i in range(square_matrix):
  x = input().split(" ")
  trace_matrix.append(x[i])

output = 0
for i in trace_matrix:
  output += int(i)

print("Output:",output)