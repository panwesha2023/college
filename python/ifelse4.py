#a book seller offers 50% discount if purchase amount is more than 10,000 otherwise discount is 10%.print the deposit amount
pa = float(input("Enter the purchase amount "))
dis = 0
da = 0
if(pa >= 10000):
  dis = pa * 50 / 100
else:
  dis = pa * 10 / 100
da = pa - dis
print("Deposit amount = ",da)
