# Electricity Bill Program

print("------ Electricity Bill ------")

name = input("Enter Customer Name: ")
units = int(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

print("\n----- Electricity Bill -----")
print("Customer Name :", name)
print("Units Consumed:", units)
print("Total Bill    : Rs.", bill)
