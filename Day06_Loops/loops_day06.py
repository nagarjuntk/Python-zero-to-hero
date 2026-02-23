# ---------------------------------
# Day 06: Loops Practice
# ---------------------------------

# 1. Print numbers from 1 to 10 using for loop
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i)


# 2. Print numbers from 10 to 1 using while loop
print("Numbers 10 to 1:")
num = 10
while num >= 1:
    print(num)
    num -= 1


# 3. Print even numbers from 1 to 20
print("Even numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 4. Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i

print("Sum:", total)


# 5. Break when number becomes 5
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 6. Skip number 3 using continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 7. Multiplication table of 5
print("Table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i) 