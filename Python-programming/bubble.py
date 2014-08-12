# -*- coding: utf-8 -*-

# Bubble Sort Algorithm
# Best case: O(n) - occurs when numbers are already ordered.
# Worst case: O(n^2)
# Average case: O(n^2)

x = [1,5,1,5,6,123,616,4,61,462,64,62,245,21,4,14324,5,1,66,1,7,1,7,17,52,5,2546,7,8,8,9,4325,2,345,3,45]

def bubble_sort(x):
	swapped = True
	while swapped:
		swapped = False
		for i in range(0, len(x) - 1):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				swapped = True
			

print x
bubble_sort(x)
print x


