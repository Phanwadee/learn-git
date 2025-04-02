rainblow = "red,orange,yellow,green,blue,indigo,violet"
color = input("What color does a rainblow have?")
count = 1
while color.isalpha()==True:
    if color in rainblow:
        print("Correct!")
        break
    else:
        count += 1
        color = input("What color does a rainbow have?")
        if count> 3:
            print("Your color is not color of rainblow")
            break