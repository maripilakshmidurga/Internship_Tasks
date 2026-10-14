```python
# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_counts = Counter(shoe_sizes)

n = int(input())
total = 0

for i in range(n):
    size, price = map(int, input().split())

    if shoe_counts[size] > 0:
        total += price
        shoe_counts[size] -= 1

print(total)
```