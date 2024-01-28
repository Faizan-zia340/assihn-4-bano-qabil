def sum_of_numbers(numbers):
    total = sum(numbers)
    return total

# Example usage:
n =int(input("enter n numbers"))
user_numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]

result = sum_of_numbers(user_numbers)

print(f"Sum of {n} numbers entered by the user: {result}")
