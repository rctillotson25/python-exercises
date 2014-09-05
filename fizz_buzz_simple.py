#-*- coding: utf-8 -*-





# Sys package is needed for printing w.o space.
import sys

for i in range(1,101):
	if i%3 == 0:
		sys.stdout.write('Fizz')
	if i%5 == 0:
		sys.stdout.write('Buzz')
	if (not i%5 == 0 and not i%3 == 0):
		sys.stdout.write(str(i))
	if not i == 100:
		print(','),

print 




