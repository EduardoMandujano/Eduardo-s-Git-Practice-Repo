# 1. Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def evens_are_first(listing):                   # defining the functions, passing array listing as an argument
    array_index = 0                             # variable that defines an index position in the array
    for x in range(len(listing)):               # loop looping through all numbers inside the array
        if listing[array_index] % 2 != 0:       # modulus sorts out which numbers are odd
            temporary_odd_value = listing[array_index]  # defining temp value so that we don't lose the value while swap
            listing.remove(listing[array_index])    # removing odd value from array
            listing.append(temporary_odd_value)     # appending odd value at the end of array
        else:                                   # if number in the array is even, this block will activate
            array_index += 1                    # if the number is even, we move on, it remains in place in the array
    return listing                              # stops executing current function


listing = [7, 3, 5, 6, 4, 10, 3, 2]             # array from the description
print(evens_are_first(listing))                 # shows the solution


# 2. Increment a Number
# Write a program that takes as input a list of digits encoding a non-negative decimal integer D,
# and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def increment_a_number(encoded_integer):        # defining the function, passing array encoded_integer as argument
    string_variable = ''                        # empty variable that initializes an  empty string character
    for y in encoded_integer:                   # loops through all elements of the array
        string_variable += str(y)               # empty variable stores the looped elements of the array as a string
        variable_plus_one = int(string_variable) + 1    # turns the string into an int and adds 1 (D+1)
        results_list = list(map(int, str(variable_plus_one)))   # map function converts a number to a list of integers
    return results_list                         # stops executing the current function


encoded_integer = [1, 2, 9]                     # test list given in the instructions
print(increment_a_number(encoded_integer))      # shows the solution
