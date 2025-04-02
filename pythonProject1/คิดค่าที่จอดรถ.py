inH = float(input("Please enter your time in Hours"))
inM = float(input("Please enter your time in Minute"))
outH = float(input("Please enter your time out Hours"))
outM = float(input("Please enter your time out Minute"))
price = (((outH - inH)*10) + (((outM - inM)/60)*10))

if price < 15:
    print("free")
elif 15 <= price = 60:
    print("10")
elif 61 <= price = 120:
    print("20")
elif 121 <= price = 180:
    print("30")
elif 181 <=-