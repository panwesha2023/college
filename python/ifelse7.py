#A shopkeeper offers 30% discount if no. of items are more than 15 otherwise discount is 10%.print the deposit amount.
ni = int(input("Enter the number of items "))
pi = float(input("Enter the price per item "))
dis = 0
da = 0
if(ni >= 15):
  dis = (pi * ni) * 30 / 100
else:
  dis = (pi * ni) * 10 / 100
da = (pi * ni)-dis
print("Deposit amount= ",da)
