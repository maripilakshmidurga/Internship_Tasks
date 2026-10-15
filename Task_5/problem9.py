# Problem 9: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter

n = int(input())
words = []

for i in range(n):
    words.append(input())

counts = Counter(words)

print(len(counts))
print(*counts.values())