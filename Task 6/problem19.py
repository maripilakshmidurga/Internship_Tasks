# Problem 19: Company Logo

# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

Code:

```python
if __name__ == '__main__':
    s = input()

    from collections import Counter

    count = Counter(s)

    for char, freq in sorted(count.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, freq)
```