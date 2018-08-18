#Ptoblem 12 - Longest Collatz sequence
#Python version - 3.5.2

"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

If can be seen that sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def even_number(n):
    n = n / 2
    return int(n)

def odd_number(n):
    n = 3 * n + 1
    return int(n)

def reverse_even_number(n):
    n = n * 2
    return int(n) 

def reverse_odd_number(n):
    n = (n - 1) / 3
    return int(n)

while counter <= 10:
    break
