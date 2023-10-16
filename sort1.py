# Ask the user for the size of the list
size = int(input("Enter the size of the list: "))

# Initialize an empty list
numbers = []

# Get input for the specified number of elements
for i in range(size):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted list
print("Sorted numbers in ascending order:", sorted_numbers)

# Sort the list in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)

# Print the sorted list in descending order
print("Sorted numbers in descending order:", sorted_numbers_desc)
