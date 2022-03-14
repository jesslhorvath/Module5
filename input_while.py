"""
Program: input_while.py
Author: Jessie Horvath
Last date modified: 02/13/2022

The purpose of this program is to prompt a user for a numeric
input between 1 and 100. It then uses loops to determine if the user 
would like to continue inputting numbers and adding them to the list
or quit and print the list of inputs.
"""
input_storage = []

user_input = input("Enter a number between 1 and 100 or 'quit' to exit: ")

while user_input != "quit":
    int(user_input)
    while int(user_input) not in range(1, 101):
        print("That number is not between 1 and 100. Try again.")
        user_input = int(input("Enter a new number between 1 and 100: "))
    input_storage.append(user_input)
    user_input = input(
        "Enter another number between 1 and 100 or 'quit' to exit: ").lower()

for x in input_storage:
    print(x)

"""
Test results:
Input: 5 6 7 8 quit
Output: 5 6 7 8

Input: 23 104
Output: That number is not between 1 and 100. Try again.
Input: 7 quit
Output: 23 7
"""
