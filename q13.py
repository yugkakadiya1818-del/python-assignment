# wap to perform linear search on a list.

lst = [10, 20, 30, 40, 50]
key = int(input("Enter element to search : "))

for i in range(len(lst)):
    if lst[i] == key:
        print("Element found at index : ", i)
        break
else:
    print("Element not found")
