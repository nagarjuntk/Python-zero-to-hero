# -------------------------------
# Day 04: String Practice
# -------------------------------

# Create a string variable
name = "Nagarjun"
print(name)

# Print first character (index 0)
print(name[0])

# Print last character (negative index)
print(name[-1])

# Print length of the string
print(len(name))


# String concatenation
first_name = "Nagarjun"
last_name = "TK"
full_name = first_name + " " + last_name
print(full_name)


# Convert string to uppercase and lowercase
name_lower = "nagarjun"
print(name_lower.upper())   # Convert to uppercase
print(name_lower.lower())   # Convert to lowercase


# Check if a word exists in string
greeting = "Hii nagarjun"
print("Hii" in greeting)   # Returns True or False


# Reverse a string using slicing
name_reverse = "nagarjun"
print(name_reverse[::-1])


# Count occurrences of a character
print(name_reverse.count("a"))


# Replace a word in string
new_name = name_reverse.replace("nagarjun", "Arjun")
print(new_name)


# f-string formatting
name = "Arjun"
age = 22
print(f"My name is {name} and I am {age} years old")
