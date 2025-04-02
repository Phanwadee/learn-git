suma = 0
sumo = 0
while True:
    sum = input("please input number or q for exit prograam")
    if sum == 'q':
        break;
    if sum.isdigit():
        sumo = int(sum)
        suma = suma + sumo
    else:
        print('input just digit')
    print("summation is",suma)
