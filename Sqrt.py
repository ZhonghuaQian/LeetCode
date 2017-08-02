# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:54:54 2017

@author: qzhoo
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = 1
        while(True):
            t2 = 0.5 * (t + x / t)
            if t2 - t < 0.5 and t2 - t > -0.5:
                return int(t2+1)
            else:
                t = t2

answer = Solution()
print(answer.mySqrt(21))