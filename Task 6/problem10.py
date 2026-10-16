# Problem 10: Designer Door Mat
# HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

# Question:
Given two integers, N and M, design a door mat of size N × M.

1. N must be an odd natural number, and M must be 3 times N.
2. The design should have 'WELCOME' written in the center.
3. The pattern should use only |, . and - characters.
4. Print the design pattern symmetrically.

# Code:

if __name__ == '__main__':
    n, m = map(int, input().split())

    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range(n - 2, 0, -2):
        print(('.|.' * i).center(m, '-'))