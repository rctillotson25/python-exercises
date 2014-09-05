# -*- coding: utf-8 -*-

# This is a basic FizzBuzz program that will
# print out all the numbers between 1 and 100.
# If a number is divisible by 3, Fizz is printed.
# If a number is divisible by 5, Buzz is printed.
# If a number is divisible by both, FizzBuzz is printed.
# If a number is not divisible by either, then the number is printed.
# The least common multiple of 3 and 5 is 15

import sys

#inclusive range functiton
def rangec(a, b):
	return range(a, b+1)

def printN(n):
	div_3 = n%3 == 0
	div_5 = n%5 == 0
	if div_3:
		sys.stdout.write('Fizz')
	if div_5:
		sys.stdout.write('Buzz')
	if not div_3 and not div_5:
		sys.stdout.write(str(n)),
	print(','),


# for n 1 - 100
for i in rangec(1,100):
	printN(i)

