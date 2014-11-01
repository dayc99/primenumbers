
i = 2
a = 2
print('Enter 0 to End')
num = int(input("Enter a number:"))
pri = False

while num != 0:
    
    while num >= i:

        while i>a:
            if i%a==0:
                pri = True
            a +=1

        if pri == False:
            print(str(i))
        i+=1
        a=2
        pri = False
    num = int(input("Enter a number:"))
    i=2
