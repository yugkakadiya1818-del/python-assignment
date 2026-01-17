# wap to demonstrate user-defined functions by calculating the square and cube of a number.

def square(n):
    print("Square =", n * n)

def cube(n):
    print("Cube =", n * n * n)


num = int(input("Enter a number: "))

square(num)
cube(num)
