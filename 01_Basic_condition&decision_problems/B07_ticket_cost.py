# A person wants to buy 4 tickets.

# Given the price of one ticket, calculate the total cost.

# Then check whether the total cost is less than or equal to 1000.

# If total cost <= 1000, print yes.
# Otherwise, print no.


ticket_price=int(input("enter one ticket price: "))

total_amout=ticket_price*4

if total_amout<=1000:
    print("Yes")
else:
    print("No")