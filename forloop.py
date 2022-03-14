"""
Program: forloop.py
Author: Jessie Horvath
Last date modified: 02/13/2022

The purpose of this program is to create two for loops. 
The first for loop prints a list of float point numbers.
The second for loop prints odd number from 99 to 33 descending.
"""
x = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
for number in x:
    print(number)


y = range(99, 31, -2)
for number in y:
    print(number)
