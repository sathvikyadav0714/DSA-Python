# Given an integer n, determine whether it is a Perfect number.

# A Perfect number is equal to the sum of all its proper divisors, excluding itself.

n=6
total=0
for i in range(1,n):
    if n%i==0:
        total+=i

if total==n:
    print(f"{n} is a perect number")
else:
    print("not a perfect number")
