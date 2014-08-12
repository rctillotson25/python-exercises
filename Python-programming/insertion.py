# -*- coding: utf-8 -*-

#This algorithm is the array-oriented variant.
#Best case: O(n) - no swaps are necessary 
#Worst case: O(n^2)
#Average case: O(n^2)

x = [1,5,1,5,6,123,616,4,61,462,64,62,245,21,4,14324,5,1,66,1,7,1,7,17,52,5,2546,7,8,8,9,4325,2,345,3,45]


def insertion_sort(x):
	for i in range(1, len(x)):
		j = i
		if i < 5:
			print x[j-1], ' ', x[j]
		while j > 0 and x[j-1] > x[j]:
			x[j-1], x[j] = x[j], x[j-1]
			j = j - 1
			
print x
insertion_sort(x)
print x
