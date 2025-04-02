listnum = []
count = 0
while count < 5:
    num = int(input("enter your number:"))
    listnum.append(num)
    count+=1
# print(max(listnum)) ใช้ในกรณีสูตรสำเร็จ
print(listnum)
#[x,x,x,x,x]
maxvalue = 0
for x in listnum:
    if x>maxvalue:
        maxvalue = x
print(maxvalue)

