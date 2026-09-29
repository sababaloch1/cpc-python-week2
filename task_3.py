def sum_and_average_digits(s1):
    # Extract all digit characters and convert them to integers
    digits = [int(ch) for ch in s1 if ch in "0123456789"]

    if not digits:
        return 0, 0.0  # no digits found

    total = sum(digits)
    average = total / len(digits)

    return total, average


# Example usage
s1 = "a1b2c3d4"
total, average = sum_and_average_digits(s1)

print("Sum of digits:", total)
print("Average of digits:", average)