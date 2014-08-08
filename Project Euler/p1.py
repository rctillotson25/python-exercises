# -*- coding: utf-8 -*-

#Find the sum of all the multiples of 3 or 5 below 1000.

#Brute force method

isMultiple = lambda n : (n % 3 == 0) or (n % 5 == 0)
sum = 0
for x in range(0,1000):
	if isMultiple(x):
		sum += x
print sum


