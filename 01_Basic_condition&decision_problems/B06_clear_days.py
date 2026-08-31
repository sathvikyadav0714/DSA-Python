# Calculate Clear Days

# You are given:

# Number of cloudy days
# Number of rainy days
# Total number of days

# Calculate how many clear days there are.


total_days=7
number_of_rainy_days=int(input("Enter no of rainy days: "))
number_of_cloudy_days=int(input("Enter no of cloudy days: "))
clear_days=total_days-number_of_cloudy_days-number_of_rainy_days
print("number of clear days: ", clear_days)