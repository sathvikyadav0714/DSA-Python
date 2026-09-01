# Given an integer n, determine whether it reads the same forwards and backwards.


# method 1
n=int(input("enter a number: "))
temp=n
rev=0
while n>0:
    last_digit=n%10
    rev=(last_digit)+rev*10
    n=n//10

if temp==rev:
    print(f"{temp} is an palindrome")
else:
    print("not a palindrome")


# method 2
n=input("Enter s number: ")
rev=n[::-1]
if n==rev:
    print("palindrome")
else:
    print("not palindrome")


# method 3

n = int(input("Enter a number: "))
rev = str(n)[::-1]
print(str(n) == rev)