number = int(input("Enter your number: "))

original_number = number
reversed_number = 0

while number > 0: 
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //=10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is a not palindrome")








numberLargest = int(input("Enter Largest number:"))
numberSmallest = int(input("Enter Smallest number:"))


while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ",numberLargest)