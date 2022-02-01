# Task : Read a given string, change the character at a given index and then print the modified string.
# Function Description: Complete the mutate_string function in the editor below. mutate_string has the
# following parameters:
#
#     string string: the string to change
#     int position: the index to insert the character at
#     string character: the character to insert
#
# Returns string: the altered string
#
# Input Format
#
# The first line contains a string,
# .
# The next line contains an integer , the index location and a string , separated by a space.

string = "nino"
position = 3
character = "a"

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    new_string = "".join(string_list)
    print(new_string)

mutate_string(string=string, position=position, character=character)


# In this challenge, the user enters a string and a substring. You have to print the number of times
# that the substring occurs in the given string. String traversal will take place from left to right,
# not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
#
# Constraints
# Each character in the string is an ascii character.
#
# Output the integer number indicating the total number of occurrences of the substring in the original string.

#without overlapping
def count_substring(string, sub_string):
    return (string.count(sub_string, 0, len(string)))

print(count_substring("ninoninonin", "nin"))

#with overlapping
def count_substring(string, sub_string):
    sub_len = len(sub_string)
    counter = 0
    occur = 0
    for _ in string:
        if sub_string == string[counter: sub_len + counter]:
            occur += 1
        counter += 1
    return occur

print("overlapping:")
print(count_substring("ninoninonin", "nin"))

# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    swapted_string = ''
    for letter in s:
        if letter.isupper():
            swapted_string += letter.lower()
        else:
            swapted_string += letter.upper()
    return swapted_string

print(swap_case("NiNo"))




# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    splited_list = line.split(" ")
    joined_list = "-".join(splited_list)
    return joined_list

print(split_and_join("nino i ti"))



# Task
#
# You are given a string
# .
# Your task is to find out if the string contains: alphanumeric characters, alphabetical characters,
# digits, lowercase and uppercase characters.

def check_characters():
    s = input()
    alnum = False
    alphab = False
    digit = False
    lower = False
    upper = False
    for _ in s:
        if _.isalnum():
            alnum = True
        if _.isalpha():
            alphab = True
        if _.isdigit():
            digit = True
        if _.islower():
            lower = True
        if _.isupper():
            upper = True
    print(alnum)
    print(alphab)
    print(digit)
    print(lower)
    print(upper)