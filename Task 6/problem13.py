# Problem 14: Set .intersection()

# HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

Code:

```python
n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english.intersection(french)))
```