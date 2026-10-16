# Problem 5: Write a function
# HackerRank Link: https://www.hackerrank.com/challenges/write-a-function/tutorial

# Question:
Given a year, determine whether it is a leap year. If it is a leap year, return True; otherwise, return False.

# Code:

def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))