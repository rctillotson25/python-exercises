# -*- coding: utf-8 -*-


# Date: 09/16/2014
# Program: Recursive binary search algorithm written in 
# python that operates over an array of integers sorted in non-decreasing order.




n = []


def search(x, low, high):
	global n
	mid = (high + low) / 2
	if low > high:
		return False
	else:
		if n[mid] > x:
			return search(x, low, mid - 1)
		elif x > n[mid]:
			return search(x, mid + 1, high)
		else:
			return True

for x in range(1, 1000):
	if x%3 == 0:
		n.append(x)
print search(int(raw_input('>')), 0, len(n) -1)
