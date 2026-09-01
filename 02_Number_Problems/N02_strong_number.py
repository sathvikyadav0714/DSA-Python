# Given an integer n, determine whether it is a Strong number.

# A number is Strong if the sum of the factorials of its digits equals the original number.

n=145
temp=n
total_sum=0
while n>0:
    last_digit=n%10
    
    factorial=1
    for i in range(1,last_digit+1):
        factorial*=i
    total_sum+=factorial
    n=n//10
if total_sum==temp:
    print(f"{temp} is a Strong number.")
else:   
    print(f"{temp} is not a Strong number.") 
