# Original list of dictionaries
original_list = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sort the list of dictionaries by the 'color' key using a lambda
sorted_list = sorted(original_list, key=lambda d: d['color'])

print("Original list of dictionaries:")
print(original_list)

print("\nSorting the List of dictionaries:")
print(sorted_list)