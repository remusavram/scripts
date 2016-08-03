'''
Created on Dec 16, 2014

@author: remusav
'''


def small_straight(dice):
    """Score the given roll in the 'Small Straight' Yatzy category,
    
    Args:
      dice: a sorted list of 5 integers indicating the dice rolled
    Returns:
      an integer score
      
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0
    >>> small_straight([1,2,3,5,4])
    0
    >>> small_straight([5,4,3,2,1])
    0

    """
    
    if dice ==[1,2,3,4,5]:
        return sum(dice)
    else:
        return 0


""" Result:

>$ python -m doctest yatzy.py -v
Trying:
    small_straight([1,2,3,4,5])
Expecting:
    15
ok
Trying:
    small_straight([1,2,3,4,4])
Expecting:
    0
ok
Trying:
    small_straight([1,2,3,5,4])
Expecting:
    0
ok
Trying:
    small_straight([5,4,3,2,1])
Expecting:
    0
ok
1 items had no tests:
    yatzy
1 items passed all tests:
   4 tests in yatzy.small_straight
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
"""
