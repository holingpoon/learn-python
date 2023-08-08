from sys import argv
# ^^ can be `from sys import *`, but don't do that
# read the WYSS section for how to run this
# script, first, second, third, fourth = argv
script, first = argv
age = input("How old are you?")


print("The script is called:", script)
print("Your first variable is:", first)
print(f"You are {age} years old")
# print("Input First? {input_first}")
# print("Your third variable is:", third)
# print("Your fourth variable is:", fourth)