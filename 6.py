#Problem 6 - Sum square difference

"""
The sum of the squares of the first ten natural number in,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and squar of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the squar of the sum.
"""

c = 0
d = 0

for a in range(1, 101):
    b = a**2
    c = c + b
ans1 = c

for a in range(1, 101):
    d = d + a
c = d**2
ans2 = c

print(ans2 - ans1)

