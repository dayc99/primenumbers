#once prime is imported into pythin you out the parameter for prime
def prime(num):
# i tracks what number you are testing to see if it is prime
    i = 2
# a goes through the possible divisors for i
    a = 2
#prime tracks if the number is prime
    pri = True
    
#the first while lets you enter multiple numbers to test for what 
#lower numbers are prime
    while num != 0:
    
#the second while increases the i value and prints the int
#if it is prime
        while num >= i:

#the third while checks to see if the values of i are prime
            while i>a:
#if i divided by a has no remamnder than the number
#is not prime
                if i%a==0:
                    pri = False
                a +=1

#if pri is true than print the prime value
            if pri == True:
                print(str(i))
            i+=1
#reset a to test the next i value
            a=2
            pri = True
#this lets you test another int for prime
        print('Enter 0 to End')
        num = int(input("Enter a number:"))
        i=2
    
