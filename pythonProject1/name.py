

name = "phanwadee,samart,james"
g = input("enter my name")
count = 1
while g.isalpha() == True:
    if g in name:
        print("correct!")
        break
    else:
        count +=1
        g = input("enter my name")
        if count>=3:
            print("you're done")
            break