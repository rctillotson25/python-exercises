# -*- coding: utf-8 -*-

# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


letters = 0
digits = 0
chars = [x for x in raw_input()]
for c in chars:
	print c
	if c.isalpha():
		letters += 1
	elif c.isdigit():
		digits += 1
	
print 'LETTERS %d' % letters
print 'DIGITS %d' % digits


