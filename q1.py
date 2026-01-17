# wap to input two numbers and display their addition,subtraction,multiplication and division.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division \n")

c = int(input("Enter choice: "))

if c == 1:
    print("Ans:",a + b)
elif c == 2:
    print("Ans:",a - b)
elif c == 3:
    print("Ans:",a * b)
elif c == 4:
    print("Ans:",a / b)
else:
    print("Wrong choice")

