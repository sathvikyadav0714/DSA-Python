# Given an amount of money a person wants to withdraw and their available balance, determine whether the withdrawal is possible.

# The withdrawal is allowed only when the required conditions are satisfied.

balance=1000
withdraw=int(input(("Enter amount you wn=ant to withdraw: ")))

if withdraw<=balance:
    print("Withdraw successfull")
else:
    print("Withdraw failed")
