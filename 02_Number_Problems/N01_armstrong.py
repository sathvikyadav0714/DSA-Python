# Given an integer n, determine whether it is an Armstrong number.

# An Armstrong number is a number where the sum of each digit raised to the power of the total number of digits equals the original number.

n=int(input("Enter an number: "))
temp=n
total_sum=0
length=len(str(n))
while n>0:
    last_digit=n%10
    total_sum+=last_digit**length
    n=n//10
if total_sum==temp:
    print(f"{temp} is an Armstrong number.")
else:
    (print(f"{temp} is not an Armstrong number.")) 