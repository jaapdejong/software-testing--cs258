#!/usr/bin/python

# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    # queue with length 1
    q = Queue(1)
    # test empty stuff
    assert q.empty() == True
    assert q.full() == False     # [bug 5]
    assert q.dequeue() == None   # [bug 4]
    
    # test enqueue 1st
    assert q.enqueue(10) == True
    assert q.empty() == False
    assert q.full() == True      # [bug 3]
    
    # test enqueue 2nd (should fail)
    assert q.enqueue(11) == False
    assert q.empty() == False
    assert q.full() == True

    # test dequeue 1st
    assert q.dequeue() == 10
    assert q.empty() == True
    assert q.full() == False

    # test dequeue 2nd (should fail)
    assert q.dequeue() == None
    assert q.empty() == True
    assert q.full() == False

    # try strange value
    assert q.enqueue(-1) == True
    assert q.dequeue() == -1     # [bug 1]

    q3 = Queue(3)
    assert q3.enqueue(1) == True ;    assert q3.empty() == False ;    assert q3.full() == False
    assert q3.enqueue(2) == True ;    assert q3.empty() == False ;    assert q3.full() == False
    assert q3.enqueue(3) == True ;    assert q3.empty() == False ;    assert q3.full() == True
    assert q3.enqueue(4) == False ;   assert q3.empty() == False ;    assert q3.full() == True
    assert q3.dequeue() == 1 ;        assert q3.empty() == False ;    assert q3.full() == False
    assert q3.dequeue() == 2 ;        assert q3.empty() == False ;    assert q3.full() == False
    assert q3.enqueue(5) == True ;    assert q3.empty() == False ;    assert q3.full() == False
    assert q3.enqueue(6) == True ;    assert q3.empty() == False ;    assert q3.full() == True
    assert q3.enqueue(7) == False ;   assert q3.empty() == False ;    assert q3.full() == True
    assert q3.dequeue() == 3 ;        assert q3.empty() == False ;    assert q3.full() == False
    assert q3.dequeue() == 5 ;        assert q3.empty() == False ;    assert q3.full() == False
    assert q3.dequeue() == 6 ;        assert q3.empty() == True ;     assert q3.full() == False
    assert q3.dequeue() == None ;     assert q3.empty() == True ;     assert q3.full() == False
    
    
    

