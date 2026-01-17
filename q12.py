# wap to sort a list of numbers in ascending order.

numbers = input("Enter numbers : ")

numbers_list = [int(num) for num in numbers.split()]

numbers_list.sort()

print("Sorted list in ascending order:", numbers_list)
