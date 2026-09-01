# Given two positive integers a and b, find their GCD (Greatest Common Divisor).


# method 1 

a=12
b=24
gcd=0
# m=min(a,b)
limit=0
if a<b:
    limit=a
else:
    limit=b
for i in range(1,limit+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# method 2
a = 18
b = 36

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)