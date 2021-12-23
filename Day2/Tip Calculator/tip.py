print("Welcome to the Tip Calculator")

total = float(input("Enter Total bill amount: "))
tip = int(input("How much tip you want to pay: 10, 12 or 15? "))
totalPersons = int(input("Enter how many persons: "))
'''
Total amount with Tip = (Tip / 100 * total) + total

OR ( taking total as common)

Total amount with Tip = total * (1 + tip/100) Since tip = 10 or 12 or 15

'''
grandTotal = total * (1 + tip/100)

eachShare = grandTotal/totalPersons

print("{:.2f}".format(eachShare))
