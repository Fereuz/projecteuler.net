#Problem 7 - 10001st print

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

i = 3
pm = [2]

while len(pm) <= 10000:
    if all(i % a != 0 for a in pm):
        pm.append(i)
    i = i + 1

print(i - 1)
