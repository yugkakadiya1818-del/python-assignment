# wap to check whether a given number is a prime number.

n = int(input("Enter number : "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime number")
            break
    else:
        print("Prime number")
else:
    print("Not prime number")
