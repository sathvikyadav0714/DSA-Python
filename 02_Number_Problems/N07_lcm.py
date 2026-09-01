# Given two positive integers a and b, find their LCM (Least Common Multiple).

# method 1
a=12
b=18
if a > b:
    start = a
else:
    start = b

for i in range(start, a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break

# method 2 
a = 12
b = 18

x = a
y = b

while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x

lcm = (a * b) // gcd

print(lcm)