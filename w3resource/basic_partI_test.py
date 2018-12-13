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

    def test_q6_separe2LT(self):
        abc = 'a,b,c,d,e,f'
        pair = q6_separe2LT(abc)
        self.assertEqual(len(pair),2)

    def test_q7_displayExtension(self):
        self.assertEqual(q7_displayExtension('abc.java'),'java')
        self.assertEqual(q7_displayExtension('somePy.py'),'py')
        self.assertEqual(q7_displayExtension('none'),'')
        self.assertEqual(q7_displayExtension('withDot.'),'')

    def test_q8_firstLastColor(self):
        colors = q8_firstLastColor()
        self.assertEqual(len(colors),2)
        self.assertEqual(colors[0],"Red")
        self.assertEqual(colors[1],"Black")

    def test_q9_examination_date(self):
        self.assertEqual('11 / 12 / 2014' in q9_examination_date(), True)
        self.assertEqual('examination' in q9_examination_date(), True)

    def test_q10_pyramidN(self):
        self.assertEqual(q10_pyramidN(1),3)
        self.assertEqual(q10_pyramidN(5),615)

    def test_q11_documentsBuiltinF(self):
        self.assertNotEqual(len(q11_documentsBuiltinF('abs')),0)
        self.assertNotEqual(len(q11_documentsBuiltinF('min')),0)
        self.assertNotEqual(len(q11_documentsBuiltinF('list')),0)

        self.assertEqual(len(q11_documentsBuiltinF('avengers')),0)

    def test_q12_getMonthYear(self):
        cal = q12_getMonthYear(2012,2)
        self.assertNotEqual(len(cal),0)

    def test_q14_daysBetween(self):
        self.assertEqual(q14_daysBetween((2018,12,1),(2018,12,1)),0)
        self.assertNotEqual(q14_daysBetween((2018,12,2),(2018,12,5)),1)

    def test_q15_getVolumeSphere(self):
        self.assertEqual(q15_getVolumeSphere(2),33.51)

    def test_q16_near_oneOrTwoThounsand(self):
        self.assertEqual(q16_near_oneOrTwoThounsand(2000),True)
        self.assertTrue(q16_near_oneOrTwoThounsand(2000))
        self.assertFalse(q16_near_oneOrTwoThounsand(1200))
        self.assertTrue(q16_near_oneOrTwoThounsand(1000))
        self.assertFalse(q16_near_oneOrTwoThounsand(200))
        self.assertTrue(q16_near_oneOrTwoThounsand(1001))
        self.assertTrue(q16_near_oneOrTwoThounsand(2012))

    def test_q17_sumOfValues(self):
        self.assertEqual(q17_sumOfValues(1,1,1),9)
        self.assertEqual(q17_sumOfValues(1,2,3),6)
        self.assertEqual(q17_sumOfValues(2,2,2),18)
        self.assertEqual(q17_sumOfValues(3,5,7),15)
        self.assertEqual(q17_sumOfValues(1,1,33),35)
        self.assertEqual(q17_sumOfValues(1,12,1),14)

    def test_q18_startWithOrAdd(self):
        self.assertTrue(q18_startWithOrAdd('Is','IsTV'))
        self.assertTrue(q18_startWithOrAdd('Is','TV'))
        self.assertTrue(q18_startWithOrAdd('Is','IsEmpty'))
        self.assertTrue(q18_startWithOrAdd('Is','Empty'))

    def test_q20_nCopyString(self):
        self.assertEqual(q20_nCopyString('asdf',3),"asdfasdfasdf")
        self.assertEqual(q20_nCopyString('12345',4),"12345123451234512345")
        self.assertEqual(q20_nCopyString('ok',0),"")
        self.assertEqual(q20_nCopyString('ok',1),"ok")

    def test_q21_descriEvenOdd(self):
        self.assertEqual(q21_descriEvenOdd(10), '10 is EVEN')
        self.assertEqual(q21_descriEvenOdd(2), '2 is EVEN')
        self.assertEqual(q21_descriEvenOdd(200), '200 is EVEN')
        self.assertEqual(q21_descriEvenOdd(64), '64 is EVEN')
        self.assertEqual(q21_descriEvenOdd(34), '34 is EVEN')

        self.assertEqual(q21_descriEvenOdd(203), '203 is ODD')
        self.assertEqual(q21_descriEvenOdd(1), '1 is ODD')
        self.assertEqual(q21_descriEvenOdd(45), '45 is ODD')
        self.assertEqual(q21_descriEvenOdd(93), '93 is ODD')
        self.assertEqual(q21_descriEvenOdd(91), '91 is ODD')

    def test_q22_count4(self):
        self.assertEqual(q22_count4([21,4,3,1,5,7,4,98]), 2)
        self.assertEqual(q22_count4([8,4,3,1,5,7,4,98]), 2)
        self.assertEqual(q22_count4([76,4,3,1,5,7,4,98]), 2)
        self.assertEqual(q22_count4([9,45,32,4,5,7,4,4]), 3)
        self.assertEqual(q22_count4([23,4,3,1,5,7,8,98]), 1)

    def test_q23_getfirst2Ch(self):
        self.assertEqual(q23_getfirst2Ch('fdaserq'),'fd')
        self.assertEqual(q23_getfirst2Ch('A'),'A')
        self.assertEqual(q23_getfirst2Ch(''),'')

    def test_q24_isVowel(self):
        self.assertEqual(q24_isVowel('A'),True)
        self.assertEqual(q24_isVowel('o'),True)
        self.assertEqual(q24_isVowel(''),False)
        self.assertEqual(q24_isVowel('C'),False)

    def test_q25_eInGroup(self):
        self.assertTrue(q25_eInGroup(1,[1,34,56,7]))
        self.assertTrue(q25_eInGroup(56,[1,34,56,7]))
        self.assertTrue(q25_eInGroup(8,[5,8,5,6,7]))

        self.assertFalse(q25_eInGroup(7,[1,3,4,5,67]))
        self.assertFalse(q25_eInGroup(9,[1,3,4,567]))
        self.assertFalse(q25_eInGroup(9,[6,3,4,56,7]))


if __name__ == '__main__':
    unittest.main()
