# -------------------------------
# Day 04: Strings
# -------------------------------

# 1. Create and print a string
name = "Nagarjun"
print(name)


# 2. First and last character
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])


# 3. Length of string
word = "Programming"
print("Length:", len(word))


# 4. String concatenation
first_name = "Nagarjun"
last_name = "TK"
full_name = first_name + " " + last_name
print(full_name)


# 5. Uppercase and lowercase
msg = "Hello Python"
print(msg.upper())
print(msg.lower())


# 6. Check word in string
sentence = "I am learning Python"
print("Python" in sentence)


# 7. Reverse a string
text = "Python"
print(text[::-1])


# 8. Count character occurrence
word = "banana"
print(word.count("a"))


# 9. Replace word
sentence = "I love Java"
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)


# 10. f-string example
name = "Nagarjun"
age = 21
print(f"My name is {name} and I am {age} years old")
