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

ERROR = 0

# Fix this Queue class
class Queue:
    
	def __init__(self,size_max):
		assert size_max > 0
		if ERROR == 1:
			self.max = size_max - 1		#TODO# error 1
		else:
			self.max = size_max		#TODO# ok 1
		self.head = 0
		self.tail = 0
		self.size = 0
		self.data = array.array('i', range(size_max))

	def empty(self):
		return self.size == 0

	def full(self):
		return self.size == self.max

	def enqueue(self,x):
		if ERROR == 2:
			x = x % 1000			#TODO# error 2
		if ERROR != 3:
			if self.size == self.max:	#TODO# ok 3
				return False		#TODO# ok 3
		self.data[self.tail] = x
		self.size += 1
		self.tail += 1
		if self.tail == self.max:
			self.tail = 0
		return True

	def dequeue(self):
		if ERROR != 4:
			if self.size == 0:		#TODO# error 4
				return None		#TODO# error 4
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

def enqueue(q, value):
	try:
		q.enqueue(value)
		q.checkRep()
		result = 0
	except:
		result = 1

	return (value, result)
	
def dequeue(q, expectedValue):
	try:
		actualValue = q.dequeue()
		q.checkRep()
		if expectedValue == actualValue:
			result = 0
		else:
			result = 1
	except:
		result = 1

	return ('dq', result)
	
# create the list for regression test1
def error1():
	q = Queue(2)
	l = []
	l.append(enqueue(q, 1))
	l.append(enqueue(q, 2))
	l.append(dequeue(q, 1))
	l.append(dequeue(q, 2))
	return l
	
# create the list for regression test2
def error2():
	q = Queue(2)
	l = []
	l.append(enqueue(q, 9999))
	l.append(dequeue(q, 9999))
	return l
	
# create the list for regression test3
def error3():
	q = Queue(2)
	l = []
	l.append(enqueue(q, 1))
	l.append(enqueue(q, 2))
	l.append(enqueue(q, 3))
	return l
	
# create the list for regression test4
def error4():
	q = Queue(2)
	l = []
	l.append(dequeue(q, None))
	return l

### This calculates the wrong output for the 4 problems found
ERROR = 1 ; listError1 = error1() ; print "listError1 =", listError1
ERROR = 2 ; listError2 = error2() ; print "listError2 =", listError2
ERROR = 3 ; listError3 = error3() ; print "listError3 =", listError3
ERROR = 4 ; listError4 = error4() ; print "listError4 =", listError4

### This calculates the correct output for the 4 problems found
### it will serve as input for regression_test()
ERROR = 0 ; listOk1 = error1() ; print "listOk1 =", listOk1
ERROR = 0 ; listOk2 = error2() ; print "listOk2 =", listOk2
ERROR = 0 ; listOk3 = error3() ; print "listOk3 =", listOk3
ERROR = 0 ; listOk4 = error4() ; print "listOk4 =", listOk4

