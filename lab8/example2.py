def is_prime(x):
  for i in range(2,x):
    if x%i==0:
      return False
  return True

def print_primes_between(y,z):
  if y>z:
    y,z=z,y
  for i in range(y,z):
    a = is_prime(i)
    if a == True:
      print(i,end=" ")

def main():
  y = int(input("Enter first number: "))
  z = int(input("Enter second number: "))
  print_primes_between(y,z)

main()
