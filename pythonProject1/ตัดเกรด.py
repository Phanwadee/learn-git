x = float(input("enter your score"))
if 80 <= x <=100:
    print("A")
elif 75 <= x <80:
    print("B+")
elif 70 <= x < 75:
    print("B")
elif 65 <= x <70:
    print("C+")
elif 60 <= x <65:
    print("C")
elif 55 <= x <= 60:
    print("D+")
elif 50 <= x < 55:
    print("D")
elif 0 <= x < 50:
    print("F")
else:
    print("ERROR")