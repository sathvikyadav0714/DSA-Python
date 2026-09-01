# Given an integer n, determine whether it is a Harshad number.

# A number is Harshad if it is divisible by the sum of its digits.

n=int(input("Enter a number: "))
temp=n
total=0
while n>0:
    last_digit=n%10
    total+=last_digit
    n=n//10

if temp%total==0:
    print(f"{temp} is an harshad number")
else:
    print("not a harshad number") 