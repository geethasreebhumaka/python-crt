def addDigits(num):
    number=0
    while num>=10:
        sum=0
        while num>0:
            number=num%10
            sum+=number
            num=num//10
        num=sum
    return num
num=int(input())
print(addDigits(num))