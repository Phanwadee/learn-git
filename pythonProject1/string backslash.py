print("\" sweet\" is an ice-cream")
dessert = "ice cream"
d = dessert[:5]
print(d)
print("ice" in dessert)
print(len(dessert))
print(dessert.isupper())
print("s" in dessert)

name = input("Enter your name")
print("My name is %s" %name)
print("I'm %d years old" %15)
print(name*15)

new = [1,2,3,5,7,9]
n = len(new)
print(n)
print(new[2:5])
new += [4,8,9]
new[4] = 4.3
print(new)
new.append(8)
print(new)
new[5] = ["dino","cat"]
print(new)
new[:6]=[]
print(new)
personal = {"Thapanee":31,"yod":43,"Papani":28}
personal["napapon"] = 56
print(personal)
del personal['yod']
print(personal)
print(personal.values())
print('napapon' in personal)
print("1" in new)
num = "123"
if num.isdigit():
    print(True)
else:
    print(False)


