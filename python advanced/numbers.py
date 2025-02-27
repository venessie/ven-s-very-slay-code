def checkIfSame(number1, number2):
    if ((number1 ^ number2) != 0 ):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")

number1 = int(input("Enter first number to compare : "))
number2 = int(input("Enter second number to compare :"))

checkIfSame(number1, number2)









def OddOccurring(arr):
    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []
n = int(input("Enter array size : "))

while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1                    

print("\n\nOdd occuring number is :", OddOccurring(arr))