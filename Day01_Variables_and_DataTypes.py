# -------------------------------
# Day 01: Variables & Data Types
# -------------------------------

# 1. Create a variable age and print its value and data type
age = 25              # Step 1: store age
print(age)            # Step 2: print value
print(type(age))      # Step 3: print data type


# 2. Store your name in a variable and print it
name = "Nagarjun"     # Step 1: store name
print(name)           # Step 2: print name


# 3. Create one integer and one float, add them and print result and type
marks = 62            # Step 1: integer value
percentage = 68.7     # Step 2: float value
total = marks + percentage   # Step 3: add both values
print(total)          # Step 4: print result
print(type(total))    # Step 5: print data type


# 4. Assign a boolean value and print its type
is_student = True     # Step 1: boolean value
print(type(is_student))  # Step 2: print data type


# 5. Create a variable with None and print its type
habit = None          # Step 1: assign None
print(type(habit))    # Step 2: print data type


# -------------------------------
# Type Conversion
# -------------------------------

# 6. Convert string "50" into integer
string_value = "50"           # Step 1: string value
print(type(string_value))     # Step 2: type before conversion

int_value = int(string_value) # Step 3: convert to integer
print(int_value)              # Step 4: print integer
print(type(int_value))        # Step 5: type after conversion


# 7. Convert integer 10 into float
x = 10               # Step 1: integer value
y = float(x)         # Step 2: convert to float
print(y)             # Step 3: print float
print(type(y))       # Step 4: print data type


# 8. Convert number 25 into string and print sentence
age = 25                     # Step 1: integer value
age_str = str(age)           # Step 2: convert to string
print("I am " + age_str + " years old")  # Step 3: print message


# 9. Take a number as input and print its data type
num = input("Enter a number: ")   # Step 1: take input
print(type(num))                  # Step 2: input is always string


# 10. Convert input to integer and add 5
num = input("Enter a number: ")   # Step 1: take input
num_int = int(num)                # Step 2: convert to integer
result = num_int + 5              # Step 3: add 5
print(result)                     # Step 4: print result
