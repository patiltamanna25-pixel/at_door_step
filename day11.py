#Write a recursive function to find sum of first n numbers
def sum_of_n(n):
    # Base condition: to stop the recursion
    if n <= 1:
        return 1
    else:
        # Recursive call: n + sum of (n-1)
        return n + sum_of_n(n - 1)

# Example Usage:
number = 4
result = sum_of_n(number)
print(f"The sum of the first {number} numbers is: {result}")
#Write a recursive function to count digits of a number
def count_digits(n):
    if n<10:
        return 1
    else:
        return 1 + count_digits(n // 10)
print(count_digits(3000))


