#!/usr/bin/env python
# -*- coding: utf-8 -*-



""" Some wonderful lines in python """
"""Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php"""

from math import *

def q1_twinkle():
    '''1. Write a Python program to print the following string in a specific
    format (see the output). Go to the editor Sample String : "Twinkle, twinkle,
    little star, How I wonder what you are! Up above the world so high, Like a
     diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
     Output :

    Twinkle, twinkle, little star,
    	How I wonder what you are!
    		Up above the world so high,
    		Like a diamond in the sky.
    Twinkle, twinkle, little star,
    	How I wonder what you are
    '''
    string = 'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are'

    #print(string)

    return string

import platform as platf

def q2_python_version():
    '''Write a Python program to get the Python version you are using.'''
    current_version = platf.version()
    return current_version

import datetime
def q3_diplayCurrentDate():
    '''Write a Python program to display the current date and time.'''
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return currentDate

from math import pi
def q4_circleArea(r):
    ''' Write a Python program which accepts the radius of a circle from the
    user and compute the area.'''
    return (r*r) * pi

def q5_circleArea(first,last):
    '''Write a Python program which accepts the user's first and last name
    and print them in reverse order with a space between them. '''
    return  '{ } { }'.format(last,first)

def q7_displayExtension(filename):
    '''. Write a Python program to accept a filename from the user and
    print the extension of that.
    Sample filename : abc.java
    Output : java '''
    sp =  filename.split('.')
    if (len(sp)>1):
        return sp[-1]
    return ''

def q6_separe2LT(sep):
    ''' Write a Python program which accepts a sequence of comma-separated
    numbers from user and generate a list and a tuple with those numbers.'''
    l = sep.split(',')
    t = tuple(l)
    return l,t
    
if __name__ == '__main__':
    print('some test')
