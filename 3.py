#Problem 3 - Largest prime factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

i = 2
Number = 600851475143

while Number >= 0:
    if Number % i == 0:
        print(i)
        ans = Number / i
        print('ans = ', ans)
        Number = ans
    i = i + 1
