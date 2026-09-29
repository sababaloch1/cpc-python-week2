def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda t: t[-1])

# Sample list
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort by the last element of each tuple
result = sort_by_last_element(sample_list)

print("Original list:", sample_list)
print("Sorted result:", result)