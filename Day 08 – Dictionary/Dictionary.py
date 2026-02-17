
# ---------------------------------
# Day 08: Dictionary Practice
# ---------------------------------

# 1. Create dictionary
student = {
    "name": "Nagarjun",
    "age": 22,
    "marks": 85
}

print("Original dictionary:", student)


# 2. Access marks
print("Marks:", student["marks"])


# 3. Add new key "city"
student["city"] = "Bangalore"
print("After adding city:", student)


# 4. Update marks
student["marks"] = 90
print("After updating marks:", student)


# 5. Remove age key
student.pop("age")
print("After removing age:", student)


# 6. Print all keys
print("Keys:", student.keys())


# 7. Print all values
print("Values:", student.values())


# 8. Loop through dictionary
print("Key-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

