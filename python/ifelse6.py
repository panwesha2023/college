#A fancy store offers 12% discount if no. of items are more than 10 otherwise discount is 5%.print the deposit amount
ni = int(input("Enter the number of items: "))
pi = float(input("Enter the price of items: "))
dis = 0
da = 0
if(ni >= 10):
  dis = (pi * ni) * 12 / 100
else:
  dis = (pi * ni) * 5 / 100
da = (pi * ni) - dis
print("Deposit amount = ",da)
