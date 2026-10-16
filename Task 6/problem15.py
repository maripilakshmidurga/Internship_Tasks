# Problem 15: Set .difference()

# HackerRank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

Code:

```python
n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english.difference(french)))
```