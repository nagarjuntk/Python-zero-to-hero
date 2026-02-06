# -------------------------------
# Day 04: Input & Output
# -------------------------------

# 1. Name input
name = input("Enter your name: ")
print(name)


# 2. Age input
age = input("Enter your age: ")
print(age)


# 3. Sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


# 4. Square of a number
num = int(input("Enter a number: "))
print("Square =", num * num)


# 5. Operations on two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum =", x + y)
print("Difference =", x - y)
print("Product =", x * y)


# 6. Formatted output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old")


# 7. Total and average of marks
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total =", total)
print("Average =", average)
 
 