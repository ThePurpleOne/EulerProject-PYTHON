"""
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

def main():
	somme = 2
	for x in range(1, 2000000 + 1, 2):
		if( isPrimeNumber(x) ):
			somme += x
			# print(x)
	return somme


start = time.time()
print(main())
end = time.time()
print(f"Time taken: {end - start} seconds")