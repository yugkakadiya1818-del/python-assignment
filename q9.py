# wap to find the sum of digits of a given number.

num = int(input("Enter a number: "))

num = abs(num) 
sum_of_digits = 0

for digit in str(num):      
    sum_of_digits += int(digit)  

print("Sum of digits is:", sum_of_digits)
