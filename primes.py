"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    primes=[]
    check = 2

    if number_of_primes<=0:
        raise ValueError


    while len(primes) < number_of_primes:
        primeTest = [check for i in primes if check%i == 0]
        primes += [] if primeTest else [check]
        check += 1
    return primes


