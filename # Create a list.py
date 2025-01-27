# Create a list
my_list = [1, 3, 5, 7, 9]

# Add an element
my_list.append(11)
print("After appending 11:", my_list)

# Remove an element
my_list.remove(3)
print("After removing 3:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Find the sum of elements in the list
list_sum = sum(my_list)
print("Sum of list elements:", list_sum)

# Create strings
str1 = "Hello"
str2 = "World"

# Concatenate strings
concat_str = str1 + " " + str2
print("Concatenated string:", concat_str)

# Convert to uppercase
upper_str = str1.upper()
print("Uppercase string:", upper_str)

# Convert to lowercase
lower_str = str2.lower()
print("Lowercase string:", lower_str)

# Check if a substring exists
substring = "ello"
if substring in str1:
    print(f"'{substring}' exists in '{str1}'")

# Count occurrences of a character
char_count = str1.count('l')
print("Occurrences of 'l' in str1:", char_count)




# Define two numbers
num1 = 10
num2 = 3

# Basic calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
exponentiation = num1 ** num2
floor_division = num1 // num2
modulus = num1 % num2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Exponentiation: {exponentiation}")
print(f"Floor division: {floor_division}")
print(f"Modulus: {modulus}")


# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)


# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to filter odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)


