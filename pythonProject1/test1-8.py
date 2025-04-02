#จงเขียนโปรแกรม หาว่าชื่อโรงเรียน tepleela school มีตัวอักษร a e i o u รวมกันกี่ตัว
#1.สร้างตัวแปร ชื่อโรงเรียน
#2.เงื่อนไขคือหาผลรวมของตัวอักษที่มี a e i o u
#3.ประกาศผลรวม
txt = "tepleela school"
sum = 0
for t in txt:
    if t == "a" or t == "e" or t == "i" or t == "o" or t =="u":
        sum +=1
print(sum)
