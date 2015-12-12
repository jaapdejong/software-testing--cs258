#!/usr/bin/python

# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
def luhn_checksum(n):
	checksum = 0
	double = False
	while n != 0:
		digit = n % 10
		n //= 10
		if double:
			digit *= 2
			if digit >= 10:
				digit -= 9
		checksum += digit
		double = not double
	print n, checksum % 10
	return checksum % 10

def is_luhn_valid(n):
	return luhn_checksum(n) == 0

