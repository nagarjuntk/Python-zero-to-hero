# ---------------------------------
# Day 06: Simple List Operations
# ---------------------------------

# 1. Create a list
my_list = [10, 20, 30, 40, 50]

# 2. Print the entire list
print("Original List:", my_list)


# 3. Print element at index 2
print("Element at index 2:", my_list[2])


# 4. Add a new element at the end
my_list.append(60)
print("After append:", my_list)


# 5. Insert a value at index 1
my_list.insert(1, 15)
print("After insert:", my_list)


# 6. Remove an element (remove 30)
my_list.remove(30)
print("After remove:", my_list)


# 7. Update first element
my_list[0] = 5
print("After update:", my_list)


# 8. Find length of list
print("Length of list:", len(my_list))


# 9. Count occurrence of 20
print("Count of 20:", my_list.count(20))


# 10. Reverse the list
my_list.reverse()
print("Reversed list:", my_list)
