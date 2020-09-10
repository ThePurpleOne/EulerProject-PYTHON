"""
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

def main():
	resultat = 0
	for i in range(0, 1000):
		if (i % 3) == 0: 
			resultat += i
		elif (i % 5) == 0:
			resultat += i
	print(resultat)

start = time.time()
main()
end = time.time()

print(f"Time taken: {end - start} seconds")

