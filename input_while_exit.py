"""
Program: input_while.py
Author: Jessie Horvath
Last date modified: 02/13/2022

The purpose of this program is to prompt a user for a numeric
input between 1 and 100. It then uses loops to determine if the user 
would like to continue inputting numbers and adding them to the list
or break statements to quit and print the list of inputs.
"""
input_storage = []


while True:
    while True:
        user_input = input(
            "Enter a number between 1 and 100 or 'quit' to exit: ")
        if user_input == "quit":
            break
        try:
            num_user_input = int(user_input)
            if num_user_input not in range(1, 101):
                print("That number is not between 1 and 100. Try again.")
            else:
                break
        except ValueError:
            print("That is not a number. Enter a number.")

    if user_input == "quit":
        break
    input_storage.append(num_user_input)

for x in input_storage:
    print(x)

"""
Test Results:
Input: 4 5 6 quit
Output: 4 5 6 

Input: 2 jessie
Output: That is not a number. Enter a number.
Input: 5 6 -10
Output: That number is not between 1 and 100. Try again.
Input: 2 quit
Output: 2 5 6 2
"""
