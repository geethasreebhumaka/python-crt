#to print n natural numbers using recurssion
def naturalnum(n):
    if n==10:
        return
    print((n))
    naturalnum(n+1)
naturalnum(1)

#to print the numbers from reverse order
def kk(n):
    if n==10:
        return
    kk(n+1)
    print((n))
kk(1)

#fibnacciseries 
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b 
        b=c 
        print(c)
n=int(input())
fib(n)

#fibonacci series using recurrsion
def fib1(n):
    if n==0 or n==1:
        return n 
    return fib1(n-1)+(n-2)
n=int(input())
print(fib1(n))

#factorial
def fact(n):
    f=1 
    for i in range(1,n+1):
        f*=i 
    print(f)
n=int(input())
fact(n)

#factorial using recurrsion
def fact1(n):
    if n==0 or n==1:
        return n 
    return n*fact1(n-1)
print(fact1(6))