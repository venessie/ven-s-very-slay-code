def sun(n):
    return n*(n+1)/2
print(sun(10))


def arraysum(a):
    sum=0
    for i in a:
        sum = sum + i

    return(sum)

a = [1,1,1,1]
print(arraysum(a))




def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
        
    j=1
    while(j<=n+1):
        print("Second Loop", j)
        j=j*2

    for i in range(0,100):
        print("Third Loop")


print(myfunction(3))
    
