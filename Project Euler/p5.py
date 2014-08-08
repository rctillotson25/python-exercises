# -*- coding: utf-8 -*-

#Project Euler Problem #5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# GIVEN:
# 2520 is smallest for integers from 1 to 10, 
# so can start at 2520 and increment by 2520.

range1 = lambda start, end: range(start, end+1)

divisible = False
x = 2520
while True:
	for y in range1(1,20):
		if (x % y == 0):
			divisible = True
		else:
			divisible = False
			break
	if divisible == True:
		print x
		break
	x += 2520

