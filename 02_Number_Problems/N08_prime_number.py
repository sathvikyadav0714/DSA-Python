# Given an integer n, determine whether it is prime.

# A prime number has exactly two factors:

# 1 and itself


n=int(input("enter a number: "))
count=0
if n<=1:
    print("Not a prime number")
else:
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            count+=1
    if count==1:
        print("prime number")
    else:
        print("not a prime number")