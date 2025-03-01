def power2(number):

    if (number == 0):
        return 0
    if ((number & (~(number - 1))) == number):
        return 1
    return 0 

number = int(input("Enter the number : "))

if (power2(number)):
    print("\nThe number is power of 2")
else:
    print("\nThe number is not power of 2")







def powerOf4(number):
    count = 0

    if(number & (~(number & (number - 1)))):

        while(number > 1):
            number >>= 1
            count += 1

        if(count % 2 == 0):
            return True
        else: 
            return False
        

number = int(input("Enter your number : "))
if (powerOf4(number)):
    print(number, 'is a power of 4')
else: 
    print(number, 'is not a power of 4')






def computePower( x, y):

    result = 1

    while(y > 0):
        if(y % 2 == 0):
            x = x * x
            y>>=1


        else:
            result = result * x
            y = y - 1

    return result



x = int(input("Enter x for x^y : "))
y = int(input("Enter y for x^y : "))
print("Total : ", (computePower(x, y)))