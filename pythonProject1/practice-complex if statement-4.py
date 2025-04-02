from operator import ifloordiv


max_amount = 7
min_amount = 1
price = 40
pork_num = float(input("a weight of pork"))
if (pork_num > max_amount):
    print(pork_num,"is more than currently available stock")
elif (min_amount <= pork_num <= max_amount):
    print(pork_num,"total Price",(price *(pork_num)))
else:
    print(pork_num,"is below minimum order amount")