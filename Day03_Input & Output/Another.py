# Write a program that:

# Takes two friends’ names and ages as input

# Prints a sentence showing they are best friends

# Take input Friend 1 name and age
friend1_name = input("Friend 1 Name: ")
friend1_age = int(input("Friend 1 Age: "))

# Take input Friend 2 name and age
friend2_name = input("Friend 2 Name: ")
friend2_age = int(input("Friend 2 Age: "))

# Print friendship message
print(friend1_name + " and " + friend2_name + " are best friends")

# Calculate age difference
age_diff = abs(friend1_age - friend2_age)

# Final formatted output
print(f"{friend1_name} and {friend2_name} have an age difference of {age_diff} years")
