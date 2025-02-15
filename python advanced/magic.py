import sqrt  # Import sqrt function

# Input from the user

number = int(input("Enter your number: "))

print("\n")

# Check if the number is greater than 1

if number > 1:

    for i in range(2, int(sqrt(number)) + 1):

        if number % i == 0:

           print(number, "is not a prime number")

           break # Exit loop if a factor is found

    else:

       print(number, "is a prime number") # Runs if loop completes without breaking

else:


    print(number, "is not a prime number") # Handles numbers <= 1

 