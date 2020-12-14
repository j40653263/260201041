a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b**2 - 4*a*c

if delta > 0:
    print("There are two real roots.")
    x1 = -b + (delta**0.5) / (2 * a)
    x2 = -b - (delta**0.5) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
elif delta == 0:
    print("There is one real root.")
    x = -b / (2 * a)
    print("x1 = x2 = ", x)
else:
    print("There are two complex roots.")
    i = (-1)**0.5
    x1 = -b + i * (delta**0.5) / (2 * a)
    x2 = -b - i * (delta ** 0.5) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)