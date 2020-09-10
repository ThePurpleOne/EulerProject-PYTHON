"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

#only works with a pair number of digits
def isPalindrome(number):
	stredNumber = str(number)
	#print(len(stredNumber))
	left_part = stredNumber[0:int(len(stredNumber)/2)]
	right_part = stredNumber[int(len(stredNumber)/2 ):]
	if left_part == right_part[::-1]:
		return True
	else:
		return False

def main():
	produit = 0
	for x in range(100, 1000):
		for y in range(100, 1000):
			if isPalindrome((x * y)):
				if (x*y) > produit:
					produit = x*y
					result = (f" {x} * {y} = {x * y}")
	print(result)

start = time.time()
main()
end = time.time()

print(f"Time taken : {end - start} seconds")


