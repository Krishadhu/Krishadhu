# h2 - E-Commerce Price Filter using Binary Search

prices = [15000, 22000, 35000, 50000, 56000, 62000, 70000]

target = int(input("Enter Minimum Price: "))

low = 0
high = len(prices) - 1
answer = -1

while low <= high:

    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1

    else:
        low = mid + 1

if answer != -1:
    print("First Product Price:", prices[answer])
else:
    print("No Product Found")
