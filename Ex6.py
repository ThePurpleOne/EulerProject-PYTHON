""" 
https://projecteuler.net/problem=6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time 

#The sum of the squares
def sumOfSquares(limit):
	sumOfSquares = 0
	for i in range(1, limit + 1):
		sumOfSquares += i**2
	return sumOfSquares

#The square of the sum
def squareOfSum(limit):
	squareOfSum = 0
	for i in range(1, limit + 1):
		squareOfSum += i
	squareOfSum = squareOfSum**2
	return squareOfSum

def getDifference(limit):
	return (f"difference = {squareOfSum(limit) - sumOfSquares(limit)}")

start = time.time()
print(getDifference(100))
end = time.time()

print(f"Time taken : {end - start} seconds")



