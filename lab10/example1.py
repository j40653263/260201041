def basic_mult(n):
  if n == 0:
    return 0
    
  return basic_mult(n-1) + 3 
  
print(basic_mult(10))