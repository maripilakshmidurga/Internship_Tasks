# Problem 4: Loops
# HackerRank Link: https://www.hackerrank.com/challenges/python-loops/tutorial

# Question:
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where i < n, print i² on a separate line.

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)