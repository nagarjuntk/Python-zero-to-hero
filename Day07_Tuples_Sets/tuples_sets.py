# ---------------------------------
# Day 07: Tuples and Sets
# ---------------------------------

# ========================
# 🔹 TUPLES
# ========================

# 1. Create a tuple
my_tuple = (10, 20, 30, 40, 20)

print("Tuple:", my_tuple)

# 2. Access element at index 3
print("Element at index 3:", my_tuple[3])

# 3. Find index of value 30
print("Index of 30:", my_tuple.index(30))

# 4. Count occurrence of 20
print("Count of 20:", my_tuple.count(20))

# 5. Tuple slicing
print("Sliced tuple:", my_tuple[1:4])

# Tuples are immutable
# my_tuple[0] = 100   # ❌ This will cause an error


# ========================
# 🔹 SETS
# ========================

# 6. Create a set (duplicates automatically removed)
my_set = {10, 20, 30, 40, 20}

print("Set:", my_set)

# 7. Add new element
my_set.add(50)
print("After adding 50:", my_set)

# 8. Remove an element
my_set.remove(30)
print("After removing 30:", my_set)

# 9. Create another set
set2 = {40, 50, 60, 70}

# 10. Union
print("Union:", my_set.union(set2))

# 11. Intersection
print("Intersection:", my_set.intersection(set2))

# 12. Difference
print("Difference:", my_set.difference(set2))
