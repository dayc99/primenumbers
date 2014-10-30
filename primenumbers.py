
i = 2
print('Enter 0 to End')
num = int(input("Enter a number:"))
pri = False

while num != 0:
    while num > i:
        if num%i==0:
            pri = True
            print(str(i) + ', ')
        i +=1

    if pri == False:
        print(str(num) + ' is Prime')
    else:
        print(str(num) + ' is Not Prime')

    num = int(input("Enter a number:"))
    pri = False
    i = 2
    


