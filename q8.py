# wap to reverse a given number and check whether it is a palindrome.

num = input("Enter a number: ")

rev = num[::-1]

print("Reversed number:", rev)

if num == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
