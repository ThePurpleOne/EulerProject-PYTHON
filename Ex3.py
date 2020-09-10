"""
https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
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

def getFactors(number):
	factors = []
	for i in range(1, int(sqrt(number)) + 1):
		if number % i == 0:
			factors.append(i)
	return factors

def getBiggestPrimeFactor(number):
	biggestFactor = 0 
	for x in getFactors(number):
		if isPrimeNumber(x) and x > biggestFactor:
			biggestFactor = x
	print(biggestFactor)

start = time.time()
getBiggestPrimeFactor(600851475143)
end = time.time()

print(f"Time taken : {end - start} seconds")