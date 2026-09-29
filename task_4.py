# Given list of strings
strings = ["hello", "world", "python"]

# Convert each string into a list of characters using map()
list_of_lists = list(map(list, strings))

print("Original list of strings:")
print(strings)

print("\nList of lists:")
print(list_of_lists)