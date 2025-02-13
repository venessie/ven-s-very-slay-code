number = int(input("Input your number:"))
digits = len(str(number))
resultNumber = 0

temp = number
while temp > 0:
    digit= temp % 10
    resultNumber += digit ** digits
    temp //= 10

if number == resultNumber:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")








def print_factors(number):
    print("The factors of",number,"are:")
    for i in range(1, number + 1):
        if number % i == 0:
           print(i) 

number = int(input("Enter your number to find it's factors:"))
print_factors(number)