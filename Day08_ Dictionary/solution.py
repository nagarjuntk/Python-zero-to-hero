# ===============================
# Day 8 – Dictionary Solutions
# ===============================

print("\n--- Q1 Create Dictionary ---")
student = {
    "name": "Nagarjun",
    "age": 22,
    "branch": "ISE"
}
print(student)


print("\n--- Q2 Access Values ---")
print("Name:", student["name"])
print("Age:", student["age"])


print("\n--- Q3 Add and Update ---")
student2 = {
    "name": "Nagarjun",
    "age": 22
}

student2["branch"] = "ISE"   # add
student2["age"] = 23         # update

print(student2)


print("\n--- Q4 Loop Dictionary ---")
for key, value in student.items():
    print(key, ":", value)


print("\n--- Q5 Character Frequency ---")
text = input("Enter a word: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)