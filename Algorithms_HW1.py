# 1. Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# 1. Version 1
number = int(input("Enter a number: "))
sum_a = 0
for i in range(1, number + 1):
    sum_a = sum_a + i
print('The sum is: ', sum_a)


# 1. Version 2
def sum_of_digits_from_1_to_n(n: int):
    sum_b = 0
    for i in range(1, n + 1):
        sum_b = sum_b + i
    print('The sum is: ', sum_b)


sum_of_digits_from_1_to_n(17)

# 2. Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.


n1 = int(input("Enter a number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number number: "))
if n1 > n2 and n1 > n3:
    print('The Max Number of the three is: ', n1)
elif n2 > n1 and n2 > n3:
    print('The Max Number of the three is: ', n2)
elif n3 > n1 and n3 > n2:
    print('The Max Number of the three is: ', n3)


# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


numbers = input('Enter a number: ')
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
odd_numbers_count = 0
even_numbers_count = 0
for x in numbers:
    if not int(x) % 2:
        even_numbers_count += 1
    else:
        odd_numbers_count += 1

print('Number of odd numbers: ', odd_numbers_count)
print('Number of even numbers: ', even_numbers_count)


# end
