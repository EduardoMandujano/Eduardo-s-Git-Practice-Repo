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
#
#
# def make_negative(number):
#     if number > 0:
#         return number * (-1)
#     if number <= 0:
#         return number
#
#
# number = 0
# print(make_negative(number))
#
#
# def digitize(n):
#     reversed_array = []
#     for i in str(n):
#         reversed_array.insert(0, int(i))
#     return reversed_array
#
# n = 0
# print(digitize(n))
#
#
# def greet(name, owner):
#     if name == owner:
#         return "Hello boss"
#     else:
#         return "Hello guest"
#
#
# name = "Gus"
# owner = "Gus"
# print(greet(name, owner))
#
#
# def minimum(arr):
#     return min(arr)
#
#
# def maximum(arr):
#     return max(arr)
#
#
# arr = [4, 6, 2, 1, 9, 63, -134, 566]
# print(minimum(arr))
# print(maximum(arr))
#
#
# def likes(names):
#     if len(names) == 1:
#         return names[0] + " likes this"
#     elif len(names) == 2:
#         return names[0] + " and " + names[1] + " like this"
#     elif len(names) == 3:
#         return names[0] + ", " + names[1] + " and " + names[2] + " like this"
#     elif len(names) == 4:
#         return names[0] + ", " + names[1] + " and 2 others" + " like this"
#     elif len(names) == 5:
#         return names[0] + ", " + names[1] + " and 3 others" + " like this"
#     elif names == []:
#         return "no one likes this"
#
#
# names = ["Peter", "Jacob", "Max", "Mark"]
# print(likes(names))
#
#
# def likes(names):
#     n = len(names)
#     if n == 0:
#         return "no one likes this"
#     elif n == 1:
#         return f"{names[0]} likes this"
#     elif n == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif n == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {n-2} others like this"
#

# def is_pangram(s):
#     alphabet = set("abcdefghijklmnopqrstuvwxyz")
#     return set(s.lower()) >= alphabet
#
#
# s = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(s))


# def sum_two_smallest_numbers(numbers):
#     sorted_list = sorted(numbers)
#     sum = sorted_list[0] + sorted_list[1]
#     return sum
#
#
# numbers = [19, 5, 42, 2, 77]
# print(sum_two_smallest_numbers(numbers))


# def filter_list(l):                         # define function with argument l for list
#     resulting_list = []                     # create empty list that will hold the result
#     for item in l:                          # for loop iterates for every item on the l list
#         if isinstance(item, int):           # check to see if each item is an integer, returns true if it is
#             resulting_list.append(item)     # if it returns true, appends the item to the resulting list
#     return resulting_list                   # returns resulting list results
#
#
# l = [1, 2, 'a','b']
# print(filter_list(l))
#
#
# def dna_to_rna(dna):
#     return dna.replace("T", "U")
#
#
# dna = "GCAT"
# print(dna_to_rna(dna))
#
#
# def string_to_array(s):
#     array = []
#     array = s.split(" ")
#     return array
#
#
# s = "I love arrays they are my favorite"
# print(string_to_array(s))
#
#
# def solution(s):
#     result = ""
#     for i in s:
#         if i.isupper():
#             result += " " + i
#         else:
#             result += i
#     return result
#
#
# s = "camelCasing"
# print(solution(s))


# def find_smallest_int(arr):
#     return min(arr)
#
#
# arr = [34, 15, 88, 2]
# print(find_smallest_int(arr))
#
#
# def cockroach_speed(s):
#     result = s * 100000 // 3600
#     return int(result)
#
#
# s = 1.08
# print(cockroach_speed(s))


# def even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
#
# number = 3
# print(even_or_odd(number))
#
#
# def get_middle(s):
#     length = len(s)
#     resulting_char = 0
#     actual_char = ""
#     if length % 2 != 0:
#         resulting_char = int(length // 2)
#         actual_char = s[resulting_char]
#     elif length % 2 == 0:
#         resulting_char = int(length // 2)
#         actual_char = s[resulting_char - 1:resulting_char + 1]
#
#     return actual_char
#
#
# s = "test"
# print(get_middle(s))


# def fake_bin(x):
#     resulting_string = ""
#     for i in x:
#         if int(i) < 5:
#             resulting_string += "0"
#         else:
#             resulting_string += "1"
#     return resulting_string
#
# x = "1234567890"
# print(fake_bin(x))
#
#
# def number(lines):
#     numbered_lines = []
#     for i, line in enumerate(lines, start=1):
#         numbered_line = f"{i}: {line}"
#         numbered_lines.append(numbered_line)
#     return numbered_lines
#
#
# lines = ["a", "b", "c"]
# print(number(lines))
#
#
# def get_count(sentence):
#     result_1 = int(sentence.count("a", "e", "i"))
#     result_2 = int(sentence.count("o", "u"))
#     final_result = result_1 + result_2
#     return final_result
#
#
# sentence = "aeiouy"
# print(get_count(sentence))


# def open_or_senior(data):
#     category = []
#     for member in data:
#         age, handicap = member
#         if age >= 55 and handicap > 7:
#             category.append("Senior")
#         else:
#             category.append("Open")
#     return category
#
#
# data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# print(open_or_senior(data))


# def get_age(age):
#     parsed_age = int(age[0])
#     return parsed_age
#
#
# age = "9 years old"
# print(get_age(age))
#
#
# def correct(s):
#     if "0" in s:
#         s = s.replace("0", "O")
#     if "1" in s:
#         s = s.replace("1", "I")
#     if "5" in s:
#         s = s.replace("5", "S")
#     return s
#
#
# s = "L0ND0N DUBL1N 51NGAP0RE"
# print(correct(s))

# def solution(text, ending):
#     return text.endswith(ending)
#
#
# print(solution("abc", "bc"))
# print(solution("abc", "d"))
#
#
# def multiple_of_index(arr):
#     new_array = []
#     for i in range(1, len(arr)):
#         if (arr[1] % i == 0):
#             new_array.append(arr[i])
#     return new_array
#
#
# arr = [22,-6, 32, 82, 9, 25]
# print(multiple_of_index(arr))
#
#
# import math
# def find_next_square(sq):
#     result = math.sqrt(sq)
#     if result.is_integer():
#         return (result + 1) * (result + 1)
#     else:
#         return -1
#
#
# sq = 121
# print(find_next_square(sq))
#
#
# def switch_it_up(number):
#     if number == 0:
#         return "Zero"
#     elif number == 1:
#         return "One"
#     elif number == 2:
#         return "Two"
#     elif number == 3:
#         return "Three"
#     elif number == 4:
#         return "Four"
#     elif number == 5:
#         return "Five"
#     elif number == 6:
#         return "Six"
#     elif number == 7:
#         return "Seven"
#     elif number == 8:
#         return "Eight"
#     elif number == 9:
#         return "Nine"
#
# number = 0
# print(switch_it_up(number))
#
#
# def hero(bullets, dragons):
#     if bullets >= (dragons * 2):
#         return True
#     else:
#         return False
#
# bullets = 1
# dragons = 1
# print(hero(bullets, dragons))


# def paperwork(n, m):
#     pages_needed = 0
#     if n > 0 and m > 0:
#         pages_needed = n * m
#     if n < 0 or m < 0:
#         pages_needed = 0
#     return pages_needed
#
#
# n = -5
# m = 5
# print(paperwork(n, m))
#
#
# def find_short(s):
#     words = s.split()
#     shortest_length = 100
#     for word in words:
#         if len(word) < shortest_length:
#             shortest_length = len(word)
#     return shortest_length
#
#
# s = "el conde de parangaricutirimicuaro"
# print(find_short(s))
#
#
# def sum_array(arr):
#     output = 0
#     for numbers in arr:
#         output += numbers
#     return output
#
#
# arr = [1, 5.2, 4 , 0, -1]
# print(sum_array(arr))
#
#
# def check_for_factor(base, factor):
#     if base % factor == 0:
#         return True
#     else:
#         return False
#
# base = 9
# factor = 2
# print(check_for_factor(base, factor))
#
#
# def get_sum(a,b):
#     output = 0
#     if a == b:
#         output = a
#     if a != b:
#         output = (a) + (b)
#     return output
#
#
# a = -1
# b = 0
# print(get_sum(a, b))


# def step(x, y):
#     result = 0
#     return y - x
#
#
# x = 45
# y = 48
# print(step(x,y))
#
#
# def problem(a):
#     if type(a) == int:
#         return (a * 50) + 6
#     else:
#         return "Error"
#
# a = 10
# print(problem(a))
#
#
# def twice_as_old(dad_years_old, son_years_old):
#     result = (dad_years_old - (2 * son_years_old))
#     if result < 0:
#         result = (dad_years_old - (2 * son_years_old)) * -1
#     return result
#
#
#
# dad_years_old = 36
# son_years_old = 7
# print(twice_as_old(dad_years_old, son_years_old))
#
#
# def plural(n):
#     if n == 0 or n > 1:
#         return True
#     else:
#         return False
#
# n = 0
# print(plural(n))


# def multiply(a, b):
#     result = a * b
#     return result
#
#
# a = 2
# b = 3
# print(multiply(a, b))
#
#
# def between(a,b):
#     result_array = []
#     for i in range(a, b+1):
#         result_array.append(i)
#     return result_array
#
#
#
# a = 1
# b = 4
# print(between(a, b))
#
#
# def repeat_str(repeat, string):
#     return repeat * string
#
#
# repeat = 4
# string = "Hello"
# print(repeat_str(repeat, string))


# def find_needle(haystack):
#     for needle in haystack:
#         if needle == "needle":
#             return "found the needle at position " + str(haystack.index("needle"))
#
#
# haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# print(find_needle(haystack))
#
#
# def check(seq, elem):
#     return elem in seq
#
#
# seq = [1, 2, 3, 4, 0]
# elem = 0
# print(check(seq, elem))


# def wave(people):
#     wave_array = []
#     for person in range(len(people)):
#         if people[person].isspace():
#             continue
#         wave_array.append(people[:person] + people[person].upper() + people[person+1:])
#     return wave_array
#
#
# people = "hello"
# print(wave(people))
#
#
# def move(position, roll):
#     result = (2 * roll) + position
#     return result
#
#
# position = 3
# roll = 6
# print(move(position, roll))


# def opposite(number):
#     return number * (-1)
#
#
# number = -34
# print(opposite(number))
#
#
# def round_to_next5(n):
#     if n % 5 == 0:
#         return n
#     else:
#         return n + (5 - (n % 5))
#
#
# n = 7
# print(round_to_next5(n))
#
#
# def powers_of_two(n):
#     return [2 ** i for i in range(n+1)]
#
# n = 5
# print(powers_of_two(n))
#
#
# def century(year):
#     return (year + 99) // 100
#
#
# year = 89
# print(century(year))


# def to_jaden_case(string):
#     # jaden_cased_string = ' '.join(word.capitalize() for word in string.split())
#     # return jaden_cased_string
#     result = ""
#     for word in string.split():
#         result += word.capitalize() + " "
#     return result
#
#
# string = "How can mirrors be real if our eyes aren't real"
# print(to_jaden_case(string))


# def even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     elif number % 2 != 0:
#         return "Odd"
#
#
# number = 0
# print(even_or_odd(number))
#
#
# def get_count(sentence):
#     total = 0
#     vowels = "aeiou"
#     for vowel in sentence:
#         if vowel in vowels:
#             total += 1
#     return total
#
#
#
# sentence = "aeiou"
# print(get_count(sentence))


# def opposite(number):
#     return number * (-1)
#
#
# number = -14
# print(opposite(number))
#
#
# def number_to_string(num):
#     return str(num)
#
# num = 123
# print(number_to_string(num))
#
#
# def solution(string):
#     result = ""
#     for i in range(len(string)-1, -1, -1):
#         result += string[i]
#     return result
#
#
# string = "world"
# print(solution(string))


# def reverse_list(l):
#     # l.reverse()
#     # return l
#    return l[::-1]
#
#
# l = [1, 2, 3, 4]
# print(reverse_list(l))
#
#
# def get_real_floor(n):
#     if n >= 1 and n < 13:
#         return n-1
#     elif n <= 0:
#         return n
#     elif n == 13:
#         return None
#     elif n >= 14:
#         return n-2
#
#
# n = 13
# print(get_real_floor(n))
#
#
# def find_difference(a, b):
#     cuboid_a = 1
#     cuboid_b = 1
#     for i in a:
#         cuboid_a *= i
#     for i in b:
#         cuboid_b *= i
#     if (cuboid_a - cuboid_b) < 0:
#         return (cuboid_a - cuboid_b) * -1
#     else:
#         return cuboid_a - cuboid_b
#
#
# a = [2, 2, 3]
# b = [5, 4, 1]
# print(find_difference(a, b))


# def capitals(word):
#     resulting_list = []
#     for i in range(len(word)):
#         if word[i].isupper():
#             resulting_list.append(i)
#     return resulting_list
#
# word = "CodEWaRs"
# print(capitals(word))
#
#
# def litres(time):
#     return int((time * 0.5) / 1)
#
# time = 11.8
# print(litres(time))


# def descending_order(num):
#     stringed_num = str(num)
#     listed_num = sorted(stringed_num, reverse=True)
#     result = int("".join(listed_num))
#     return result
#
#
# num = 42145
# print(descending_order(num))


# def positive_sum(arr):
#     positive_numbers = []
#     for pos in arr:
#         if pos > 0:
#             positive_numbers.append(pos)
#     return sum(positive_numbers)
#
#
# arr = [1, -4, 7, 12]
# print(positive_sum(arr))


# def arithmetic(a, b, operator):
#     result = 1
#     if operator == "add":
#         return a + b
#     elif operator == "subtract":
#         return a - b
#     elif operator == "multiply":
#         return a * b
#     elif operator == "divide":
#         return a / b
#     return result
#
#
# a = 5
# b = 2
# operator = "divide"
# print(arithmetic(a, b, operator))


# def rental_car_cost(d):
#     per_day = 40
#     total_cost = d * per_day
#     if d >= 7:
#         total_cost = (d * per_day) - 50
#     elif d >= 3:
#         total_cost = (d * per_day) - 20
#     return total_cost
#
# d = 3
# print(rental_car_cost(d))


# def is_palindrome(s):
#     lower_s = s.lower()
#     if len(lower_s) == 1:
#         return True
#     elif lower_s[0] == lower_s[-1] and lower_s[1] == lower_s[-2] and lower_s[2] == lower_s[-3]:
#         return True
#     else:
#         return False
#
#
# s = "Abba"
# print(is_palindrome(s))


# def count_smileys(arr):
#     valid_smileys = [":)", ":D", ";)", ";D", ":-)", ":-D", ";-)", ";-D", ":~)", ":~D", ";~)", ";~D"]
#     count = 0
#     for face in arr:
#         if face in valid_smileys:
#             count += 1
#     return count
#
#
# arr = [";)", ";(", ";}", ";-D"]
# print(count_smileys(arr))


# def disemvowel(string_):
#     new_string = ""
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     for v in string_:
#         if v not in vowels:
#             new_string += v
#     return new_string
#
#
# string_ = "This website is for losers LOL!"
# print(disemvowel(string_))


# def friend(x):
#     friends = []
#     for fr in x:
#         if len(fr) == 4:
#             friends.append(fr)
#     return friends
#
#
# x = ["Ryan", "Kieran", "Mark"]
# print(friend(x))
#
#
# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     elif (p1 == "scissors" and p2 == "paper") or (p1 == "rock" and p2 == "scissors") or ((p1 == "paper" and p2 == "rock")):
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"
#
#
# p1 = "rock"
# p2 = "paper"
# print(rps(p1, p2))
#
#
# def double_integer(i):
#     return 2 * i
#
#
# i = 47
# print(double_integer(i))


# def people_with_age_drink(age):
#     resulting_drink = ""
#     if age < 14:
#         resulting_drink = "drink toddy"
#     elif 14 <= age < 18:
#         resulting_drink = "drink coke"
#     elif 18 <= age < 21:
#         resulting_drink = "drink beer"
#     else:
#         resulting_drink = "drink whisky"
#     return resulting_drink
#
# age = 14
# print(people_with_age_drink(age))


# def printer_error(s):
#     total_errors = sum(1 for character in s if character not in 'abcdefghijklm')
#     return F"{total_errors}/{len(s)}"
#
# s = "aaaxbbbbyyhwawiwjjjwwm"
# print(printer_error(s))


# def sort_by_length(arr):
#     return sorted(arr, key=len)
#
#
# arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]
# print(sort_by_length(arr))


# def is_isogram(string):
#     lower_string = string.lower()
#     seen_letters = set()
#     for char in lower_string:
#         if char in seen_letters:
#             return False
#         else:
#             seen_letters.add(char)
#             return True
#
#
# string = "mouse"
# print(is_isogram(string))


# def name_shuffler(str_):
#     split_string = str_.rsplit(" ")
#     result = " ".join(split_string[::-1])
#     return result
#
#
# str_ = "Troy McLure"
# print(name_shuffler(str_))


# def find_average(numbers):
#     if numbers == []:
#         return 0
#     else:
#         return sum(numbers)/len(numbers)
#
#
# numbers = [1, 2, 3, 4]
# # numbers = []
# print(find_average(numbers))
#
#
# def how_much_i_love_you(nb_petals):
#     if nb_petals == 1:
#         return "I love you"
#     elif nb_petals == 2:
#         return "a little"
#     elif nb_petals == 3:
#         return "a lot"
#     elif nb_petals == 4:
#         return "passionately"
#     elif nb_petals == 5:
#         return "madly"
#     elif nb_petals == 6:
#         return "not at all"
#
# nb_petals = 2
# print(how_much_i_love_you(nb_petals))
#
#
# def better_than_average(class_points, your_points):
#     average = sum(class_points)/len(class_points)
#     if your_points > average:
#         return True
#     else:
#         return False
#
#
# class_points = [100, 40, 34, 57, 29, 72, 57, 88]
# your_points = 56
# print(better_than_average(class_points, your_points))


# def reverse(st):
#     split_st = st.rsplit(" ")
#     resulting_st = " ".join(split_st[::-1])
#     return resulting_st
#
#
# st = "Hello World"
# print(reverse(st))
#
#
# def sum_mix(arr):
#     return sum(int(num) for num in arr)
#
#
# arr = [9, 3, '7', '3']
# print(sum_mix(arr))
#
#
# def add_five(num):
#     total = num + 5
#     return total
#
# num = 5
# print(add_five(num))


# def remove_exclamation_marks(s):
#     mod_string = ""
#     for excl in s:
#         if excl != "!":
#             mod_string += excl
#     return mod_string
# 
# 
# s = "Hello!!! World!!!"
# print(remove_exclamation_marks(s))


# def reverse_letter(string):
#     str_tobe_reversed = ""
#     for s in string:
#         if s.isalpha():
#             str_tobe_reversed += s
#     return str_tobe_reversed[::-1]
#
#
# string = "ultr53o?n"
# print(reverse_letter(string))


# def human_years_cat_years_dog_years(human_years):
#     cat_years_after_2 = ((human_years - 2) * 4) + 24
#     dog_years_after_2 = ((human_years - 2) * 5) + 24
#     if human_years == 1:
#         return [human_years, 15, 15]
#     elif human_years == 2:
#         return [human_years, 24, 24]
#     elif human_years >= 3:
#         return [human_years, cat_years_after_2, dog_years_after_2]
#
#
# human_years = 5
# print(human_years_cat_years_dog_years(human_years))


# def sum_digits(number):
#     number = abs(number)
#     result = 0
#     for n in str(number):
#         result += int(n)
#     return result
#
#
# number = -32
# print(sum_digits(number))
#
#
# def filter_string(string):
#     just_numbers = ""
#     for char in string:
#         if char.isdigit():
#             just_numbers += char
#     return int(just_numbers)
#
#
# string = "a1b2c3"
# print(filter_string(string))
#
#
# def remove_url_anchor(url):
#     list = url.split("#")
#     return list[0]
#
#
# url = "www.codewars.com#about"
# print(remove_url_anchor(url))
#
#
# def smash(words):
#     result = ""
#     for word in words:
#         result += word + " "
#     return result.rstrip()
#
#
# words = ['hello', 'world', 'this', 'is', 'great']
# print(smash(words))


# def alphabet_position(text):
#     text_just_letters = ""
#     for lett in text:
#         if lett.isalpha():
#             text_just_letters += lett.lower()
#
#     letter_numbers = []
#     for num in text_just_letters:
#         letter_numbers.append(str(ord(num) - ord('a') + 1))
#     return " ".join(letter_numbers)
#
#
# text = "The sunset sets at twelve o'clock."
# print(alphabet_position(text))


# def drop_cap(str_):
#     cap_list = str_.title()
#     split_list = cap_list.split()
#     new_list = []
#     for word in split_list:
#         if len(word) <= 2:
#             new_list.append(word.lower())
#         else:
#             new_list.append(word)
#     return " ".join(new_list)
#
#
# str_ = "apple of banana"
# print(drop_cap(str_))


# def divisors(n):
#     list_of_divisors = []
#     for divs in range(1, n + 1):
#         if n % divs == 0:
#             list_of_divisors.append(divs)
#     return len(list_of_divisors)
#
#
# n = 30
# print(divisors(n))


# def two_are_positive(a, b, c):
#     if a >= 0 and b >= 0 and c < 0:
#         return True
#     elif a >= 0 and c >= 0 and b < 0:
#         return True
#     elif b >= 0 and c >= 0 and a < 0:
#         return True
#
#     else:
#         return False
#
#
# print(two_are_positive(4, 6, 0))


# def position(alphabet):
#     letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#     alphabet_index = (letters.index(alphabet)) + 1
#     return "Position of alphabet: " + str(alphabet_index)
#
#
# alphabet = "k"
# print(position(alphabet))
#
#
# def how_many_light_sabers_do_you_own(name):
#     if name == "Zach":
#         return 18
#     if name == "anyone else":
#         return 0
#     else:
#         return 0
#
#
# name = "Zach"
# print(how_many_light_sabers_do_you_own(name))
#
#
# def replace_exclamation(s):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     for i in s:
#         if i in vowels:
#             s = s.replace(i, "!")
#     return s
#
#
# s = "aeiouAEIOU"
# print(replace_exclamation(s))


# def enough(cap, on, wait):
#     if cap >= (on + wait):
#         return 0
#     elif cap < (on + wait):
#         return (on + wait) - cap
#
#
# print(enough(100, 60, 50))
#
#
# def area_or_perimeter(l, w):
#     if l == w:
#         return l * w
#     elif l != w:
#         return (l + w) * 2
#
#
# print(area_or_perimeter(6, 6))
#
#
# def take(arr, n):
#     return arr[0:n]
#
#
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 5
# print(take(arr, n))


# def distinct(seq):
#     resulting_seq = []
#     for num in seq:
#         if num not in resulting_seq:
#             resulting_seq.append(num)
#     return resulting_seq
#
#
# seq = [1, 2, 1, 1, 3, 2]
# print(distinct(seq))
#
#
# def update_light(current):
#     if current == "green":
#         return "yellow"
#     elif current == "yellow":
#         return "red"
#     elif current == "red":
#         return "green"
#
#
# current = "red"
# print(update_light(current))


# def sort_list(sort_by, lst):
#     sorted_lst = sorted(lst, key=lambda x: x[sort_by], reverse=True)
#     return sorted_lst
#
#
# lst = [
#   {"a": 1, "b": 3},
#   {"a": 3, "b": 2},
#   {"a": 2, "b": 40},
#   {"a": 4, "b": 12}
# ]
# print(sort_list("a", lst))
#
#
# def shortcut(s):
#     res_s = ""
#     lowercase_vowels = {"a", "e", "i", "o", "u"}
#     for i in s:
#         if i not in lowercase_vowels:
#             res_s += i
#     return res_s
#
#
# s = "HELLO"
# print(shortcut(s))
#
#
# def series_sum(n):
#     sum = 0.0
#     for i in range(n):
#         sum += 1 / (1 + i * 3)
#     return "{:.2f}".format(sum)
#
#
# n = 3
# print(series_sum(n))


# def get_grade(s1, s2, s3):
#     average = (s1 + s2 + s3) / 3
#     if 100 >= average >= 90:
#         return "A"
#     elif 90 > average >= 80:
#         return "B"
#     elif 80 > average >= 70:
#         return "C"
#     elif 70 > average >= 60:
#         return "D"
#     elif 60 > average >= 0:
#         return "F"
#
#
# print(get_grade(89, 89, 89))


# def DNA_strand(dna):
#     resulting_strand = ""
#     for i in dna:
#         if i == "A":
#             resulting_strand += "T"
#         elif i == "T":
#             resulting_strand += "A"
#         elif i == "C":
#             resulting_strand += "G"
#         elif i == "G":
#             resulting_strand += "C"
#     return resulting_strand
#
#
# dna = "ATTGC"
# print(DNA_strand(dna))


# def past(h, m, s):
#     result = ((h * 3600000) + (m * 60000) + (s * 1000))
#     return result
#
#
# h = 1
# m = 1
# s = 1
# print(past(h, m, s))


# def queue_time(customers, n):
#     if n == 1:
#         return sum(customers)
#
#     tills_times = [0] * n
#
#     for time in customers:
#         tills_times[0] += time
#         tills_times.sort()
#
#     return max(tills_times)
#
#
# customers = [5, 3, 4]
# n = 2
# print(queue_time(customers, n))


# def count_sheep(n):
#     sheep_string = ""
#     if n == 0:
#         return ""
#     else:
#         for i in range(1, n + 1):
#             sheep_string += F"{i} sheep..."
#     return sheep_string
#
#
# n = 9
# print(count_sheep(n))


# def sum_array(arr):
#     if arr is None or len(arr) <= 2 or len(arr) == 0:
#         return 0
#     else:
#         result_arr = sorted(arr)
#         result_arr.pop()
#         result_arr.pop(0)
#     return sum(result_arr)
#
# arr = [1]
# # arr = [6, 2, 1, 8, 10]
# print(sum_array(arr))
#
#
# def apple(x):
#     if int(x) * int(x) > 1000:
#         return "It's hotter than the sun!!"
#     else:
#         return "Help yourself to a honeycomb Yorkie for the glovebox."
#
#
# x = 10
# print(apple(x))
#
#
# def expanded_form(num):
#     num_str = str(num)
#     result = []
#     for i, digit in enumerate(num_str):
#         if digit != "0":
#             result.append(digit + "0" * (len(num_str) - i - 1))
#     return " + ".join(result)
#
#
# num = 12
# print(expanded_form(num))
#

# def tail_swap(strings):
#     a_head, a_tail = strings[0].split(":")
#     # swapped_a = a_head + ":" + strings[1].split(":")[1]
#     b_head, b_tail = strings[1].split(":")
#     # swapped_b = b_head + ":" + strings[0].split(":")[1]
#     swapped_b = b_head + ":" + a_tail
#     swapped_a = a_head + ":" + b_tail
#     return [swapped_a, swapped_b]
#
#
# strings = ["abc:123", "cde:456"]
# print(tail_swap(strings))

# import math
# def square_it(digits):
#     digits_str = str(digits)
#     digits_count = len(digits_str)
#     sqrd_digit_count = int(math.sqrt(digits_count))
#     if sqrd_digit_count * sqrd_digit_count != digits_count:
#         return 'Not a perfect square!'
#     rows = [digits_str[i:i + sqrd_digit_count] for i in range(0, digits_count, sqrd_digit_count)]
#     square = "\n".join(rows)
#
#     return square
#
#
# digits = 1212
# print(square_it(digits))


def find_multiples(integer, limit):
    result = []     # Variable where the resulting list/array will be stored
    i = 1           # Initializes the number iterations
    while (i * integer) <= limit: # While i and the iterations * integer are lesser or equals to five, loop keeps going
        result.append(i * integer) # Stores the iteration results into the array
        i += 1                      # Stops the iteration for never stopping
    return result           # Returns the result

integer = 12
limit = 144
print(find_multiples(integer, limit))


def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        solution = current_year - year_of_birth
        if solution == 1:
            return F"You are {solution} year old."
        else:
            return F"You are {solution} years old."
    elif year_of_birth > current_year:
        solution = year_of_birth - current_year
        if solution == 1:
            return F"You will be born in {solution} year."
        else:
            return F"You will be born in {solution} years."
    elif year_of_birth == current_year:
        return "You were born this very year!"


year_of_birth = 1983
current_year = 1982
print(calculate_age(year_of_birth, current_year))







