# Given an integer n, determine whether it is an Armstrong number.

# An Armstrong number is a number where the sum of each digit raised to the power of the total number of digits equals the original number.

n=153
temp=n
sum=0
while n>0:
    last_digit=n%10
    sum+=last_digit**3
    n=n//10
if sum==temp:
    print(f"{temp} is an Armstrong number.")
else:
    (print(f"{temp} is not an Armstrong number."))