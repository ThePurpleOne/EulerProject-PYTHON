"""
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import time
from math import floor, sqrt

def isPrimeNumber(number):
	if number == 1: 					# 1 is not prime
		return False 
	if number == 2:						# 2 is a prime number
		return True
	if number > 2 and number % 2 == 0:	# even numbers are not prime
		return False

	for i in range( 3, floor( sqrt(number) + 1 ), 2 ):
		if number % i == 0: 
			return False
	return True

def nthPrime(number):
	primeNumber = 1 #counts the number of primes
	counter = 1 
	while primeNumber != number:
		counter += 2 #inc even when not prime
		if isPrimeNumber(counter):
			primeNumber += 1 
	return counter

start = time.time()
print(nthPrime(10001))
end = time.time()

print(f"Time taken : {end - start} seconds")