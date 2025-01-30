def printnumber(n):
    iteration=0
    print("The number entered by user is",n)
    iteration+=1
    print("Total iterations done by the code is",iteration,"\n")



printnumber(10)
printnumber(20)
print("\n With any 'n' the time taken by our code won't change")






def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=2
    print("When n is",n,"Iterations = ",iteration)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nWith every 'n' the time taken and iterations will increase")







def ONSqaureTime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
         print("*", end = "  ")
         iteration+=1
        print("")
    print("\nWhen n is ",n," Iteration = ",iteration, "\n")


ONSqaureTime(5)
ONSqaureTime(4)
ONSqaureTime(3)


print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")