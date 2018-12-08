#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Some wonderful lines in python """
"""Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php"""


import unittest
from basic_partI import *

import re

class BasicPartITest(unittest.TestCase):

    def test_q1_twinkle(self):
        self.assertNotEqual(q1_twinkle(), '')
        self.assertEqual(q1_twinkle().count('\n'),5)
        self.assertEqual(q1_twinkle().lower().count('twinkle'),4)

    def test_q2_python_version(self):
        self.assertNotEqual(q2_python_version(), '')

    def test_q3_diplayCurrentDate(self):
        self.assertNotEqual(q3_diplayCurrentDate(), '')
        re.match("\d{4}-\d\d-\d\d \d\d:\d\d:\d\d", q3_diplayCurrentDate())

    def test_q4_circleArea(self):
        self.assertNotEqual(q3_circleArea(21), 0)
        self.assertLess( 2.5,q3_circleArea(2))
        self.assertEqual(q3_circleArea(1.1), 3.8013271108436504)

    def test_q5_reverseFirstLast(self):
        self.assertEqual(q5_reverseFirstLast('John','Doe'), 'Doe John')
        self.assertNotEqual(q5_reverseFirstLast('John','Doe'), '')

    def test_q7_displayExtension(self):
        self.assertEqual(q7_displayExtension('abc.java'),'java')
        self.assertEqual(q7_displayExtension('somePy.py'),'py')
        self.assertEqual(q7_displayExtension('none'),'')
        self.assertEqual(q7_displayExtension('withDot.'),'')

    def test_q6_separe2LT(self):
        abc = 'a,b,c,d,e,f'
        pair = q6_separe2LT(abc)
        self.assertEqual(len(pair),2)

if __name__ == '__main__':
    unittest.main()
