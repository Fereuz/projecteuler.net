#Problem 4 - Largest palindrome product

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

for multiplier_1 in range(100, 1000):
    for multiplier_2 in range(100, 1000):
        product = multiplier_1 * multiplier_2
        number = str(product)
        numb_symbol = len(number)
        
        if number[0] == number[numb_symbol - 1]:
            if number[1] == number[numb_symbol - 2]:
                if number[2] == number[numb_symbol - 3]:
                    print(product)
