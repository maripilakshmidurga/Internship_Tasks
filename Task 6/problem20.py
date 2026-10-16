# Problem 20: Validating and Parsing Mobile Numbers

# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

Code:

```python
import re

T = int(input())

for _ in range(T):
    number = input()
    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
```