# def number_to_string(num):
#     return str(num)
# test_num = 123
# print(type(number_to_string(test_num)))

# def multiplication_of_elements(arr, n):     # define the function, arguments passed are actual array and n(# elements)
#     product = 1                             # initialize variable to hold the result
#     for x in range(n):                      # for loop that runs through elements in array
#         product = product * arr[x]          # in the result variable store logic for 1 * each element of the array
#     return product                          # stop function
#
#
# arr = [1,2,3,4]                             # actual array
# n = len(arr)                                # defining n = number of elements in the array
# print(multiplication_of_elements(arr, n))   # show the result, calling the function with arguments values.
#
# # Also valid
# def grow(arr):
#     product = 1
#     for x in range(len(arr)):
#         product = product * arr[x]
#     return product
#
# arr = [1,2,3,4]
# print(grow(arr))

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
# def simple_multiplication(number):
#     product = 1
#     if number % 2 == 0:
#         product = number * 8
#     else:
#         product = number * 9
#     return product
#
#
# number = 10
# print(simple_multiplication(number))

# You were camping with your friends far away from home, but when it's time to go back,
# you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
#
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#
# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= 50 and mpg >= 25 and fuel_left >= 2:
        we_can_make_it = True
    else:
        we_can_make_it = False
    return we_can_make_it


distance_to_pump = 50
mpg = 25
fuel_left = 2
print(zero_fuel(distance_to_pump,mpg, fuel_left))