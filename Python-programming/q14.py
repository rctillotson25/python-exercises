# -*- coding: utf-8 -*-

# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

upper = 0
lower = 0
x = [x for x in raw_input()]
for n in x:
	if n.isalpha():
		if n.istitle():
			upper += 1
		else:
			lower += 1
print 'Upper: %d' % upper
print 'Lower: %d' % lower
			
		