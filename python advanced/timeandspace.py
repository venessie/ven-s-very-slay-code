def time(n):
    return n * (n+1)/2

print(time(5))

def space(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(space(6))


def button(n):
    sum = 0
    for i in range(1,n+1):
        for j in range (i,i+1):
            sum += i
    return sum
print(button(9))























def multiply (n,m):
    return n*m
n = 2
m = 3
print(multiply (n,m))


def division (n,m):
    return n/m
n = 2
m = 3
print(division (n,m))



def subtraction (n,m):
    return n-m
n = 3
m = 2
print(subtraction (n,m))


def addition (n,m):
    return n+m
n = 3
m = 2 
print(addition (n,m))