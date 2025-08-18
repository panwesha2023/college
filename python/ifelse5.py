#a shopkeeper offers 20% discount if pa is more than 7000, otherwise discount is 5%.print the deposit amount.
pa = float(input("Enter the pa "))
dis = 0
da = 0
if(pa >= 7000):
  dis = pa * 20 / 100
else:
  dis = pa * 5 / 100
da = pa - dis 
print("Deposit amount= ",da)
