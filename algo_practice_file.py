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
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump <= 50 and mpg >= 25 and fuel_left >= 2:
#         we_can_make_it = True
#     else:
#         we_can_make_it = False
#     return we_can_make_it
#
#
# distance_to_pump = 50
# mpg = 25
# fuel_left = 2
# print(zero_fuel(distance_to_pump,mpg, fuel_left))


# def set_alarm(employed, vacation):
#     if employed == True and vacation == False:
#         ring_ring = True
#     else:
#         ring_ring = False
#     return ring_ring
#
# employed = True
# vacation = False
# print(set_alarm(employed, vacation))
#
#
# def remove_chars(str):
#     return str[1 :-1]
#
#
# str = "Queretaro"
# print(remove_chars(str))
#
#
# def reverse_seq(n):                     # defining function with number
#     resulting_sequence = []             # empty array to hold the result
#     for i in range(n):                  # for loop that for the range of n will append the number to array
#         resulting_sequence.append(n)
#         n -= 1                          # goes in descending order
#     return resulting_sequence           # stop function and return the result
#
#
# n = 5
# print(reverse_seq(n))

# def count_sheeps(sheep):
#     return sheep.count(True)
#
#
# sheep = [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# print(count_sheeps(sheep))
#
#
# def boolean_to_string(b):
#     return str(b)
#
# b = True
# print(boolean_to_string(b))


# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


# def count_positives_sum_negatives(arr):
#     if arr is None or len(arr) == 0:
#         return []
#
#     count = 0
#     neg_sum = 0
#
#     for i in arr:
#         if i > 0:
#             count += 1
#         elif i < 0:
#             neg_sum += i
#     return [count, neg_sum]
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# print(count_positives_sum_negatives(arr))


# Write a function which converts the input string to uppercase
# def make_upper_case(str):
#     print(str)
#     return str.upper()
#
#
# str = "tacos"
# print(make_upper_case(str))

# def messi_total_goals(laliga, copadelrey, champions):
#     g = 0
#     g = laliga + copadelrey + champions
#     return g
#
#
# laliga = 5
# copadelrey = 10
# champions = 2

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# def two_ints(a, b):
#     if not a:
#         a = "0"
#     if not b:
#         b = "0"
#     output_sum = int(a) + int(b)
#     return str(output_sum)
#
#
# a = ''
# b = '9'
# print(two_ints(a, b))

# Complete the solution so that it reverses the string passed into it.

# def solution(string):
#     return string[::-1]
#
#
# string = "word"
# print(solution(string))
#
# # Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
#
#
# def bool_to_word(boolean):
#     string = ""
#     if boolean == True:
#         string = "Yes"
#     elif boolean == False:
#         string = "No"
#     return string
#
# boolean = False
# print(bool_to_word(boolean))


# Make a function that will return a greeting statement that uses an input; your program should
# return, "Hello, <name> how are you doing today?".

# def greet(name):
#     return "Hello, " + name + " how are you doing today?"
#
#
# print(greet("John"))

# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.
#
# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);
#
# This function should return a number (final grade). There are four types of final grades:
#
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases
# def final_grade(exam, projects):
#     if exam > 90 or projects > 10:
#         result = 100
#     elif exam > 75 and projects >= 5:
#         result = 90
#     elif exam > 50 and projects >= 2:
#         result = 75
#     else:
#         result = 0
#     return result
#
#
# exam = 55
# projects = 0
# print(final_grade(exam, projects))

# Given a list of integers, determine whether the sum of its elements is odd or even.
#
# Give your answer as a string matching "odd" or "even".
#
# If the input array is empty consider it as: [0] (array with a zero).

# def odd_or_even(arr):
#     if len(arr) == 0:
#         return "even"
#     else:
#         if sum(arr) % 2 == 0:
#             return "even"
#         else:
#             return "odd"
#
#
# arr = [0, 1, 4, 1]
# print(odd_or_even(arr))

# Given an integral number, determine if it's a square number:


# def is_square(n):
#     if n < 0:
#         return False
#     i = 0
#     while i*i <= n:
#         if i*i == n:
#             return True
#         i += 1
#     return False
#
# n = 25
# print(is_square(n))


# Write a function that returns both the minimum and maximum number of the given list/array.


# def min_max(lst):
#     min_num = lst[0]
#     max_num = lst[0]
#     for num in lst:
#         if num < min_num:
#             min_num = num
#         if num > max_num:
#             max_num = num
#     return [min_num, max_num]
#
#
# lst = [1, 5]
# print(min_max(lst))

# Write a program where Alex can input (n) how many times the hoop goes round
# and it will return him an encouraging message :)
#
# If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# If he doesn't get 10 hoops, return the string "Keep at it until you get it".

# def hoop_count(n):
#     if n >= 10:
#         return "Great, now move on to tricks"
#     else:
#         return "Keep at it until you get it"
#
#
# n = 1
# print(hoop_count(n))


# All of the animals are having a feast! Each animal is bringing one dish. There is just one rule:
# the dish must start and end with the same letters as the animal's name. For example,
# the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
#
# Write a function feast that takes the animal's name and dish as arguments
# and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.
#
# Assume that beast and dish are always lowercase strings,
# and that each has at least two letters. beast and dish may contain hyphens and spaces,
# but these will not appear at the beginning or end of the string. They will not contain numerals.

# def feast(beast, dish):
#     if beast[0] == dish[0] and beast[-1] == dish[-1]:
#         return True
#     else:
#         return False
#
#
# beast = "brown bear"
# dish = "bear claw"
# print(feast(beast, dish))


# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"


# def bmi(weight, height):
#     result = weight / pow(height, 2)
#     if result <= 18.5:
#         return "Underweight"
#     elif result <= 25:
#         return "Normal"
#     elif result <= 30:
#         return "Overweight"
#     else:
#         return "Obese"
#
#
# weight = 110
# height = 1.80
# print(bmi(weight, height))


# Bob needs a fast way to calculate the volume of a cuboid with three values:
# the length, width and height of the cuboid.
# Write a function to help Bob with this calculation.
# def get_volume_of_cuboid(length, width, height):
#     result = length * width * height
#     return result
#
#
# print(get_volume_of_cuboid(2, 3, 4,))

#
# Create a function that accepts a string and a single character,
# and returns an integer of the count of occurrences the 2nd argument is found in the first one.
#
# If no occurrences can be found, a count of 0 should be returned.


# def str_count(strng, letter):
#     count = 0
#     for i in strng:
#         if i == letter:
#             count += 1
#     return count
#
#
# strng = "starbucks"
# letter = "s"
# print(str_count(strng, letter))


# def are_you_playing_banjo(name):
#     if name[0] == "R" or name [0] =="r":
#         name = name + " plays banjo"
#     else:
#         name = name + " does not play banjo"
#     return name
#
#
# name = "Robert"
# print(are_you_playing_banjo(name))


# def add_binary(a,b):
#     sum = a + b
#     return bin(sum)[2:]
#
#
# print(add_binary(2,3))


# def stray(arr):
#     for s in arr:
#         if arr.count(s) == 1:
#             return s
#
#
# arr = [17, 17, 3, 17, 17, 17, 17]
# print(stray(arr))


# def square(n):
#     n = n*n
#     return n
#
#
# n = 3
# print(square(n))


# def high_and_low(numbers):
#     numbers_list = list(map(int, numbers.split()))
#     highest = max(numbers_list)
#     lowest = min(numbers_list)
#     numbers = f'{highest} {lowest}'
#     return numbers
#
#
# numbers = ("1 2 3 4 5")
# print(high_and_low(numbers))
#
#
# def xo(s):
#     if s.lower().count("o") == s.lower().count("x"):
#         return True
#     else:
#         return False
#
#
# s = "xooxx"
# print(xo(s))
#
#
# def say_hello(name):
#     return "Hello, " + name
#
#
# name = "Mr. Spock"
# print(say_hello(name))
#
#
# def maps(a):
#    return [v*2 for v in a]
#
#
# a = [1, 2, 3]
# print(maps(a))
#
#
# def double_char(s):
#     result_s = ""
#     for char in s:
#         result_s += char*2
#     return result_s
#
#
# s = "Hello!"
# print(double_char(s))
#
#
# def unusual_five()
#     return len("hacker")
#
# print(unusual_five())


# def square_sum(numbers):
#     return sum(x*x for x in numbers)
#
#
# numbers = [1, 2, 2]
# print(square_sum(numbers))
#
#
# def string_to_number(s):
#     s = int(s)
#     return s
#
#
# s = "1234"
# print(string_to_number(s))


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# n = 3
# print(is_even(n))
#

# def summation(num):
#     result = 0
#     for i in range(1, num+1):
#         result += i
#     return result
#
#
# num = 8
# print(summation(num))


# def square_digits(num):
#     num_string = str(num)
#     result = ""
#     for i in num_string:
#         result += str((int(i)**2))
#     return int(result)
#
#
# num = 9119
# print(square_digits(num))


# def count_by(x, n):
#     result = []
#     i = x
#     while i <= n:
#         result.append(i)
#         i += x
#     return result
#
#
# print(count_by(1, 10))
#
#
# def greet(xo):
#     return xo
#
#
# xo = "hello world!"
# print(greet(xo))
#
#
# def greet():
#     return "hello world!"
#
#
# print(greet())
#
#
# def reverse_words(text):
#     words = text.split()
#     reversed_words = []
#     for i in words:
#         reversed_word = i[::-1]
#         reversed_words.append(reversed_word)
#     return "  ".join(reversed_words)
#
#
# text = "This is an example!"
# print(reverse_words(text))
#
#
# def is_triangle(a, b, c):
#     if a+b > c and a+c > b and b+c > a:
#         return True
#     else:
#         return False

# def find_multiples(integer, limit):
#     result = []
#     for i in range(integer, limit+1, integer):
#         result.append(i)
#     return result
#
#
# integer = 2
# limit = 10
# print(find_multiples(integer, limit))
#
#
# def validate_pin(pin):
#     if pin.isdigit() and len(pin) == 4 or len(pin) == 6:
#         return True
#     else:
#         return False
#
#
# pin = "-12345"
# print(validate_pin(pin))


# def lovefunc( flower1, flower2 ):
#     if flower1 % 2 == 0 and flower2 % 2 != 0 or flower1 % 2 != 0 and flower2 % 2 == 0:
#         return True
#     else:
#         return False
#
#
# flower1 = 2
# flower2 = 2
# print(lovefunc(flower1,flower2))


def make_negative(number):
    if number > 0:
        return number * (-1)
    if number <= 0:
        return number


number = 0
print(make_negative(number))


def digitize(n):
    reversed_array = []
    for i in str(n):
        reversed_array.insert(0, int(i))
    return reversed_array

n = 0
print(digitize(n))


def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


name = "Gus"
owner = "Gus"
print(greet(name, owner))

