# ===============================
# Day 9 – Function Solutions
# ===============================

print("\n--- Q1 Simple Function ---")
def greet():
    print("Hello Python")

greet()


print("\n--- Q2 Function with Parameter ---")
def hello(name):
    print("Hello", name)

hello("Nagarjun")


print("\n--- Q3 Add Two Numbers ---")
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


print("\n--- Q4 Return Square ---")
def square(n):
    return n * n

result = square(5)
print("Square =", result)


print("\n--- Q5 Even or Odd ---")
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"   

print(check(7))       