# 1. Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

initial_string = str(input("Enter any word: "))
string_length = len(initial_string)
odd_or_even = string_length % 2
first_split = initial_string[:len(initial_string)//2]
second_split = initial_string[len(initial_string)//2:]
odd_first_split = initial_string[:((len(initial_string)//2)+1)]
odd_second_split = initial_string[len(initial_string)//2+1:]
if odd_or_even == 0:
    print("The result is:", second_split+first_split)
elif odd_or_even != 0:
    print("The result is:", odd_second_split+odd_first_split)

# 2. Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

another_string = str(input("Enter any word: "))
list_conversion = list(another_string)
set_conversion = set(another_string)
if len(another_string) == len(set_conversion):
    print("True, all characters in your string are unique")         # sets do NOT accept duplicate chars
elif len(another_string) == len(list_conversion):
    print("False, there are duplicate characters in your string")   # lists accept duplicate chars


#end