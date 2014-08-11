# -*- coding: utf-8 -*-

# Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def has_even_digits(x):
	p = x / 10
	r = x % 10
	if p < 1:
		return True
	elif r % 2 == 0:
		return has_even_digits(p)
	else:
		return False
	
nums = []
nums = [x for x in range(100,300) if has_even_digits(x) == True]
print ','.join(map(str, nums))