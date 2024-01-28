def count_unique_values(input_list):
    unique_values = set(input_list)
    count_dict = {value: input_list.count(value) for value in unique_values}

    return count_dict

# Example usage:
my_list = [1, 2,2, 3, 4, 1, 2, 3, 5, 6, 7, 8, 9, 9, 8, 7]
result = count_unique_values(my_list)

print("Original List:", my_list)
print("Count of unique values:", result)
