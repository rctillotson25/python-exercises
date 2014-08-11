# -*- coding: utf-8 -*-
# Question 9
# Level 2

# Question��
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

out_string = []

while True:
	s = raw_input()
	if s:
		out_string.append(s.upper())
	else:
		break

for s in out_string:
	print s
