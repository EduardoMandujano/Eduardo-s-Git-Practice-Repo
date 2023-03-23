# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
# Algorithm 1, Solution 1
import statistics


first_test_list = [1, 3, 5, 6, 4, 10, 2, 3]         # given list
arith_mean = statistics.mean(first_test_list)       # imported from statistics library the arithmetical mean function
new_list = []                                       # empty list that will contain the numbers meeting the condition
for x in first_test_list:                           # loops through all numbers in list
    if arith_mean > x:                              # compares numbers to the arithmetic mean
        new_list.append(x)                          # adds qualifying numbers to new_list
print(new_list)                                     # shows the result


# Algorithm 1, Solution 2
def elements_below_mean(first_test_list):             # defining the function
    resulting_numbers = []                            # empty list that will contain numbers meeting the condition
    arith_mean = statistics.mean(first_test_list)     # variable that contains the arithmetical mean
    for x in first_test_list:                         # loops through numbers in list
        if arith_mean > x:                            # determines if the listed number is lesser than arith_mean
            resulting_numbers.append(x)               # adds qualifying number to resulting_numbers list
    return resulting_numbers                          # stops execution of current function


first_test_list = [1, 3, 5, 6, 4, 10, 2, 3]           # list that tests the functionality of the function
print(elements_below_mean(first_test_list))           # prints the result


# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

# Algorithm 2, Solution 1
second_test_list = [15, 3, 7, 5, 12, 7, 8, 9, 3]        # given list
second_test_list.sort()                                 # sort numbers in the list
print(second_test_list)                                 # verification of sorting
lower_two = second_test_list[0:2]                       # printing the lower two numbers of the list (solution)
print(lower_two)                                        # printing the solution

# Algorithm 2, Solution 2 with function
def lowest_elements(second_test_list):              # defining the function
    new_listing = []                                # creating a variable for an empty list to hold the sorted values
    new_listing.append(min(second_test_list))       # adds smallest number of list to new_listing variable
    to_be_removed = min(second_test_list)           # saving smallest number, so it can be removed from second_test_list
    element_count = second_test_list.count(to_be_removed)   # counts element to_be_removed
    for i in range(element_count):                  # looping once
        second_test_list.remove(to_be_removed)      # removing smallest element from list to find a new smallest element
        new_listing.append(min(second_test_list))   # adds the following smallest number to new_listing variable
        return new_listing                          # stops execution of current function


second_test_list = [15, 3, 7, 5, 12, 7, 8, 9]       # list that tests the functionality of the function
print(lowest_elements(second_test_list))            # prints the result
