# Problem 6: Print Function
# HackerRank Link: https://www.hackerrank.com/challenges/python-print/tutorial

# Question:
The included code stub will read an integer, n, from STDIN.

Without using any string methods, print the numbers from 1 to n consecutively, without spaces.

# Code:

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')