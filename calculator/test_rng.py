'''importing modules'''

import unittest
import randomcalc

class Testrng(unittest.TestCase):
    '''write test cases'''
    def test1_rng(self):
        '''check if true'''
        flag = False
        test = randomcalc.rng()
        if 0 <= test <= 1:
            flag = True
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()
