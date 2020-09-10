"""
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

import time

number = 1000

def main():
	for a in range(1, number):
		for b in range(1, number):
			for c in range(1, number):
				if( ((a + b + c) == number) and ( (a**2 + b**2) == c**2) and (a < b and b < c) ):
					return f"a = {a}\nb = {b}\nc = {c}\nresult = {a*b*c}"


start = time.time()
print(main())
end = time.time()
print(f"Time taken: {end - start} seconds")