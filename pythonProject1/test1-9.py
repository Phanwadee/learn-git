idc = input("Please enter your ID: ")
sum = 0
sn = 0  #เลขคี่
dn = 0  #เลขคู่
for i in idc:
    if int(i) % 2 == 0:#เลขคู่ต้องหารสองแล้วได้ศูนย์
        dn+= 1
    else:
        sn+=1
    sum+=int(i)
print(sum,sn,dn)
