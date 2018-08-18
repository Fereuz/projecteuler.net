#Problem 9 - Special Pythagorean triplet

"""
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a = 1
for a in range(1000):
    b = a + 1
    for b in range(1000):
        c2 = a**2 + b**2
        c = c2**0.5
        if c // 1 == c:
            if a < b < c and a + b + c == 1000:
                print(a, b, c, a * b * c)
        if a + b + c >= 1000:
            break
