# Given two integers a and b, find the absolute difference between them.

# The answer must always be non-negative.

a=int(input("enter first number: "))
b=int(input("enter second number: "))

if a>b:
    print(a-b)
elif b>a:
    print(b-a)
else:
    print(0)