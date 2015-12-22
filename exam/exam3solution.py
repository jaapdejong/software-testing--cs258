#!/usr/bin/python

# Regression Testing
# ------------------
# The goal of this problem is for you to write a regression tester
# for the Queue class.
# 
# Begin by finding and fixing all of the bugs in the Queue class. Next,
# define the function regression_test to take in a list of enqueue inputs
# and dequeue indicators (the returned list of the previous problem) and
# repeat those method calls using the fixed Queue.
# 
# That is, after fixing the Queue class, create a new Queue instance,
# and call the method corresponding to the indicator in the list
# for each item in the list:
# 
# Call the enqueue function whenever you come across an integer, using that
#     integer as the argument.
# Call the dequeue function whenever you come across the 'dq' indicator.

import array
import random

# Fix this Queue class
class Queue:
    
	def __init__(self,size_max):
		assert size_max > 0
		self.max = size_max
		self.head = 0
		self.tail = 0
		self.size = 0
		self.data = array.array('i', range(size_max))

	def empty(self):
		return self.size == 0

	def full(self):
		return self.size == self.max

	def enqueue(self,x):
		if self.size == self.max:
			return False
		self.data[self.tail] = x
		self.size += 1
		self.tail += 1
		if self.tail == self.max:
			self.tail = 0
		return True

	def dequeue(self):
		if self.size == 0:
			return None
		x = self.data[self.head]
		self.size -= 1
		self.head += 1
		if self.head == self.max:
			self.head = 0
		return x

	def checkRep(self):            
		assert self.tail >= 0
		assert self.tail < self.max
		assert self.head >= 0
		assert self.head < self.max
		if self.tail > self.head:
			assert (self.tail-self.head) == self.size
		if self.tail < self.head:
			assert (self.head-self.tail) == (self.max-self.size)
		if self.head == self.tail:
			assert (self.size==0) or (self.size==self.max)    

listOk1 = [(1, 0), (2, 0), ('dq', 0), ('dq', 0)]
listOk2 = [(9999, 0), ('dq', 0)]
listOk3 = [(1, 0), (2, 0), (3, 0)]
listOk4 = [('dq', 0)]

# Write a regression tester for the Queue class
def regression_test(lst):
	q = Queue(2); 
	for i in range(len(lst)):
		tup = lst[i]
		value = tup[0]
		expectedResult = tup[1]
		if value != 'dq':
			q.enqueue(value)
			q.checkRep()
		else:
			q.dequeue()
			q.checkRep()

regression_test(listOk1)
regression_test(listOk2)
regression_test(listOk3)
regression_test(listOk4)
print "Well Done!"

