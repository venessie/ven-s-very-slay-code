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
