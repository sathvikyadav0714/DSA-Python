# Given two numbers a and b, determine whether a is at least 7% of b.

# Print yes if the condition is satisfied; otherwise print no.

a=int(input("enter first number: "))
b=int(input("enter second number: "))

percentage_7=(7/100)*b

if a>=percentage_7:
    print("yes")
else:
    print("NO")

#how to calculate percentage
# 
# a = 7
b = 100

percentage = (a / b) * 100

print(percentage)
print(round(percentage)) # to get roundoff valuee
