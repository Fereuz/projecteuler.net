#Problem 10 - Summation of primes

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#Sieve of Eratosthenes
n = 2 * 10**6
numbers = []
prime_numbers = []

for a in range(2, n):
    numbers.append(a)

p = 2
for b in numbers:
    if b != 0:
        p = b
        prime_numbers.append(p)
    for c in range(2, n):
        try:
            numbers[c * p - 2] = 0
        except IndexError:
            break
        
print(sum(prime_numbers))
